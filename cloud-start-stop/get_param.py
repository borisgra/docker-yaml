def get_param(request):
    com = ''
    vm = ''
    projects = ''
    zone = 'us-central1-a'
    resp = request.get_json(silent=True)
    if not resp:
        resp = request.args
    if resp:
        if 'com' in resp:
            com = resp['com']
        if 'vm' in resp:
            vm = resp['vm']
        if 'projects' in resp:
            projects = resp['projects']
        if 'zone' in resp:
            zone = resp['zone']
    return com, projects, vm, zone