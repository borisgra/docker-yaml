import functions_framework
import requests
from getToken import getToken
from flask import render_template
from run_command import run_command
from get_param import get_param
import time

@functions_framework.http
def listVM(request):
    com, project, vm, zone = get_param(request)

    token = getToken()

    resp_command = ''
    if com and vm:
        # time.sleep(1) # Sleep for 1 second
        resp_command = run_command(com, project, token, vm, zone)

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
    urlCom = request.url.split('?')[0]
    if not response.status_code == 200:
        return 'List! ({})'.format(response.status_code)
    else:
        if 'items' in response.json():
            items = response.json()['items']
            for item in items:
                accessConfigs = item['networkInterfaces'][0]['accessConfigs'][0]
                natIP = accessConfigs['natIP'] if 'natIP' in accessConfigs else ''
                vmList += ("<tr> <td>{}</td>  <td>{}</td> \n"
                           "<td> <a href='{}?vm={}&com=start&project={}&zone={}'> START </a> &nbsp; </td> \n" 
                           "<td> <a href='{}?vm={}&com=stop&project={}&zone={}'> STOP  </a> &nbsp; </td> \n"
                           "<td> {}</td></tr> <br>"
                           .format(item['name'],item['status'],
                                   urlCom,item['name'],project,zone,
                                   urlCom,item['name'],project,zone
                                   ,natIP ))
        vmList = '<b><table>{}</table></b>'.format(vmList)

    return render_template('index.html',code=response.status_code,data=vmList,project=project,resp_command=resp_command)