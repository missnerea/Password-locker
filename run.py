#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

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

def del_user(user)():
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user(email):
    '''
    Function that finds a user by email and returns the email
    '''
    return User.find_by_email(email)

ef check_existing_users(email):
    '''
    Function that check if a user exists with that email and return a Boolean
    '''
    return User.user_exist(email)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
