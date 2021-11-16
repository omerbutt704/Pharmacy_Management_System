from Classes import *
from Model import *


class Controller:
    # CONSTRUCTOR
    def __init__(self, password) -> None:
        self.password = password
        self.model = Model("localhost", "root", password, "pharmacy")
