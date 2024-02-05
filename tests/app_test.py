import unittest
from models.utils import endpoint, response

class TestApp(unittest.TestCase):

    def test_check_endpoint(self):

        self.assertEqual(type(endpoint), str)

    def test_check_response(self):

        self.assertEqual(type(response), dict)



if __name__ == "__main__":
    unittest.main()