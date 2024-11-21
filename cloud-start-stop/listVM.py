import functions_framework
import requests
from getToken import getToken
from flask import render_template

@functions_framework.http
def listVM(request):
    project = '????'
    zone = 'us-central1-a'
    resp = request.get_json(silent=True)
    if not resp:
        resp = request.args
    if resp:
        if 'project' in resp:
            project = resp['project']
        if 'zone' in resp:
            zone = resp['zone']

    token = getToken()
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
    urlCom = request.url.replace('/list','')
    if not response.status_code == 200:
        return 'List! ({})'.format(response.status_code)
    else:
        if 'items' in response.json():
            items = response.json()['items']
            for item in items:
                accessConfigs = item['networkInterfaces'][0]['accessConfigs'][0]
                natIP = accessConfigs['natIP'] if 'natIP' in accessConfigs else ''
                vmList += ("<tr> <td>{}</td>  <td>{}</td> <td> <a href='{}&vm={}&com=start'> START </a> </td>" 
                           "   <td>&nbsp; <a href='{}&vm={}&com=stop'> STOP </a>&nbsp; </td>  <td> {}</td></tr> \n"
                           .format(item['name'],item['status'],urlCom,item['name'],urlCom,item['name']
                                   ,natIP ))
        vmList = '<b><table>{}</table></b>'.format(vmList)

    # return 'List VM ({}) <br><br> {}'.format(response.status_code,vmList)
    return render_template('index.html',code=response.status_code,data=vmList,project=project)