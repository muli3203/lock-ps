class User:
    """
    Class that generates new instances of credentials
        """
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

        """
        __init__ method help us define properties for the objects 
        
        Arguments:

        username: new username
        password: new password

        self variable represents the instance of the object it self
        """

    def save_user(self):
      """
      save_user method saves the user objects into user_list
      """  
      User.user_list.append(self)

    @classmethod
    def find_name(cls, name):
        """
        A method that takes in a name and returns a name that matches the username.

        Arguments:
        name: the name to search.
        Returns:
        the name of the person that fits the username.
        """
        for user in cls.user_list:
            if user.username == name:
                return user
    
    @classmethod
    def show_user(cls):
        """
        This is a method that returns the user_list
        """
        return cls.user_list

    @classmethod
    def user_exist(cls, name, password):
        """
        this is a method that checks if a user exists from the user_list
        """
        the_user = ""
        for user in User.user_list:
            if(user.username == name and user.password == password):
                the_user=user.username
                return the_user

