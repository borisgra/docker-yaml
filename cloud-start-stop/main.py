import functions_framework
import requests
from requests.structures import CaseInsensitiveDict
from getToken import getToken

@functions_framework.http
def start_stop(request):
    com = 'start'
    vm = '????'
    project = '????'
    zone = 'us-central1-a'
    resp = request.get_json(silent=True)
    if not resp:
        resp = request.args
    if resp:
        if 'com' in resp:
            com = resp['com']
        if 'vm' in resp:
            vm = resp['vm']
        if 'project' in resp:
            project = resp['project']
        if 'zone' in resp:
            zone = resp['zone']

    token = getToken()

    url = ("https://compute.googleapis.com/compute/v1/projects/{}/zones/{}/instances/{}/{}?key=null"
           .format(project,zone,vm,com))
    print(url)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer {}".format(token)
    headers["Accept"] = "application/json"
    headers["Content-Length"] = "0"
    resp = requests.post(url, headers=headers)
    print(resp.status_code)

    return 'Start {}! ({})'.format(com,resp.status_code)