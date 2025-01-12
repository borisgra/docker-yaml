# !!! if need manage other project - add service account Cloud Run project to other projects (IAM& Admin/IAM - permission Editor)

from flask import Flask, request
from listVM import listVM
import os.path
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def listvm():
    return listVM(request,version)


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
