import datetime
import math
import os
import boto3
from .. import utils, conf
import logging

DEFAULT_PAGE_SIZE = 100

logger = logging.getLogger(__name__)
logger = conf.set_log_config(logger)

class IAMclient:

    def __init__(self):
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', "")
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', "")
        self.client = boto3.client(
            'iam',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def get_all_usernames(self):
        usernames = []
        try:
            paginator = self.client.get_paginator('list_users')
            page_iterator = paginator.paginate(PaginationConfig={'PageSize': DEFAULT_PAGE_SIZE})
            for page in page_iterator:
                usernames.extend([user['UserName'] for user in page['Users']])
        except Exception as e:
            logger.error(str(e))
            return [], "Fail to get usernames"
        return usernames, ""

    def get_old_access_keys_by_usernames(self, usernames, hour):
        old_keys = []
        for username in usernames:
            try:
                paginator = self.client.get_paginator('list_access_keys')
                for page in paginator.paginate(UserName=username, PaginationConfig={'PageSize': DEFAULT_PAGE_SIZE}):
                    for user_key in page.get('AccessKeyMetadata', []):
                        create_date = user_key['CreateDate']
                        passed_hours = utils.get_passed_hours(create_date.replace(tzinfo=None),
                                                              datetime.datetime.utcnow().replace(tzinfo=None))
                        if passed_hours > hour:
                            old_keys.append({
                                'UserName': user_key['UserName'],
                                'AccessKeyId': user_key['AccessKeyId'],
                                'CreateDate': str(user_key['CreateDate']),
                                'PassedHours': math.ceil(passed_hours),
                            })
            except Exception as e:
                logger.error(str(e))
                return [], "Fail to get old access keys"
        return old_keys, ""