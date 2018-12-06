from run4 import app
from unittest import TestCase


class TestRun(TestCase):
    def test_root(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)

            responce = c.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

class TestGame(TestCase):
    def test_run_game(self):
        with app.test_client() as c:
            response = c.get('/game')
            self.assertEqual(response.status_code, 200)

            responce = c.get('/game', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

''' TestResults case fails response code 500 Internal Server Error,
instead of 200 OK'''
''' Traceback (most recent call last):
  File "C:\Users\zeroa\PycharmProjects\practicalPython\test_run.py", line 28, in test_results
    self.assertEqual(response.status_code, 200)
AssertionError: 500 != 200 '''

class TestResults(TestCase):
    def test_results(self):
        with app.test_client() as c:
            response = c.get('/results')
            self.assertEqual(response.status_code, 200)

            responce = c.get('/results', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
