from app0 import app
from unittest import TestCase
import flask


# class TestSession_kimi(TestCase):
#     def setUp(self):
#         self.app = app.test_client()
#
#     def test_with_session(self):
#         with self.app as c:
#             with c.session_transaction() as sess:
#                 sess['mami'] = True
#             resp = c.get('/')
#         self.assertEqual(b'this is response', resp.data)


class TestSession_cesar(TestCase):
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
