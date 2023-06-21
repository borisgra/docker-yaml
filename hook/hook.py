from flask import Flask, render_template, request
import os
import hashlib
import hmac

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/hook', methods=['GET', 'POST'])
def hook_root():
    # print("webhook headers:")
    # print(request.headers)
    # import sys
    # sys.stdout.flush()
    if request.method == 'POST':
        WEBHOOK_SECRET = "AAAAB3NzaC1yc2EAAAADAQABAAABAQCEHGBawN9"
        return verify_signature(request.data, WEBHOOK_SECRET, request.headers["X-Hub-Signature-256"])
    else:
        return 'ERROR', 400


def verify_signature(payload_body, secret_token, signature_header):
    """Verify that the payload was sent from GitHub by validating SHA256
    https://docs.github.com/en/webhooks-and-events/webhooks/securing-your-webhooks.
    Args:
        payload_body: original request body to verify (request.data)
        secret_token: GitHub app webhook token (WEBHOOK_SECRET)
        signature_header: header received from GitHub (x-hub-signature-256)
    """
    if not signature_header:
        return 403, "x-hub-signature-256 header is missing!"
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, signature_header):
        return 403, "Request signatures didn't match!"
    return "OK", 200


if __name__ == "__main__":
    port = os.getenv('PORT', 5003)
    isNotProduction = os.getenv("ORG_GRADLE_PROJECT_isProduction", "no") == "no"
    app.run(debug=isNotProduction, host='0.0.0.0', port=port)
