from app import app
from unittest import TestCase
import flask

''' Tessting pages response by code status
and follow_redirects '''

class TestRun(TestCase):
    def test_root(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)

            response = c.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

class TestGame(TestCase):
    def test_run_game(self):
        with app.test_client() as c:
            response = c.get('/game')
            self.assertEqual(response.status_code, 200)

            response = c.get('/game', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

class TestRules(TestCase):
    def test_rules(self):
        tester = app.test_client(self)
        response = tester.get('/rules', content_type='html/text')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'GAME RULES' in response.data)


''' Testing sessions in the main application
by taking the session from the main application and
giving it value in otder to test it, I have created a copy of
the main application (app.py) with new lines of code in order to test responses '''

class TestSession_userinput(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_session_userInput(self):
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
        self.assertEqual(b'session not active', resp.data)

class TestSession_score(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess['score'] = True
            resp = c.get('/game')
        self.assertEqual(b'session not active', resp.data)

class TestSession_kimi(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess['kimi'] = False
            resp = c.get('/game')
        self.assertEqual(b'session not active', resp.data)
