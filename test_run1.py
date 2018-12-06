import run4
from run4 import app
from unittest import TestCase

class testingMyApp (TestCase):
    def test_root(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_run_game(self):
        tester = app.test_client(self)
        response = tester.get('/game', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Testing Flask' in response.data)

    # def test_results(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/results', content_type='html/text')
    #     self.assertEqual(responce.status_code, 200)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/game', follow_redirects=True)
        self.assertIn(b'Testing Flask', response.data)

    def test_results(self):
        tester = app.test_client(self)
        response = tester.get('/results', follow_redirects=True)
        self.assertIn(b'Testing Flask Results', response.data)
