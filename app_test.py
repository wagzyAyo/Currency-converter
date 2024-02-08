import unittest
from decimal import Decimal
from models.utils import endpoint, response, convert, unit_per

class TestApp(unittest.TestCase):

    def test_check_endpoint(self):
        """Check APi endpoint"""
        self.assertEqual(type(endpoint), str)

    def test_check_response(self):
        """Check the data received from db"""
        self.assertEqual(type(response), dict)
        self.assertFalse(isinstance(response, str))

    def test_convert1(self):
        """test convert function"""
        self.assertTrue(isinstance(convert('USD', 'NGN', 100), Decimal))

    def test_convert2(self):
        """Test convert function 2"""
        self.assertFalse(isinstance(convert('USD', 'NGN', 100), str))

    def test_unit_per(self):
        """Test unit_per function"""
        self.assertTrue(isinstance(unit_per('USD', 'NGN', 100, 119800), str))
        self.assertEqual(unit_per('USD', 'NGN', 100, 119800), "1USD = 1198.0NGN")
        self.assertFalse(isinstance(unit_per('USD', 'NGN', 100, 119800), int))

    def test_invalid_currency(self):
        """Test convert function with invalid currency"""
        with self.assertRaises(ValueError):
            convert('INVALID', 'NGN', 100)

    def test_negative_amount(self):
        """Test convert function with negative amount"""
        with self.assertRaises(ValueError):
            convert('USD', 'NGN', -100)


if __name__ == "__main__":
    unittest.main()