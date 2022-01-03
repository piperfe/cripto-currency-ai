import unittest
import buda_client


class TestApi(unittest.TestCase):

    def test_should_return_200(self):
        response = buda_client.make_get_ticker()

        self.assertEqual(200, response.status_code)
