from app0 import app
from unittest import TestCase
import flask


class TestSession_userName(TestCase):
    def setUp(self):
        self.app = app.test_client()

    ''' definition calling the test_client and joining the
    session_transaction to give content to the session,
    I give it a value then test the flask session in the application '''

    def test_with_session(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userName'] = 'cesar'
            rv = c.get('/')
            assert flask.session['userName'] == 'cesar'

class TestSession_score(TestCase):
    def setUp(self):
        self.app = app.test_client()

    ''' definition calling the test_client and joining the
    session_transaction to give content to the session,
    I give it a value then test the flask session in the application '''

    def test_with_session(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['score'] = 0
            rv = c.get('/')
            assert flask.session['score'] == 0

class TestSession_counter(TestCase):
    def setUp(self):
        self.app = app.test_client()

    ''' definition calling the test_client and joining the
    session_transaction to give content to the session,
    I give it a value then test the flask session in the application '''

    def test_with_session(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['counter'] = 0
            rv = c.get('/')
            assert flask.session['counter'] == 0

class TestSession_riddle(TestCase):
    def setUp(self):
        self.app = app.test_client()

    ''' definition calling the test_client and joining the
    session_transaction to give content to the session,
    I give it a value then test the flask session in the application '''

    def test_with_session(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['riddle'] = 'This is a ridddle'
            rv = c.get('/game')
            assert flask.session['riddle'] == 'This is a ridddle'
