import unittest
from decimal import Decimal
from models.utils import endpoint, response, convert

class TestApp(unittest.TestCase):

    def test_check_endpoint(self):

        self.assertEqual(type(endpoint), str)

    def test_check_response(self):

        self.assertEqual(type(response), dict)

    def test_convert1(self):
        """test convert function"""
        self.assertTrue(isinstance(convert('USD', 'NGN', 100), Decimal))
        self.assertEqual(convert(1.080672, 1290.866361, 100), "Invalid conversion")



if __name__ == "__main__":
    unittest.main()