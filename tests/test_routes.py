import unittest
from app import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode(), 'Deploying Flask App')

    def test_hello_route(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode(), 'Hello from GET request')
    def test_hello_route(self):
        response = self.client.get('/hello1post')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode(), 'Hello from another GET request')

if __name__ == '__main__':
    unittest.main()