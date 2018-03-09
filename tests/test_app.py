import unittest

from run import app


class TestRoutes(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_home(self):
        # When
        resp = self.app.get('/')

        # Then
        assert b'Some stuff here!' in resp.data
