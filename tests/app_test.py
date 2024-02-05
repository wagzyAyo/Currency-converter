import unittest
from models.utils import endpoint, response

class App_test(unittest.TestCase):

    def check_endpoint(self):

        self.assertEqual(type(endpoint), str)

    def check_response(self):

        self.assertEqual(type(response), dict)



if __name__ == "__main__":
    unittest.main()