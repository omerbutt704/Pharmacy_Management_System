# ADMIN and CUSTOMER
class Users:
    def __init__(self, email: str, password: str, status: str) -> None:
        self.email = email
        self.password = password
        self.status = status


class Medicine:
    def __init__(self, med_name: str, price: int, description: str, formula: str, quantity: int) -> None:
        self.med_name = med_name
        self.price = price
        self.description = description
        self.formula = formula
        self.quantity = quantity


class Inventory:
    def __init__(self, list_of_Medicines={}):
        self.med_obj = list_of_Medicines

    def get_all_medicine_details(self):
        return self.med_obj


class Prescription:
    def __init__(self, med_name: str, quantity: str) -> None:
        self.med_name, self.quantity = med_name, quantity


class Billing:
    def __init__(self, med_name, price, quantity):
        self.med_name = med_name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Name: " + self.med_name + "\nPrice: " + self.price + "\nQuantity: " + self.quantity)
