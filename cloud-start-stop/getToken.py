import requests


"""
    https://reqbin.com/code/python
    https://cloud.google.com/compute/docs/reference/rest/v1/instances/start?apix=true
    https://cloud.google.com/docs/authentication/rest#metadata-server
    https://cloud.google.com/compute/docs/metadata/querying-metadata#linux
     !!! add permission   Compute Instance Admin (v1)   in service account Cloud Run (Edit/Security)
    https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
    https://cloud.google.com/compute/docs/metadata/querying-metadata#linux
    https://gtseres.medium.com/using-service-accounts-across-projects-in-gcp-cf9473fef8f0
    !!! if need manage other project add service account Cloud Run project to other projects (IAM& Admin/IAM - permission Editor)
"""

def getToken():
    # url = "http://metadata.goog/computeMetadata/v1/instance/service-accounts/default/token"
    url = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
    payload = {}
    headers = {"Metadata-Flavor": "Google"}
    try:
        resp = requests.post(url, data=payload, headers=headers)
    except Exception as error:
        return "Error getToken: {} <br/> {}".format(type(error).__name__,error)
    if resp.status_code != 200:
        token = "Error getToken: status_code {}".format(resp.status_code)
    else:
        token = resp.json()['access_token']
    print(token)
    return token