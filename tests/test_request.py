import unittest
import json
from flaskr.app import app

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # should success
    def test_hello(self):
        response = self.app.get('/')
        data = json.loads(response.data)
        assert data['header']['resultCode'] == 0

    # should fail because hour is not positive int
    def test_check_with_zero_hour(self):
        response = self.app.get('/check?hour=0')
        data = json.loads(response.data)
        assert data['header']['resultCode'] != 0

    def test_check_with_positive_int_hour(self):
        hour = 60
        response = self.app.get(f'/check?hour={hour}')
        data = json.loads(response.data)
        assert data['header']['resultCode'] == 0

    def test_check_with_no_old_keys(self):
        # too long hour
        hour = 10000000000000000000000
        response = self.app.get(f'/check?hour={hour}')
        data = json.loads(response.data)
        assert data['header']['resultCode'] == 0
        assert len(data['data']) == 0
