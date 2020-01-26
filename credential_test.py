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
        self.new_credential = Credential("Cheryl", "twitter", "cher1855")

    def __init__(self):
        """
        the init method checks if an object is initialized properly
        """
        
        self.new_credential.username, ("Cheryl")
        self.new_credential.password, ("cher1855")

    def tearDown(self):
        """
        a metod that cleans up after each testcase
        """
        Credential.credential_list = []

if __name__ == '__main__':
    unittest.main()