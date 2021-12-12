import os
from slack_sdk import WebhookClient
from .. import conf
import logging

logger = logging.getLogger(__name__)
logger = conf.set_log_config(logger)

class SlackWebhookSender:

    def __init__(self):
        slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL', "")
        self.client = WebhookClient(slack_webhook_url)

    def send_old_keys_webhook(self, passed_hours, old_keys):
        message = f"These keys has passed {str(passed_hours)} hours since creation\n"
        message += '\n'.join([str(k) for k in old_keys])
        try:
            response = self.client.send(
                 text=message,
            )
            logger.info(f"slack webhook response={str(response)}")
            assert response.status_code == 200
            assert response.body == "ok"
        except Exception as e:
            logger.error(f"slack send webhook error={str(e)}")
        return "Sending webhook message failed"