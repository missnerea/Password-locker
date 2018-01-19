class User:
    """
    Class that generates new instances of users.
    """
    user_list = []

    def __init__(self,first_name,last_name,email,password):
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.password= password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)
    @classmethod
    def user_exists(cls,email):
        '''
        Method that checks if a user exists from the user list.
        Args:
            email: email to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.email == email:
                return True
        return False
