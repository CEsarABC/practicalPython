from app import app
import unittest
from unittest import TestCase
import flask

''' Testing pages response by code status
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

# '''unknown issue testing results page  '''

class TestResults(TestCase):
    def test_game_results(self):
        with app.test_client() as c:
            response = c.get('/results')
            self.assertEqual(response.status_code, 200)

            response = c.get('/results', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

# # class TestResults(TestCase):
# #     def test_results(self):
# #         tester = app.test_client(self)
# #         response = tester.get('/results', content_type='html/text')

# #         self.assertEqual(response.status_code, 200)
# #         self.assertTrue(b'Leaderboard' in response.data)


class TestSessions_root(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess['userName'] = True
            resp = c.get('/')
            print(flask.session)
            self.assertEqual(flask.session['score'],0)
            self.assertEqual(flask.session['user'],'')
            self.assertEqual(flask.session['userInput'],'')


class TestSessions_run_game(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess['userName'] = True
            resp = c.get('/game')
            print(flask.session)
            self.assertEqual(flask.session['counter'],0)
            self.assertIn('riddle', flask.session)
            self.assertTrue(flask.session['userName'])
            
            
class TestSessions_results(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_with_session(self):
        with self.app as c:
            with c.session_transaction() as sess:
                sess['userName'] = True
            resp = c.get('/results')
            print(flask.session)
            # self.assertEqual(flask.session['counter'],0)
            # self.assertIn('riddle', flask.session)
            # self.assertTrue(flask.session['userName'])





if __name__ == '__main__':
    unittest.main()
