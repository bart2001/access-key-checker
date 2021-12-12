import datetime
import json

def get_passed_hours(date1: datetime.datetime, date2: datetime.datetime) -> float:
    diff = date2 - date1
    diff_hours = diff.total_seconds() / 60 / 60
    return diff_hours

def check_positive_int(numstr: str) -> bool:
    if numstr.isdigit() and int(numstr) > 0:
        return True
    else:
        return False


def create_json_response(is_successful, result_code, result_msg, data):
    return json.dumps({
        "header": {
            "isSuccessful": is_successful,
            "resultMessage": result_msg,
            "resultCode": result_code,
        },
        "data": data
    })