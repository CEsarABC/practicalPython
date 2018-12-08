import basic_test
from basic_test import app
from unittest import TestCase

class testingMyApp (TestCase):
    def test_results(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')

        self.assertEqual(response.status_code, 200)

    def test_rules(self):
        tester = app.test_client(self)
        response = tester.get('/rules', content_type='html/text')

        self.assertEqual(response.status_code, 200)


    def test_rules1(self):
        tester = app.test_client(self)
        response = tester.get('/rules', content_type='html/text')

        self.assertTrue(b'End game' in response.data)
