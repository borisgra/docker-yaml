import functions_framework
import requests
from getToken import getToken
from flask import render_template
from run_command import run_command
from get_param import get_param
from datetime import datetime

@functions_framework.http
def listVM(request,ver):
    urlCom = request.url.split('?')[0].replace('http:','https:')  # todo http ??
    a,b,c,_ = ver.split('\n')
    version = ('version:1.0.{} {} compile {} started {}'
               .format(a,b,c,str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))))
    print('urlCom =',urlCom,'version=',version)
    com, projects, vm, zone = get_param(request)
    if projects == '':
        return 'Add param (url?projects=my_projects1_id,my_project2_id,..)'

    vmList=""
    codes=[]
    token = getToken()
    if token.startswith('Error'):
        return render_template('index.html',codes='',data=token,projects=projects,ver=version)
    if not(com == '' and vm == ''):
        return run_command(com, projects, token, vm, zone)

    for project  in projects.split(","):
        codes, vmList = one_project(codes, project, token, urlCom, vmList, zone)

    vmList = ('<b><table> <th>Project</th> <th>Name VM</th> <th>Zone</th> <th>Status</th> <th>Start</th> <th>Stop</th> <th>natIP</th>\n '
              '{}</table></b>').format(vmList)
    return render_template('index.html',codes=','.join(codes),data=vmList,projects=projects,ver=version)


def one_project(codes, project, token, urlCom, vmList, zone):
    # url = ("https://compute.googleapis.com/compute/v1/projects/{}/zones/{}/instances"  # list - one zone
    url = "https://compute.googleapis.com/compute/v1/projects/{}/aggregated/instances".format(project) # aggregatedList - all zones
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
                if 'instances' in items[item]:
                    instances = items[item]['instances']
                    for instance in instances:
                        name = instance['name']
                        status = instance['status']
                        zone = instance['zone'].split('/')[-1]
                        accessConfigs = instance['networkInterfaces'][0]['accessConfigs'][0]
                        natIP = accessConfigs['natIP'] if 'natIP' in accessConfigs else ''

                        vmList += ('<tr> '
                                   '<td>{}</td> <td>{}</td> <td>{}</td> <td>{}</td> \n'
                                   '<td> <button onclick="com_vm(\'{}?vm={}&com=start&projects={}&zone={}\')">&nbsp;START</button> </td> \n'
                                   '<td> <button onclick="com_vm(\'{}?vm={}&com=stop&projects={}&zone={}\')">&nbsp;STOP</button> </td> \n'
                                   '<td> {}</td></tr> '
                                   .format(project, name, zone, status,
                                           urlCom,name, project, zone,
                                           urlCom, name, project, zone
                                           , natIP))
    codes.append(str(response.status_code))
    return codes, vmList