# import sys
# sys.path.insert(0, '..')
from unittest import TestCase
from run4 import app

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

class TestGame(TestCase):
    def test_results(self):
        with app.test_client() as c:
            response = c.get('/results')
            self.assertEqual(response.status_code, 200)

            responce = c.get('/results', follow_redirects=True)
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
