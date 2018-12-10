import Application_for_testing
from Application_for_testing import app
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

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/game', follow_redirects=True)
        self.assertIn(b'Testing Flask', response.data)

    ''' test cases involbing results page, NOT working
    status code results in 500 instead of 200, as is the page was not
    responding '''
    '''after testing I discovered that this taste cases don't working
    because the page depends on data inserted by the user '''

    def test_results(self):
        tester = app.test_client(self)
        response = tester.get('/results', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        #self.assertTrue(b'Testing Flask' in response.data)
    #
    # def test_results1(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/results', follow_redirects=True)
    #     self.assertIn(b'Testing Flask', response.data)
