import boto3
import datetime
import math

def main():
    old_standard = 20

    # Create IAM client
    client = boto3.client('iam')
    user_response = client.list_users()
    users = [a['UserName'] for a in user_response.get('Users', [])]

    utcnow = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)

    for user in users:
        key_response = client.list_access_keys(UserName=user)
        for key in key_response.get('AccessKeyMetadata', []):
            print('----------------')
            key_create_date = key['CreateDate'].replace(tzinfo=datetime.timezone.utc)
            diff = utcnow - key_create_date
            diff_hours = diff.total_seconds() / 60 / 60
            is_old = True if diff_hours > old_standard else False
            print(user, key['AccessKeyId'], key_create_date, diff_hours, is_old)

    # List access keys through the pagination interface.
    # paginator = iam.get_paginator('list_access_keys')
    # for response in paginator.paginate(UserName='chloe.kim'):
    #     print(response)

    #utcnow = datetime.datetime.now().replace(tzinfo=None)
    #utcnow = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    # ago = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc) - datetime.timedelta(hours=1, minutes=30)
    # print(utcnow)
    # diff = (utcnow - ago)
    # hours = diff.total_seconds() / 60 / 60
    # print(hours)

    # {'Path': '/', 'UserName': 'youngwoo.kim', 'UserId': 'AIDAQWOA54DN2XTBSUWTL', 'Arn': 'arn:aws:iam::048186122459:user/youngwoo.kim', 'CreateDate': datetime.datetime(2021, 6, 15, 0, 35, 26, tzinfo=tzutc())}

    # for user in response['Users']:
    #     create_date = user['CreateDate'].replace(tzinfo=datetime.timezone.utc)
    #     diff = utcnow - create_date
    #     diff_hours = diff.total_seconds() / 60 / 60
    #     diff_days = diff.total_seconds() / 60 / 60 / 24
        #print(user["UserName"], utcnow, create_date, diff.days, diff_days, diff_hours)
        #print(type(creation_date), type(now))
        #print(f"now={now}, creation_date={creation_date}")

    # IAM_RESOURCE = boto3.resource('iam')
    # users = IAM_RESOURCE.users.filter(
    #     PathPrefix='/'
    # )
    # print('IAM users search results:')
    # for user in users:
    #     print(f'  - {user.}')

    # iam = boto3.resource('iam')
    # user_iterator = iam.users.filter(
    #
    # )
    # for user in user_iterator:
    #     print(user)

    # paginator = iam.get_paginator('list_users')
    # for response in paginator.paginate():
    #     for user in response["Users"]:
    #         print(f"Username: {user['UserName']}, Arn: {user['Arn']}")

if __name__ == '__main__':
   main()