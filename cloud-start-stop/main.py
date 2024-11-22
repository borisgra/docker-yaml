import functions_framework
from getToken import getToken
from run_command import run_command
from get_param import get_param

@functions_framework.http
def start_stop(request):
    com, project, vm, zone = get_param(request)

    token = getToken()
    resp = run_command(com, project, token, vm, zone)

    return 'Start {}! ({})'.format(com,resp.status_code)
