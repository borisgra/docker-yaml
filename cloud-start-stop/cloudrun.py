# !!! if need manage other project - add service account Cloud Run project to other projects (IAM& Admin/IAM - permission Editor)
from flask_cors import CORS
from flask import Flask, request

from listVM import listVM
import os.path
from datetime import datetime
import requests

app = Flask(__name__)
# https://sky.pro/wiki/python/razreshenie-cors-vo-flask-dlya-zaprosov-cherez-j-query/
# http://localhost:8080/static/menus/menu-load.js
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def listvm():
    return listVM(request,version)

@app.route('/load', methods=['GET', 'POST'])
def load():
    return load_and_save()


def load_and_save():
    print('load')
    name = 'test.js'
    url = ''  # https://storage.googleapis.com/public-gra/menus/menu-gra.js
    # http://127.0.0.1:8080/load?url=https://storage.googleapis.com/public-gra/menus/menu-gra.js
    resp = request.get_json(silent=True)
    if not resp:
        resp = request.args
    if resp:
        if 'url' in resp:
            url = resp['url']
        if 'name' in resp:
            name = resp['name']
    print(url)
    z = requests.get(url)
    if (z.status_code == 200):
        # print(z.text)
        with open('static/menus/' + name, 'w') as f:
            f.write(z.text)
    return 'Code=' + str(z.status_code)


def get_version():
    global version
    fname = '../ver'
    if not os.path.isfile(fname):
        f = open(fname, "w")
        f.write('?\n?????\n{}\n'.format(str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))))
    f = open(fname, "r")
    ver = f.read()
    a, b, c, _ = ver.split('\n')
    version = ('version:1.0.{} {} compile {} started {}'
               .format(a, b, c, str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))))
    print('version=', version)


if __name__ == "__main__":
    get_version()
    app.run(debug=False, host='0.0.0.0', port=8080)
