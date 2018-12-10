from app import app
from unittest import TestCase
import flask


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

'''Testing sessions in the main application'''

class TestSession_userinput(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess['userInput'] = True
            resp = c.get('/game')
        self.assertEqual(b'session is active', resp.data)

class TestSession_riddle(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess['riddle'] = True
            resp = c.get('/game')
        self.assertEqual(b'session is active', resp.data)
