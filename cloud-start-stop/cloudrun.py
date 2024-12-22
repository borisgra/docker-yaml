# !!! if need manage other project - add service account Cloud Run project to other projects (IAM& Admin/IAM - permission Editor)

from flask import Flask, request
from listVM import listVM

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def listvm():
    print('ver=',ver)
    return listVM(request,ver)

if __name__ == "__main__":
    f = open("../ver", "r")
    ver = f.read()
    app.run(debug=False, host='0.0.0.0', port=8080)