import datetime
import json

def get_passed_hours(date1: datetime.datetime, date2: datetime.datetime) -> float:
    diff = date2 - date1
    diff_hours = diff.total_seconds() / 60 / 60
    return diff_hours

def convert_to_positive_int(numstr: str) -> int:
    try:
        number = int(numstr)
        return number if number > 0 else 0
    except ValueError:
        return 0

def create_success_json_response(data):
    return json.dumps({
        "header": {
            "isSuccessful": True,
            "resultMessage": "Success"
        },
        "data":  data
    })

def create_error_json_response(message):
    return json.dumps({
        "header": {
            "isSuccessful": False,
            "resultMessage": message
        }
    })