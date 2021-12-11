import datetime
import os
import boto3
from ..utils import utils
# class for iam client

class IAM:
    def __init__(self):
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', "")
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', "")
        print(aws_access_key_id, aws_secret_access_key)
        self.client = boto3.client('iam')

    def get_all_users(self):
        response = self.client.list_users()
        usernames = [a['UserName'] for a in response.get('Users', [])]
        return usernames

    def get_access_keys_by_user(self, username):
        response = self.client.list_access_keys(UserName=username)
        keys = response.get('AccessKeyMetadata', [])
        return keys

    def get_old_access_keys_by_user(self, username, old_standard):
        old_keys = []
        utcnow = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
        response = self.client.list_access_keys(UserName=username)
        keys = response.get('AccessKeyMetadata', [])
        for key in keys:
            key_create_date = key['CreateDate'].replace(tzinfo=datetime.timezone.utc)
            diff_hours = utils.get_diff_hours(key_create_date, utcnow)
            key['DiffHours'] = diff_hours
            if diff_hours > old_standard:
                old_keys.append(key)
        return keys

    def get_old_access_keys_by_users(self, usernames, old_standard):
        all_old_keys = []
        for username in usernames:
            old_keys = self.get_access_keys_by_user(username, old_standard)

# python -m flaskr.models.iam
if __name__ == '__main__':
    iam = IAM()
    first_user = iam.get_all_users()[0]
    client = boto3.client('iam')
    #print(iam.get_all_users())
    #old_keys = iam.get_old_access_keys_by_user('jonny.koo', 0)
    #print(old_keys)

