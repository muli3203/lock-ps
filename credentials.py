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

    @classmethod
    def credential_exist(cls):pass

    def save_credential(self):
        """
        the save credential method saves the user objects into the credential list
        """
        Credential.credential_list.append(self)