from flask import Flask, request
from main import start_stop
from listVM import listVM

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return start_stop(request)

@app.route('/list', methods=['GET', 'POST'])
def listvm():
    return listVM(request)

if __name__ == "__main__":
    import sys
    print('sys.path.__main=',sys.path)
    main_sys_path = sys.path
    app.run(debug=False, host='0.0.0.0', port=8080)