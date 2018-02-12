#!/usr/bin/env python3.6

import random
from user import User
from credential import Credential

def create_user(first_name,last_name,email,password):
    '''
    Function to create a new contact
    '''
    new_user = User(first_name,last_name,email,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user(email):
    '''
    Function that finds a user by email and returns the email
    '''
    return User.find_by_email(email)

def check_existing_users(email):
    '''
    Function that check if a user exists with that email and return a Boolean
    '''
    return User.user_exist(email)

def user_log_in(first_name, password):
    '''
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(first_name, password)
    if log_in != False:
        return User.log_in(first_name, password)


def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def create_credentail(user_password, name, password):
    '''
    Function to create a credential
    Args:
        user_password : the password for Password Locker
        name : the name of the account
        password : the password for the account
    '''

    new_credentail = Credential(user_password,name,password)

    return new_credentail

def save_credentials(credential):
    '''
    Function to save a credential
    Args:
        credential : the credential to be saved
    '''

    credential.save_credential()


def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credential.delete_credential(credentials)


def check_existing_credentials(name):
    '''
    Function that checks if a user credential name already exists
    Args:
        name : the credential name
    '''

    return Credential.credential_exist(name)

def search_credential(account):
    ''' funtion to find the credential in the list '''
    return Credential.find_credential(account)

def display_credentials(password):
    '''
    Function that returns all the saved credentials
    '''

    return Credential.display_credential(password)

def create_generated_password(name):
    '''
    Function that generates a password for the user
    Args:
        name : the name of the account
    '''
    password = Credential.generate_password()

    return password

#MAIN METHOD TO INVOKE ALL OTHER CLASS METHODS
def main():
    '''
    Function running the Password Locker app
    '''
    print("\n")
    print('''       <<< Welcome to Password Locker >>> \n \n''')

    while True:
        '''
        Loop that is running the entire application
        '''

        print('''        ***Use these short codes to navigate***:\n
        (ca) - Create a password locker account \n
        (du) - Display current users \n
        (lg)- Log into account \n
        (ex) - Exit application''')

        # Get short codes from the user
        short_code = input().lower()

        if short_code == 'ca':
            '''
            Creating a Password Locker account
            '''

            print("\n")
            print("New Password Locker Account")
            print("-"*10)# prints a ten dotted-line

            print("User name ...")
            name = input()

            print("Password ...")
            password = input()

            # Create and save new user
            save_users( create_user( user_name,user_password) )

            print("\n")
            print(f"{user_name} Welcome to Password Locker")
            print("\n")

        elif short_code == 'du':
            '''
            Display the names of the current users
            '''

            if display_users():
                print("\n")
                print("Here are the current users of Password Locker")
                print("-"*10)

                for user in display_users():
                    print(f"{user.name}")
                    print("-"*10)
            else:
                print("\n")
                print("Password Locker has no current user.\n    Be the first user :)")
                print("\n")

        elif short_code == 'lg':
            '''
            Logs in the user into their Password Locker account
            '''
            print("\n")
            print("Log into Password Locker Account")
            print("Enter the user name")
            name = input()

            print("Enter the password")
            user_password = input()

            if user_log_in(user_name , user_password) == None:
                print("\n")
                print("Please try again or create an account")
                print("\n")

            else:

                user_log_in(user_name,user_password)
                print("\n")
                print(f'''{user_name} welcome to your Credentials\n
                ''')

                while True:
                    '''
                    Loop to run functions after logging in
                    '''
                    print(''' Use these Short codes to navigate:\n\n
                    (cc) - Add new credential \n
                    (dc) - Display Credentials \n
                    (cg) - Create new credentials \n
                    (dl) - Delete Credentials \n
                    (ex) - Exit Credentials''')

                    # Get short code from the user
                    short_code = input().lower()

                    if short_code == 'cc':
                        '''
                        Creating a Credential
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        name = input()

                        print("Password of the credential ...")
                        credential_password = input()

                        # Create and save new user
                        save_credentials( create_credentail( user_password, credential_name, credential_password) )

                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                    elif short_code == 'dc':
                        '''
                        Displaying credential name and password
                        '''

                        if display_credentials(user_password):
                            print("\n")
                            print(f"{user_name}\'s credentials")
                            print("-"*10)

                            for credential in display_credentials(user_password):
                                print(f"Account ..... {credential.credential_name}")
                                print(f"Password .... {credential.credential_password}")
                                print("-"*10)

                        else:
                            print("\n")
                            print("You have no credentials")
                            print("\n")

                    elif short_code == 'cg':
                        '''
                        Creating a credential with a generated password
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        # Save new credential with its generated password
                        save_credentials( Credential(user_password, credential_name, (create_generated_password(credential_name)) ) )
                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                    elif short_code == 'ex':
                        print(f"See you later {user_name}")
                        print("\n")
                        break

                    elif short_code == 'dl':
                        while True:
                            print(f"Dear {user_name}, which credential would you like to delete?\n ")
                            cred_to_delete = input()

                            if check_existing_credentials(cred_to_delete):

                                search_cred = search_credential(cred_to_delete)

                                print(f"ACOUNT: {search_cred.credential_name} \n ")
                                print("Are You Sure You want to delete? y/n")
                                confirm = input().lower()
                                if confirm == 'y':
                                    #pass
                                    delete_credential(search_cred)
                                    print("Credential has been deleted ")
                                    break
                                elif confirm == 'n':
                                    continue

                            else:
                                print(f"Sorry {user_name},You do not have {cred_to_delete} as your credentials" )
                                break


                        print(f"{user_name} you are about to delete somn")
                    #    pass
                        #break

                    else:
                        print("\n")
                        print(f'''{short_code} does not compute.
                        Please use the short codes''')
                        print("\n")

        elif short_code == 'ex':
            '''
            Exit Password Locker
            '''
            print("\n")


            break

        else:
            print("\n")
            print(f'''{short_code} is an invalid command
    Please use the short codes''')
            print("\n")

if __name__ == '__main__':
    main()
