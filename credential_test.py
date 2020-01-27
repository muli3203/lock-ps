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
        self.new_credential = Credential("Cheryl", "twitter", 
        "cher1855")

    def test_init_(self):
        """
        the init method checks if an object is initialized properly
        """
        self.new_credential.username, ("Cheryl")
        self.new_credential.password, ("cher1855")
        self.new_credential.appname, ("twitter")


    def tearDown(self):
        """
        a metod that cleans up after each testcase
        """
        Credential.credential_list = []

    def test_display_credential(self):
        """
        a test case to test the display of credentials 
        """

        self.new_credential.save_credential()
        twitter = Credential("Cheryl", "twitter", "cher1855")
        twitter.save_credential()
        self.assertEqual(len(Credential.display_credential(twitter.username)),1)


if __name__ == '__main__':
    unittest.main()