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
    com, project, vm, zone = get_param(request)
    if zone == '':
        return 'Add param zone=  (url?project=my_project_name) - by default zone=us-central1-a'
    elif project == '':
        return 'Add param project=  (url?project=my_project_name or urlurl?project=my_project_name&project=my_project_name)'

    token = getToken()

    if not(com == '' and vm == ''):
        return run_command(com, project, token, vm, zone)

    url = ("https://compute.googleapis.com/compute/v1/projects/{}/zones/{}/instances"
           .format(project,zone))
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

    vmList=""
    if not response.status_code == 200:
        return 'List! ({})'.format(response.status_code)
    else:
        if 'items' in response.json():
            items = response.json()['items']
            for item in items:
                accessConfigs = item['networkInterfaces'][0]['accessConfigs'][0]
                natIP = accessConfigs['natIP'] if 'natIP' in accessConfigs else ''
                vmList += ('<tr> <td>{}</td>  <td>{}</td> \n'
                           '<td> <button onclick="com_vm(\'{}?vm={}&com=start&project={}&zone={}\')">&nbsp;START</button> </td> \n' 
                           '<td> <button onclick="com_vm(\'{}?vm={}&com=stop&project={}&zone={}\')">&nbsp;STOP</button> </td> \n' 
                           '<td> {}</td></tr> <br>'
                           .format(item['name'],item['status'],
                                   urlCom,item['name'],project,zone,
                                   urlCom,item['name'],project,zone
                                   ,natIP ))
        vmList = '<b><table>{}</table></b>'.format(vmList)

    return render_template('index.html',code=response.status_code,data=vmList,project=project)