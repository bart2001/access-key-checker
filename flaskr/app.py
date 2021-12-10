from flask import Flask, request
import boto3
import datetime
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/check', methods=['GET'])
def check():
    old_standard = 20

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

    return str(send_list)

@app.route('/hour', methods=['GET'])
# https://velog.io/@devmin/python-flask-request-validator
def list():
    hour = request.args.get('hour', 0)
    #print(f'hour={hour}')
    return f'hour={hour}'

# @app.route('/list', methods=['GET'])
# def list():
#     client = boto3.client('iam')
#     response = client.list_users()
#     return str(response['Users'])
