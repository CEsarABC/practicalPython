from app import app
import unittest
from unittest import TestCase
import flask

''' Testing pages response by code status
and follow_redirects '''

class TestRun(TestCase):
    def test_root(self):
        with app.test_client() as c:
            response = c.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            print('root: response, redirect')

class TestGame(TestCase):
    def test_run_game(self):
        with app.test_client() as c:
            response = c.get('/game', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            print('game: response, redirect')


class TestResults(TestCase):
    def test_results(self):
        tester = app.test_client(self)
        response = tester.get('/results', content_type='html/text')
        #print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'<title>Python Practical</title>' in response.data)
        print('results: response, assert in')


''' Testing sessions active in each section '''


class TestSessions_root(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            resp = c.get('/')
            #print(flask.session)
            self.assertEqual(flask.session['score'],0)
            self.assertEqual(flask.session['user'],'')
            self.assertEqual(flask.session['userInput'],'')
            print('root: session: score, user, userInput')


class TestSessions_run_game(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            resp = c.get('/game')
            #print(flask.session)
            self.assertEqual(flask.session['counter'],0)
            self.assertIn('riddle', flask.session)
            print("game: session['counter'], assertIn ridddle")
            
            
class TestSessions_results(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            resp = c.get('/results')
            print(flask.session)
            self.assertEqual(flask.session,{})
            print("results pass")





if __name__ == '__main__':
    unittest.main()
