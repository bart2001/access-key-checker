import pytest

from flaskr.models.iam import IAMclient
from flaskr.models.sender import SlackWebhookSender

# wrong credential should return empty usernames list
def test_iam_get_usernames_with_wrong_credential(monkeypatch):
    monkeypatch.setenv('AWS_ACCESS_KEY_ID', 'wrong_id')
    monkeypatch.setenv('AWS_SECRET_ACCESS_KEY', 'wrong_key')
    client = IAMclient()
    usernames, failmsg = client.get_all_usernames()
    assert len(usernames) == 0
    assert failmsg

# wrong usernames should return fail message
def test_iam_get_old_access_keys_with_wrong_usernames():
    sample_hour = 1000
    real_and_fake_users = ["chloe.kim", "unknown1"]
    client = IAMclient()
    keys, failmsg = client.get_old_access_keys_by_usernames(real_and_fake_users, sample_hour)
    assert failmsg

# wrong slack webhook url should return fail message
def test_sender_with_wrong_slack_webhook_url(monkeypatch):
    monkeypatch.setenv('SLACK_WEBHOOK_URL', 'https://hooks.slack.com/services/fake')
    sender = SlackWebhookSender()
    failmsg = sender.send_old_keys_webhook(0, [])
    assert failmsg

