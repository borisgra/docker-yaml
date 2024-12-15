# !!! if need manage other project - add service acсount Cloud Run project to other projects (IAM& Admin/IAM - pemision Editor)

from flask import Flask, request
from listVM import listVM

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def listvm():
    return listVM(request)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)