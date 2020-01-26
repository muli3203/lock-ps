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

    def tearDown(self):
        """
        A tear down method that cleans up after each test case is run
        """
        User.user_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized property
        """
        self.assertEqual(self.new_user.username,"Cheryl")
        self.assertEqual(self.new_user.password,"cher1855")

    def test_save_user(self):
        """
        test_save_user testcase to test if the contact object is saved into the user_list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_name(self):
        """
        test to check if one can find a user by name and to display the information provided
        """
        self.new_user.save_user()
        found_user = User.find_name("Cheryl")

        self.assertEqual(found_user.username,self.new_user.username)


if __name__ == '__main__':
    unittest.main()