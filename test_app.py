import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the DevOps Monitoring App!', response.data)

    def test_info(self):
        response = self.client.get('/info')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('hostname', data)
        self.assertIn('cpu_cores', data)

if __name__ == '__main__':
    unittest.main()