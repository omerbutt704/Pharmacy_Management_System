import pymysql
from Classes import *


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
                arg = (userid, medicine.name, medicine.price, medicine.description, medicine.formula, medicine.quantity)
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
