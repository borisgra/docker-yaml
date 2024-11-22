import requests
from requests.structures import CaseInsensitiveDict

def run_command(com, project, token, vm, zone):
    url = ("https://compute.googleapis.com/compute/v1/projects/{}/zones/{}/instances/{}/{}"
           .format(project, zone, vm, com))
    print(url)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer {}".format(token)
    headers["Accept"] = "application/json"
    headers["Content-Length"] = "0"
    resp = requests.post(url, headers=headers)
    print(resp.status_code)
    return resp.status_code