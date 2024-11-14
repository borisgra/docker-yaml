from flask import Flask, request
from main import start_stop

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return start_stop(request)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)