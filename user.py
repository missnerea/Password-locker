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
    def find_by_email(cls,email):
        """
         Method that takes in the email and returns a user that matches that email
        """
        for user in cls.user_list:
            if user.email == email:
                return user 
