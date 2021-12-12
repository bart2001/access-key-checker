import datetime
from flaskr import utils

# time gap should be greater or equal to 24
def test_passed_24hours():
    now = datetime.datetime.utcnow().replace(tzinfo=None)
    past = (now - datetime.timedelta(hours=24)).replace(tzinfo=None)
    passed_hours = utils.get_passed_hours(past, now)
    assert passed_hours >= 24

# time gap should be greater or equal to 1.5
def test_passed_90min():
    now = datetime.datetime.utcnow().replace(tzinfo=None)
    past = (now - datetime.timedelta(hours=1, minutes=30)).replace(tzinfo=None)
    passed_hours = utils.get_passed_hours(past, now)
    assert passed_hours >= 1.5

# check string is positive int
def test_check_positive_int():
    assert not utils.check_positive_int("0")
    assert not utils.check_positive_int("-1")
    assert not utils.check_positive_int("integer")
    assert not utils.check_positive_int("2.1")
    assert utils.check_positive_int("1")
