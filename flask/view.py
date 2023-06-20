import sys
from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

def hook_root():
    print("webhook")
    sys.stdout.flush()
    if request.method == 'POST':
        return 'OK', 200
    else:
        return 'OK', 400

@app. route('/test')
def test():
    hook_root()

if __name__ == "__main__":
    port = os.environ.get('PORT', 5003)
    app.run(debug=True, host='0.0.0.0', port=port)
