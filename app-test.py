import unittest
import app
import requests

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.json(), {'hello': 'world'})


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')

if __name__ == "__main__":
    unittest.main()