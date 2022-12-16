import mysql.connector
from mysql.connector import Error
import time

class DBConnection:
    def __init__(self):
        """ Create a instance of DB Connection.

            Args:
                None.

            Atributes:
                host(str): host of MYSQL DB
                username(str): User name of DB
                password(str): Password of DB
                db_name(str): Name of schema
                conn(Mysql Obj): Connection of mysql Obj
                cursor(Mysql Obj): Cursost of Mysql Obj

            Except:
                None.
        """
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._db_name = None
        self._conn = None
        self._cursor = None

    def set_credentials(self, host, port, username, password, db_name):
        """ Set Credentials for DB acess.
            Args:
                host (str): Host of mysql example: Localhost.
                port (str): Port of Mysql, standart port is 3306.
                username (str): User name of mysql example: root.
                password (str): Password of mysql.
                db_name (str): Name of Db to conect.

            Except:
                None.
        """
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._db_name = db_name

    def create_conn(self):
        """ Creates connection with choosen DB.
            Args:
                None.

            Except:
                Mysql Error.
        """
        try:
            if (self._db_name is None and self._conn is None):
                print("Connection Failed.\n")
                print("Try set Credentials for Db Acess.\n")
                return None
            else:
                self._conn = mysql.connector.connect(host=self._host, port=self._port,user=self._username, passwd=self._password, database=self._db_name)
                self._cursor = self._conn.cursor()
                print("Connection Successful. MYSQL Ver: {}\n".format(self._conn.get_server_info()))
                print(f"At Database {self._db_name}\n")
        except Error as err:
            print(f"Data Base Error Opening.\nError: '{err}'")

    def execute(self, query):
        """ Method to execute a query on DB
            Args:
                query (str): Query to esexute on DB.

            Execept: 
                MYSql Error.
        """
        try:
            self._cursor.execute(query)
        except Error as err:
            print("Error Query Execute\n.")
            print(f"Error: '{err}'")

    def commit(self):
        """ Method to commit  on DB and save changes
            Args:
                None

            Execept: 
                MYSql Error.
        """
        try:
            self._conn.commit()
            print("Successfully Saved Changes\n")
        except Error as err:
            print(f"Commit Error.\nError: '{err}'")

    def conclose(self):
        """ Method to execute clone connection with DB

            Args:
                None.

            Execept: 
                MYSql Error.
        """
        try:
            if self._conn.is_connected():
                self._conn.close()
                self._conn = None
                self._cursor = None
                print("Connection close Successfully.\n")
        except Error as err:
            print(f"Connection close error.\nError: '{err}'")

    def insert_reg(self, table, d_values):
        """ Method to insert reg on DB.

            Args:
                table(str): Choose table for input data
                d_values(dict): Keys, cols about Db and Dict Values(D.V.) is a values for data input.

            Return:
                False, if data input failure.

            Except:
                Error about Mysql integrity Error.
        """
        try:
            into = '(' + ', '.join(tuple(d_values.keys())) + ')'
            values = tuple(d_values.values())
            self._cursor.execute(f"""INSERT INTO {table} {into} VALUES {values};""")
            print("Successfully insertion record.")
            self.commit()
        except Error as err:
            print(f"Record insertion failure.\nError: '{err}'")
            return False

    def update_register(self, table, update, where):
        """ Method to update reg on DB.

            Args:
                table(str): Choose table for update data.
                update(str): Set a data for Database.
                where(str): Choose column with condition.

            Return:
                False, if data update failure.

            Except:
                Error about sqlite integrity Error.
        """
        try:
            self._cursor.execute(f"""UPDATE {table} SET {update} WHERE {where}; """)
            print("Successfully update record.")
            self.commit()
        except Error as err:
            print(f"Updating Failure.\n Error:{err}")
            return False

    def delete_register(self, table, where):
        """ Method to delete reg on DB.

            Args:
                table(str): Choose table for update data.
                where(str): Choose column with condition.

            Return:
                False, if data delete failure.

            Except:
                Error about sqlite integrity Error.

        """
        try:
            self._cursor.execute(f"""DELETE FROM {table} WHERE {where};""")
            self.commit()
        except Error as err:
            print(f"Delete Failure.\n Error:{err}")
            return False

    def search_register(self, select_data, table, where):
        """ Method to search register on DB.

            Args:
                select_data(str): Select da data in DB, such column.
                table(str): Choose table for update data.
                where(str): Choose column with condition

            Return:
                result.fetchone is da tuple with one column, about choose data.
                False, if data search failure.

            Except:
                Error about sqlite integrity Error.
        """
        try:
            self._cursor.execute(f"""SELECT {select_data} FROM {table} WHERE {where};""")
            result = self._cursor.fetchone()
            return result
        except Error as err:
            print(f"Search Failure.\nError: {err}")
            return False


if __name__ == '__main__':
    db = DBConnection()
    db.set_credentials("localhost","3306","root", "root", "Silver_POS")
    db.create_conn()
    """
    example: db.update_register('USERS', "first_names = 'Matheus', last_names = 'Vigânigo', user_names = 'viga99',
    passwords = '45456521'", 7)
    db.insert_reg("STOCKS", {'product_code':"41564654gg", 'product_name':"Produto1", 'product_weight':'45', 'qty_stock':'45'})
    db.insert_reg("USERS", {'first_names':'Matheus', 'last_names':'Vigânigo', 'user_names':'viga99', 'passwords':'14654r56ggggf'})
    db.update_register('USERS', "first_names = 'Matheus', last_names = 'Vigânigo', user_names = 'viga99', passwords = '45456521'", 7)
    """
    result = db.search_register("user_names", "USERS", """user_names='viga99'""")
    print(result)
    db.conclose()

else:
    Exception("Execution Error")
