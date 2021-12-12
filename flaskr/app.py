from flask import Flask, request, redirect, url_for
import logging, json
from . import conf, utils
from .models.iam import IAMclient
from .models.sender import SlackWebhookSender

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger = conf.set_log_config(logger)


@app.route("/")
def hello():
    logger.info("hello access-key-checker")
    return "<p>Hello, Access Key Checker!</p>"


@app.route('/check', methods=['GET'])
def check():
    hour = request.args.get('hour', 0)
    hour = utils.convert_to_positive_int(hour)
    if hour == 0:
        return utils.create_error_json_response("Invalid parameter: hour should be greater than 0")

    # create client
    client = None
    try:
        client = IAMclient()
    except Exception as e:
        logger.error(f"error={str(e)}")
        return utils.create_error_json_response("Invalid credential key")

    # get all usernames
    usernames, failmsg = client.get_all_usernames()
    if not usernames and failmsg:
        return utils.create_error_json_response(failmsg)

    # get all old keys by usernames and hour parameter
    old_keys, failmsg = client.get_old_access_keys_by_usernames(usernames, hour)
    if not old_keys and failmsg:
        return utils.create_error_json_response(failmsg)

    sender = SlackWebhookSender()
    sender.send_old_keys_webhook(hour, old_keys)

    return utils.create_success_json_response(old_keys)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('hello'))
