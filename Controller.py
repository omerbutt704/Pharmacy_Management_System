from Classes import *
from Model import *

class Controller:
    # CONSTRUCTOR
    def __init__(self) -> None:
        self.model = AddressBookModel("localhost", "root", "2334011019", "lab4")