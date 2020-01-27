class Credential:
    """
    this is a class that generates new credentials
    """
    credential_list = []

    def __init__(self, username, password, appname):
        
        """
        __init__ method help us define properties for the objects 
        """
        self.username = username
        self.password = password
        self.appname = appname

    def save_credential(self):
        """
        the save credential method saves the user objects into the credential list
        """
        Credential.credential_list.append(self)

    @classmethod
    def display_credential(cls, user):
        """
        the display credentials method is to show the likst of the credentials saved
        """
        users_credential_list = []
        for credential in cls.credential_list:
            if credential.username == user:
                users_credential_list.append(credential)
                return users_credential_list

