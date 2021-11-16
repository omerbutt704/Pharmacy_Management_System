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
            if status == "Admin":
                while True:
                    choice = input("to Add Medicine\tPress 1\nto Delete Medicine\tPress 2\nBack\t\tPress 3\nChoice: ")
                    if choice == "1":
                        name = input("Adding Medicine...\nName: ")
                        while True:
                            try:
                                price = int(input("Price: "))
                                break
                            except TypeError:
                                print("Enter a Number!")
                        while True:
                            try:
                                quantity = int(input("Quantity: "))
                                break
                            except TypeError:
                                print("Enter a Number!")
                        formula = input("Formula: ")
                        description = input("Description: ")
                        medicine = Medicine(name, price, description, formula, quantity)
                        add = self.model.add_medicine(medicine, user)
                        if add:
                            print("O : Medicine Added!")
                        else:
                            print("X : Error: Addition Failure")
                    elif choice == "2":
                        name = input("Deleting Medicine...Name: ")
                        formula = input("Formula: ")
                        delete = self.model.delete_medicine(name, formula, user)
                        if delete:
                            print("O : Medicine Deleted!")
                        else:
                            print("X : Error: Deleted Failure")
                    else:
                        return
            elif status == "Customer":
                while True:
                    choice = input("to Give Prescription\tPress 1\nBack\t\t\tPress 2\nChoice: ")
                    if choice == "1":
                        #
                    else:
                        return
        else:
            print('O : SignIn Failed!')
