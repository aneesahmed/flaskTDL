# coding=utf-8
import unittest
import tdl_main
import requests
import json
import sys

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000/todos')
        self.assertEqual(response.json(), {'hello': 'world'})


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = tdl_main.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {'hello': 'world'}
        )


if __name__ == "__main__":
    tdl_main.main()