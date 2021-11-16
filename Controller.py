from Classes import *
from Model import *


class Controller:
    # CONSTRUCTOR
    def __init__(self, password) -> None:
        self.password = password
        self.model = Model("localhost", "root", password, "pharmacy")

    def sign_up(self, status):
        email = input("Enter Email: ")
        password = input("Enter Password\n(Length > 8): ")
        while len(password) < 8:
            password = input("(Length > 8): ")
        user = Users(email, password, status)
        taken = self.model.check_user_exist(user)
        if taken is False:
            insert = self.model.insert_user(user)
            if insert:
                print("O : Signup Successful!")
            else:
                print("X : Signup Failed!")
        else:
            print("X : Sorry! Email Taken!")

    def sign_in(self, status):
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        user = Users(email, password, status)
        valid = self.model.check_user_credentials(user)
        if valid:
            print('O : SignIn Successful!')
        else:
            print('O : SignIn Failed!')
