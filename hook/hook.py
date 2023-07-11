import socket

from flask import Flask, render_template, request
import os
import hashlib
import hmac
from dotenv import load_dotenv
import datetime
import sys

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ssh', methods=['GET', 'POST'])
def test_ssh():
    print("cmd_test={}".format(cmd_test))
    sys.stdout.flush()
    ssh(cmd_test)
    return 'TEST SSH', 401


@app.route('/test', methods=['GET', 'POST'])
def test():
    with open("static/history.html", "a") as text_file:
        print("<div>HOOK-T : {} CMD_TEST={} </div>".format(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                                                           cmd_test), file=text_file)
    os.system(cmd_test)
    return 'TEST', 401

@app.route('/hook', methods=['GET', 'POST'])
def hook_root():
    # print("webhook headers:")
    # print(request.headers)
    # import sys
    # sys.stdout.flush()
    if request.method == 'POST':
        webhook_secret = os.getenv("WEBHOOK_SECRET", "no")
        return verify_signature(request.data, webhook_secret, request.headers["X-Hub-Signature-256"])
    else:
        run_command_os("echo ' echo  \" ERROR 400 : Method not POST !!! \" ' > myHostPipe")
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
        return "x-hub-signature-256 header is missing!", 403
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, signature_header):
        return "Request signatures didn't match!", 403
    return run_command_os(os.getenv("CMD", "ls -a "))


def run_command_os(cmd):
    try:
        os.system(cmd)
        with open("static/history.html", "a") as text_file:
            print("<div>HOOK   : {} CMD={} </div>".format(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"),cmd), file=text_file)
    except Exception as error:
        with open("static/history.html", "a") as text_file:
            print("<div>HOOK : {} \n Error: {} </div>".format(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                                                              error), file=text_file)
        return "Error in CMD {}".format(error), 402
    return "OK", 200


import paramiko

def ssh(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        k = paramiko.RSAKey.from_private_key_file(OPENSSH_KEY_FILENAME)
        if (OPENSSH_KEY_FILENAME == ""):
            ssh.connect(HOST_SSH, PORT_SSH, username=USERNAME_SSH, password=PASS_SSH)
        else:
            ssh.connect(HOST_SSH, PORT_SSH, username=USERNAME_SSH, pkey=k) # sshkey.pub
            # ssh.connect(HOST_SSH, PORT_SSH, username=USERNAME_SSH, key_filename=OPENSSH_KEY_FILENAME) # openssh key

        stdin, stdout, stderr = ssh.exec_command(command)
    except socket.error:
        raise ValueError('Unable to connect to {}:{}'.format(HOST_SSH,PORT_SSH))
    except paramiko.BadAuthenticationType:
        raise ValueError('Bad authentication type.')
    except paramiko.AuthenticationException:
        raise ValueError('Authentication failed.')
    except paramiko.BadHostKeyException:
        raise ValueError('Bad host key.')
    # except paramiko.ssh_exception.SSHException:
    #     raise ValueError('The host key given by the SSH server did not match what we were expecting {}'.format(OPENSSH_KEY_FILENAME))

    lines = stdout.readlines()
    print(lines)
    sys.stdout.flush()

if __name__ == "__main__":
    load_dotenv(".env")
    port = os.getenv('HOOK_PORT', 5003)
    HOST_SSH = os.getenv("HOST_SSH", "172.17.0.1") # https://stackoverflow.com/questions/22944631/how-to-get-the-ip-address-of-the-docker-host-from-inside-a-docker-container
    PORT_SSH = int(os.getenv("PORT_SSH", "22"))
    USERNAME_SSH=os.getenv("USERNAME_SSH", "boris")
    PASS_SSH=os.getenv("PASS_SSH", "123")
    OPENSSH_KEY_FILENAME=os.getenv("OPENSSH_KEY_FILENAME", "")

    cmd_test = os.getenv("CMD_TEST", "ls -a ")
    print ("HOST_SSH={}, PORT_SSH={} ".format(HOST_SSH,PORT_SSH,))
    sys.stdout.flush()
    isProduction = os.getenv("isProduction", "no") == "yes"
    # ssh("ls ")
    app.run(debug=not isProduction, host='0.0.0.0', port=port)
