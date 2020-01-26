class User:
    """
    Class that generates new instances of credentials
        """


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