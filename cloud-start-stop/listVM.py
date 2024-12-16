import functions_framework
import requests
from getToken import getToken
from flask import render_template
from run_command import run_command
from get_param import get_param

@functions_framework.http
def listVM(request):
    urlCom = request.url.split('?')[0].replace('http:','https:')  # todo http ??
    print('urlCom =',urlCom)
    com, projects, vm, zone = get_param(request)
    if zone == '':
        return 'Add param zone=  (url?zone=my_zone) - by default zone=us-central1-a'
    elif projects == '':
        return 'Add param projects=  (url?projects=my_projects_id or url?projects=my_projects1_id,my_project2_id)'

    vmList=""
    codes=[]
    token = getToken()
    if token.startswith('Error'):
        return render_template('index.html',codes='',data=token,projects=projects)
    if not(com == '' and vm == ''):
        return run_command(com, projects, token, vm, zone)

    for project  in projects.split(","):
        codes, vmList = one_project(codes, project, token, urlCom, vmList, zone)

    vmList = '<b><table>{}</table></b>'.format(vmList)
    return render_template('index.html',codes=','.join(codes),data=vmList,projects=projects)


def one_project(codes, project, token, urlCom, vmList, zone):
    url = ("https://compute.googleapis.com/compute/v1/projects/{}/zones/{}/instances"
           .format(project, zone))
    print(url)
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Accept': 'application/json',
    }
    params = {
        'key': 'null',
    }
    response = requests.get(
        url,
        params=params,
        headers=headers,
    )
    if response.status_code == 200:
        if 'items' in response.json():
            items = response.json()['items']
            for item in items:
                accessConfigs = item['networkInterfaces'][0]['accessConfigs'][0]
                natIP = accessConfigs['natIP'] if 'natIP' in accessConfigs else ''
                vmList += ('<tr> <td>{}</td> <td>{}</td>  <td>{}</td> \n'
                           '<td> <button onclick="com_vm(\'{}?vm={}&com=start&projects={}&zone={}\')">&nbsp;START</button> </td> \n'
                           '<td> <button onclick="com_vm(\'{}?vm={}&com=stop&projects={}&zone={}\')">&nbsp;STOP</button> </td> \n'
                           '<td> {}</td></tr> '
                           .format(project, item['name'], item['status'],
                                   urlCom, item['name'], project, zone,
                                   urlCom, item['name'], project, zone
                                   , natIP))
    codes.append(str(response.status_code))
    return codes, vmList