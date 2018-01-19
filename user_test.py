import unittest
from user import User

class TestUser(unittest.TestCase):
     '''
     Test class that defines test cases for the user class behaviours.

     Args: unittest.TestCase: TestCase class that helps in creatin test cases.
     '''

     def setUp(self):
         '''
         Setup method to run before each tests.
         '''
         self.new_user = User("Elaine","Nerea","elaine@n.com","0712345")

     def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

     def test_init(self):
         '''
         test_init test case to test if object is iniialized properly
         '''

         self.assertEqual(self.new_user.first_name,"Elaine")
         self.assertEqual(self.new_user.last_name,"Nerea")
         self.assertEqual(self.new_user.email,"elaine@n.com")
         self.assertEqual(self.new_user.password,"0712345")


     def test_save_user(self):
         '''
         test_save_user test case to test if the user object is saved into the user list.
         '''
         self.new_user.save_user()
         self.assertEqual(len(User.user_list),1)

     def test_save_multipe_user(self):
        '''
        Test save_multiple_user to check if we can save multiple user objects to our user list.
        '''
        self.new_user.save_user()
        test_user = User("Test","user","test@user.com","0712345")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

     

if __name__ == '__main__':
    unittest.main()
