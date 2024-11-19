import functions_framework
import requests
from getToken import getToken

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
        items = response.json()['items']
        for item in items:
            accessConfigs = item['networkInterfaces'][0]['accessConfigs'][0]
            vmList += ("<b>{}  {} <a href='{}&vm={}&com=start'> START </a>"
                       " .. <a href='{}&vm={}&com=stop'> STOP </a> .. {}"
                       .format(item['name'],item['status'],urlCom,item['name'],urlCom,item['name']
                               ,accessConfigs['natIP'] if 'natIP' in accessConfigs else '' ))

    return 'List VM ({}) <br><br> {}'.format(response.status_code,vmList)