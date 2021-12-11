from flask import Flask, request
import boto3
import datetime
from slack_sdk.webhook import WebhookClient
from tabulate import tabulate

app = Flask(__name__)
webhook_url = ""

def send_incoming_webhook(message):
    webhook = WebhookClient(webhook_url)
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

@app.route('/check', methods=['GET'])
def check():
    #old_standard = int(request.args.get('hour', 0))
    old_standard = 4200

    # Create IAM client
    client = boto3.client('iam')
    user_response = client.list_users()
    users = [a['UserName'] for a in user_response.get('Users', [])]
    utcnow = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)

    send_list = []
    for user in users:
        key_response = client.list_access_keys(UserName=user)
        for key in key_response.get('AccessKeyMetadata', []):
            print('----------------')
            key_create_date = key['CreateDate'].replace(tzinfo=datetime.timezone.utc)
            diff = utcnow - key_create_date
            diff_hours = diff.total_seconds() / 60 / 60
            is_old = True if diff_hours > old_standard else False
            print(user, key['AccessKeyId'], key_create_date, diff_hours, is_old)
            send_list.append([user, key['AccessKeyId'], key_create_date, diff_hours, is_old]) if is_old else None

    return tabulate(send_list, tablefmt='html')

@app.route('/hour', methods=['GET'])
# https://velog.io/@devmin/python-flask-request-validator
def list():
    hour = request.args.get('hour', 0)
    return f'hour={hour}'