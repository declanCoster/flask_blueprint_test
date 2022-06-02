import unittest
import random
import string

from run import app

class FlaskTest(unittest.TestCase):

    def test_get_all(self):
        tester = app.test_client(self)
        response = tester.get('/all')
        self.assertEqual(response.status_code, 200)

    def test_get_city_pass(self):
        tester = app.test_client(self)
        response = tester.get('/city', json={
            "city":"Atlanta"
        })
        self.assertEqual(response.status_code, 200)

    def test_get_city_fail(self):
        tester = app.test_client(self)
        response = tester.get('/city', json={
            "city":"Portland"
        })
        self.assertEqual(response.status_code, 400)

    def test_update_fail(self):
        tester = app.test_client(self)
        response = tester.post('/update', json={
            "city":"Portland"
        })
        self.assertEqual(response.status_code, 400)

    def test_update_exists(self):
        tester = app.test_client(self)
        response = tester.post('/update', json={
            "city":"Boston",
            "temperature":65,
            "altitude": 27
        })
        self.assertEqual(response.status_code, 200)

    def test_update_new(self):
        tester = app.test_client(self)
        response = tester.post('/update', json={
            "city": ''.join(random.choice(string.ascii_lowercase) for i in range(10)) ,
            "temperature":65,
            "altitude": 27
        })
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()