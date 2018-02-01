import pyperclip
class Credentials:
    """
    Class that generates new instances of users.
    """
    credentials_list = []

    def __init__(self,email,password):
        self.email= email
        self.password= password

    def save_credentials(self):
        """
        save_user method saves credentials objects into credentials_list
        """
        Credentials.credentials_list.append(self)

    @classmethod
    def copy_email(cls,email):
        credentials_found = Credentials.find_by_email(email)
        pyperclip.copy(credentials_found.email)
