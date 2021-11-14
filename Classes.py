# ADMIN and CUSTOMER
class User:
    #                       member datatype          Function return type
    #                             |                       |
    def __init__(self, username: str, password: str) -> None:
        self.username, self.password = username, password


# MEDICINE
class Medicine:
    def __init__(self, name: str, formula: str, description: str, price: int, quantity: int) -> None:
        self.name, self.formula = name, formula
        self.description, self.price = description, price
        self.quantity = quantity


# INVENTORY
class Inventory(Medicine):
    def __init__(self, meds: list, name: str, formula: str, description: str, price: int, quantity: int) -> None:
        super().__init__(name, formula, description, price, quantity)
        self.medicine = meds

    def insert_medicine(self, med: Medicine) -> bool:
        return True

    def delete_medicine(self, med: Medicine) -> bool:
        return True

    def check_medicine(self, med: Medicine) -> bool:
        return True

    def check_quantity(self, med: Medicine) -> bool:
        return True

    # def alternative(self, formula: str) -> Medicine:


# PRESCRIPTION
class Prescription:
    def __init__(self, name: str, quantity: str) -> None:
        self.name, self.quantity = name, quantity
