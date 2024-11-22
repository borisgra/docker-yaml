import functions_framework
from getToken import getToken
from run_command import run_command

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
    resp = run_command(com, project, resp, token, vm, zone)

    return 'Start {}! ({})'.format(com,resp.status_code)