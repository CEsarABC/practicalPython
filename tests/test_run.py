# import sys
# sys.path.insert(0, '..')
from unittest import TestCase
from run4 import app

class TestRun(TestCase):
    def test_root(self):
        with app.test_client() as c:
            response = c.get('/')

            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
