import functions_framework
import requests
from requests.structures import CaseInsensitiveDict

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

    """
        https://reqbin.com/code/python
        https://cloud.google.com/compute/docs/reference/rest/v1/instances/start?apix=true
        https://cloud.google.com/docs/authentication/rest#metadata-server
        https://cloud.google.com/compute/docs/metadata/querying-metadata#linux
         !!! add pemision   Compute Instance Admin (v1)   in service account Cloud Run (Edit/Security)
        https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
        https://cloud.google.com/compute/docs/metadata/querying-metadata#linux
    """

    # url = "http://metadata.goog/computeMetadata/v1/instance/service-accounts/default/token"
    url = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
    payload = { }
    headers = {"Metadata-Flavor": "Google"}
    resp = requests.post(url, data=payload, headers=headers)

    print(resp.status_code)
    token=resp.json()['access_token']
    print(token)

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