import pymysql
from Classes import *

payment = 0


class Model:
    # CONSTRUCTOR - CONNECTING TO DATABASE
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        try:
            self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                              database=self.database)
        except Exception as e:
            print("X : Error: Connection Failed", str(e))
            return

    # DESTRUCTOR - CLOSING CONNECTION
    def __del__(self) -> None:
        if self.connection is not None:
            self.connection.close()

    def check_user_exist(self, user):
        cursor, f = None, False
        try:
            if self.connection is not None:
                cursor = self.connection.cursor()
                cursor.execute("select email from users")
                emails = cursor.fetchall()
                for e in emails:
                    if user.email == e[0]:
                        f = True
                        break
        except Exception as e:
            print("Error: User Doesn't Exist", str(e))
        finally:
            if cursor is not None:
                cursor.close()
                return f

    def check_user_credentials(self, user):
        cursor, f = None, False
        try:
            if self.connection is not None:
                cursor = self.connection.cursor()
                cursor.execute("select email, password, status from users")
                credentials = cursor.fetchall()
                for c in credentials:
                    if user.email == c[0] and user.password == c[1] and user.status == c[2]:
                        f = True
                        break
        except Exception as e:
            print("Error: Invalid Credentials", str(e))
        finally:
            if cursor is not None:
                cursor.close()
                return f

    def insert_user(self, user):
        cursor, f = None, False
        try:
            if self.connection is not None:
                cursor = self.connection.cursor()
                query = "insert into users (email, password, status) values (%s, %s, %s)"
                args = (user.email, user.password, user.status)
                cursor.execute(query, args)
                self.connection.commit()
                f = True
            else:
                f = False
        except Exception as e:
            print("X : Error: Insert User Function", str(e))
            return f
        finally:
            if cursor is not None:
                cursor.close()
                return f

    def add_medicine(self, medicine, user):
        cursor, f = None, False
        try:
            if self.connection is not None:
                cursor = self.connection.cursor()
                query = "select user_id from users where email = %s"
                args = user.email
                cursor.execute(query, args)
                userid = cursor.fetchone()
                userid = userid[0]
                query = "insert into medicine (admin_id, med_name, price, description, formula, quantity) values (%s,%s,%s,%s,%s,%s)"
                arg = (userid, medicine.med_name, medicine.price, medicine.description, medicine.formula, medicine.quantity)
                cursor.execute(query, arg)
                self.connection.commit()
                f = True
            else:
                f = False
        except Exception as e:
            print("X : Error: Add Medicine Function", str(e))
            f = False
        finally:
            if cursor is not None:
                cursor.close()
                return f

    def delete_medicine(self, name, formula, user):
        cursor, f = None, False
        try:
            if self.connection is not None:
                cursor = self.connection.cursor()
                query = "select user_id from users where email = %s"
                args = user.email
                cursor.execute(query, args)
                userid = cursor.fetchone()
                userid = userid[0]
                query = "delete from medicine where admin_id = %s and med_name = %s and formula = %s"
                arg = (userid, name, formula)
                cursor.execute(query, arg)
                self.connection.commit()
                f = True
            else:
                f = False
        except Exception as e:
            print("X : Error: Delete Medicine Function", str(e))
            f = False
        finally:
            if cursor is not None:
                cursor.close()
                return f

    def search_medicine_name(self, name):
        cursor, check = None, []
        try:
            if self.connection is not None:
                cursor = self.connection.cursor()
                query = "select med_name, quantity, price, formula from medicine where med_name=%s"
                args = name
                cursor.execute(query, args)
                check = cursor.fetchone()
        except Exception as e:
            print("X : Error: Search: Name")
            if cursor is not None:
                cursor.close()
        finally:
            if cursor is not None:
                cursor.close()
            return check

    def alternative(self, formula):
        cursor, check = None, []
        try:
            if self.connection is not None:
                cursor = self.connection.cursor()
                query = "select med_name, quantity, price, formula from medicine where formula=%s"
                args = formula
                cursor.execute(query, args)
                check = cursor.fetchall()
        except Exception as e:
            print("X : Error: Alternative")
            if cursor is not None:
                cursor.close()
        finally:
            if cursor is not None:
                cursor.close()
            return check

    def order(self, medicines):
        global payment
        cursor = None
        try:
            if self.connection is not None:
                for med in medicines:
                    m = self.search_medicine_name(med.med_name)
                    if m is None:
                        print("Medicine Not Found")
                    else:
                        if m[1] > med.quantity:
                            print(m[0], " in Cart, Quantity: ", med.quantity, " , Price: ", m[2])
                            payment = payment + (m[2] * med.quantity)
                        elif m[1] == med.quantity:
                            print("Not enough Quantity in Inventory\nWe can provide ", med.quantity - 1)
                            choice = input("\nWant to Take it(y/n): ")
                            if choice == "y" or choice == "Y":
                                print(m[0], " in Cart, Quantity: ", med.quantity - 1, " , Price: ", m[2])
                                payment = payment + (m[2] * (med.quantity - 1))
                            else:
                                choice = input("Want an alternative(y/n): ")
                                if choice == "y" or choice == "Y":
                                    alternatives = self.alternative(m[3])
                                    for a in alternatives:
                                        print("Name: ", a[0], "Quantity: ", a[1], "Price: ", a[2], "Formula: ", a[3])
                                    name = input("Which one you want?Enter Name: ")
                                    mm = self.search_medicine_name(name)
                                    mmm = [Prescription(mm[0], mm[1])]
                                    payment = self.order(mmm)

            return payment
        except Exception as error:
            print("X: Order Failed!", str(error))
