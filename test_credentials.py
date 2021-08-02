import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours
    '''

    def setUp(self):
        # self.new_credentials = Password("Twitter, "John","James", "jj0897") #Create user credential object
        
        
        self.new_credentials = Credentials("Twitter","John","James","johnjames11")
        


    def tearDown(self):
        '''
        Tear down method that does clean up after each test case has run
        '''
        Credentials.credentials_list = []
        

    def test__init(self):
        '''
        Test to check whether the credentials objects are instantiated correctly
        '''
        self.assertEqual(self.new_credentials.account_name,"Twitter")
        self.assertEqual(self.new_credentials.first_name,"John")
        self.assertEqual(self.new_credentials.last_name,"James")
        self.assertEqual(self.new_credentials.user_password,"johnjames11")

    def test_save_credential(self):
        '''
        Test to check if the object is saved into the credentials list
        '''
        self.new_credentials.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credential()
        test_credentials = Credentials("Facebook", "John", "James", "johnjames11")
        test_credentials.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)


    def test_delete_credential(self):
        '''
        Test Case to check whether we can delete credentials from our credentials list
        '''
        self.new_credentials.save_credential()
        test_credentials = Credentials("Facebook", "John", "James", "johnjames11")
        test_credentials.save_credential()

        self.new_credentials.delete_credential() #deleting an object
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials(self):
        '''
        Test case to check whether we can find credentials using site name
        '''
        self.new_credentials.save_credential()
        test_credentials = Credentials("Facebook", "John", "James", "johnjames11")
        test_credentials.save_credential()

        found_credentials = Credentials.find_by_account_name("Facebook")
        self.assertEqual(found_credentials.account_name, test_credentials.account_name)

    def test_credentials_exist(self):
        '''
        Test whether the credentials object actually exists
        '''
        self.new_credentials.save_credential()
        test_credentials = Credentials("Twitter", "John", "James", "johnjames11")
        test_credentials.save_credential()

        credentials_exists = Credentials.credential_exist("twitter")
        self.assertTrue(credentials_exists)

    def test_display_credentials(self):
        '''
        Test method that returns a list of all credentials
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)





if __name__ == '__main__':
    unittest.main()