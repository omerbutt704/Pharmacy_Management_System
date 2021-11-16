import pymysql


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

    # DESTRUCTOR - CLOSING CONNECTION
    def __del__(self) -> None:
        if self.connection is not None:
            self.connection.close()
