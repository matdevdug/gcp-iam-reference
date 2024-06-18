import unittest
from flask import Flask, render_template_string
from main import app

class TestIndexPage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page_text(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        expected_text = "No Rights Reserved Go Nuts"
        actual_html = response.get_data(as_text=True)
        self.assertIn(expected_text, actual_html)

    def test_all_roles_route_text(self):
        response = self.app.get('/all-roles')
        self.assertEqual(response.status_code, 200)
        expected_text = "roles/artifactregistry.createOnPushWriter"
        actual_html = response.get_data(as_text=True)
        self.assertIn(expected_text, actual_html)

        def test_search_route_text(self):
        response = self.app.get('/search')
        self.assertEqual(response.status_code, 200)
        expected_text = "aiplatform"
        actual_html = response.get_data(as_text=True)
        self.assertIn(expected_text, actual_html)

if __name__ == '__main__':
    unittest.main()
