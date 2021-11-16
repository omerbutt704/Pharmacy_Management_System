from Controller import *


def main():
    password = input("To Connect to Database\nEnter Password: ")
    controller = Controller(password)
    while True:
        choice = input("Enter as Admin\t\tPress 1\nEnter as Customer\tPress 2\nExit\t\t\t\tPress 3\nChoice: ")
        # ADMIN
        if choice == "1":
            while True:
                choice = input("to Sign Up\tPress 1\nto Sign In\tPress 2\nBack\t\tPress 3\nChoice: ")
                if choice == "1":
                    controller.sign_up("Admin")
                elif choice == "2":
                    controller.sign_in("Admin")
                else:
                    break
        # CUSTOMER
        elif choice == "2":
            while True:
                choice = input("to Sign Up\tPress 1\nto Sign In\tPress 2\nBack\t\tPress 3\nChoice: ")
                if choice == "1":
                    controller.sign_up("Customer")
                elif choice == "2":
                    controller.sign_in("Customer")
                else:
                    break
        # EXIT
        else:
            print("\n\t\tGoodBye OwO")
            break


main()
