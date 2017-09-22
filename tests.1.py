# tests.py
import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from app import app


class MyTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        client = app.test_client()
        return app

class TestViews(MyTest):
    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        with app.test_client() as c:
            response = c.get('/login')
            self.assertEquals(response.status_code, 200)

    def test_register_view(self):
        """
        Test that login page is accessible without login
        """
        with app.test_client() as c:
            response = c.get('/register')
            self.assertEquals(response.status_code, 200)


    def test_dashboard_view(self):
        """
        Test that login page is accessible without login
        """
        with app.test_client() as c:
            response = c.get('/')
            self.assertEquals(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()