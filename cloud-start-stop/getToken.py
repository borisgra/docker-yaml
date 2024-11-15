import requests


"""
    https://reqbin.com/code/python
    https://cloud.google.com/compute/docs/reference/rest/v1/instances/start?apix=true
    https://cloud.google.com/docs/authentication/rest#metadata-server
    https://cloud.google.com/compute/docs/metadata/querying-metadata#linux
     !!! add pemision   Compute Instance Admin (v1)   in service account Cloud Run (Edit/Security)
    https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
    https://cloud.google.com/compute/docs/metadata/querying-metadata#linux
"""

def getToken():
    # url = "http://metadata.goog/computeMetadata/v1/instance/service-accounts/default/token"
    url = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
    payload = {}
    headers = {"Metadata-Flavor": "Google"}
    resp = requests.post(url, data=payload, headers=headers)
    print(resp.status_code)
    token = resp.json()['access_token']
    print(token)
    return token