import unittest
import json
from app import app as ap

API_URLS = {
    'get_data_invalid': '/get/key_do_not_exists/',
    'get_data_valid': '/get/data/',
    'set_data': '/set',
    'search_data_via_key_valid' : '/search?prefix=data',
    'search_data_via_key_invalid' : '/search?prefix=key_do_not_exist',
    'search_data_via_value_valid' : '/search?suffix=value',
    'search_data_via_value_invalid' : '/search?suffix=value_do_not_exist'
}

class TestApplication(unittest.TestCase):
    def setUp(self):
        testor = ap.test_client(self)
        data = {'key':'data', 'value': 'value'}
        response = testor.post(API_URLS['set_data'],data=json.dumps(data), headers={'Content-Type': 'application/json'})
        return super().setUp()

    def test_get_data_not_exist(self):
        testor = ap.test_client(self)
        response = testor.get(API_URLS['get_data_invalid'], headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)
    
    def test_get_data_exist(self):
        testor = ap.test_client(self)
        response = testor.get(API_URLS['get_data_valid'], headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
    
    def test_search_data_key_valid(self):
        testor = ap.test_client(self)
        response = testor.get(API_URLS['search_data_via_key_valid'], headers={'Content-Type': 'application/json'})
        self.assertIsInstance(response.json.get('data'), list)
        self.assertEqual(response.status_code, 200)

    def test_search_data_value_valid(self):
        testor = ap.test_client(self)
        response = testor.get(API_URLS['search_data_via_value_valid'], headers={'Content-Type': 'application/json'})
        self.assertIsInstance(response.json.get('data'), list)
        self.assertEqual(response.status_code, 200)
    
    def test_search_data_value_invalid(self):
        testor = ap.test_client(self)
        response = testor.get(API_URLS['search_data_via_value_invalid'], headers={'Content-Type': 'application/json'})
        self.assertEqual(response.json.get('data'), [])
        self.assertEqual(response.status_code, 200)
    
    def test_search_data_key_invalid(self):
        testor = ap.test_client(self)
        response = testor.get(API_URLS['search_data_via_key_invalid'], headers={'Content-Type': 'application/json'})
        self.assertEqual(response.json.get('data'), [])
        self.assertEqual(response.status_code, 200)
    
    
        


if __name__ == "__main__":
    unittest.main()
