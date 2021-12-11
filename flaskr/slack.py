import boto3
import datetime
from slack_sdk import WebClient, WebhookClient

url = ""

def send_simple_webhook():
    webhook = WebhookClient(url)
    response = webhook.send(text="Hello! I am byungwoo")
    assert response.status_code == 200
    assert response.body == "ok"
    print("hello slack")

def send_block_webhook():
    webhook = WebhookClient(url)
    response = webhook.send(
        #미리보기
        text="access-key-checker",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
                }
            }
        ]
    )
    assert response.status_code == 200
    assert response.body == "ok"


if __name__ == '__main__':
   send_block_webhook()