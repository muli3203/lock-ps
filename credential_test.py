import unittest
from credentials import Credential
from user import User

class TestCredential(unittest.TestCase):
    """
    this is a test class that defines the test cases for a user class
    """
    def setUp(self):
        """
        A setUp method runs before each testcase
        """
        self.new_credentials = Credential("Cheryl", "twitter", "cher1855")