import Model
from Model import *


class Controller:
    # CONSTRUCTOR
    def __init__(self, password) -> None:
        self.password = password
        self.model = Model("localhost", "root", password, "pharmacy")

    def sign_up(self, status):
        email = input("Enter Email: ")
        password = input("Enter Password\n(Length > 5): ")
        while len(password) < 5:
            password = input("(Length > 5): ")
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
                    choice = input("to Add Medicine\t\tPress 1\nto Delete Medicine\tPress 2\nBack\t\t\t\tPress "
                                   "3\nChoice: ")
                    if choice == "1":
                        name = input("Adding Medicine...\nName: ")
                        while True:
                            try:
                                price = int(input("Price: "))
                                break
                            except ValueError:
                                print("Enter a Number!")
                        while True:
                            try:
                                quantity = int(input("Quantity: "))
                                break
                            except ValueError:
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
                        name = input("Deleting Medicine...\nName: ")
                        formula = input("Formula: ")
                        delete = self.model.delete_medicine(name, formula, user)
                        if delete:
                            print("O : Medicine Deleted!")
                        else:
                            print("X : Error: Delete Failure")
                    else:
                        return
            elif status == "Customer":
                while True:
                    choice = input("to Give Prescription\tPress 1\nBack\t\t\t\t\tPress 2\nChoice: ")
                    if choice == "1":
                        while True:
                            try:
                                many = int(input("How many medicine you wanna buy? "))
                                break
                            except ValueError:
                                print("Enter a Number!")
                        medicines = []
                        for i in range(many):
                            name = input("Details of Medicine you want to buy!\nName: ")
                            while True:
                                try:
                                    quantity = int(input("Quantity: "))
                                    break
                                except ValueError:
                                    print("Enter a Number!")
                            med = Prescription(name, quantity)
                            medicines.append(med)
                        print("Total Bill: Rs.", self.model.order(medicines))
                        self.model.payment = 0
                        input("Press Any key to Pay...")
                        print("Bill Payment Successful!")
                        return
                    else:
                        return
        else:
            print('O : SignIn Failed!')
