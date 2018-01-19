import unittest
from user import User

class TestUser(unittest.TestCase)
     '''
     Test class that defines test cases for the user class behaviours.

     Args: unittest.TestCase: TestCase class that helps in creatin test cases.
     '''

     def setUp(self):
         '''
         Setup method to run before each tests.
         '''
         self.new_user = User("Elaine","Nerea","elaine@n.com","0712345")

     def test_init(self):
         '''
         test_init test case to test if object is iniialized properly
         '''

         self.assertEqual(self.new_user.first_name,"Elaine")
         self.assertEqual(self.new_user.last_name,"Nerea")
         self.assertEqual(self.new_user.email,"elaine@n.com")
         self.assertEqual(self.new_user.password,"0712345")

if __name__ == '__main__':
