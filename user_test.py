import unittest

from user import User

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviours

    Arguments:
    unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run after each test case
        """
        self.new_user = User("Cheryl", "cher1855")
