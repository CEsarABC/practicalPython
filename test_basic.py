import Application_for_testing
from Application_for_testing import app
from unittest import TestCase

class testingMyApp (TestCase):
    # def test_results(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/results', content_type='html/text')
    #
    #     self.assertEqual(response.status_code, 200)
        #self.assertTrue(b'Testing Flask' in response.data)

    def test_rules(self):
        tester = app.test_client(self)
        response = tester.get('/rules', content_type='html/text')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'GAME RULES' in response.data)

    def test_root(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')

        self.assertEqual(response.status_code, 200)
        #self.assertTrue(b'GAME RULES' in response.data)

    def test_game(self):
        tester = app.test_client(self)
        response = tester.get('/game', content_type='html/text')

        self.assertEqual(response.status_code, 200)
        #self.assertTrue(b'GAME RULES' in response.data)
