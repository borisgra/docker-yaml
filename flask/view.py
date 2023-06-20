from flask import Flask, render_template, request, json
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app. route('/hooktest', methods=['GET', 'POST'])
def hook_root():
    if request.headers['Content-Types'] == 'application/json':  # calling json objects
        # print(json.dumps(request.json))
        return json.dumps(request.json)

@app. route('/test')
def test():
    hook_root()

if __name__ == "__main__":
    port = os.environ.get('PORT', 5003)
    app.run(debug=True, host='0.0.0.0', port=port)
