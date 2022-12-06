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
                print(f"At Schema {self._db_name}\n")
        except Error as err:
            print("Data Base Error Opening.\n")
            print(f"Error: '{err}'")

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
            print("Salvo com Sucesso as alterações realizadas.\n")
        except Error as err:
            print("Commit Error.\n")
            print(f"Error: '{err}'")

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
            print("Connection close error.\n.")
            print(f"Error: '{err}'")

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
            into = tuple(d_values.keys())
            values = list(d_values.values())
            #query = f"INSERT INTO {table}" + "(" +", ".join(into) + ")" + "VALUES" + "(" + "'" + "','".join(values) + "'" + ");"
            query = f"INSERT INTO {table} (" + ", ".join(into) + ") VALUES ('" + "','".join(values) + "')"
            print(query)
            self._cursor.execute(query)
            print("Successfully insertion record.")
            self.commit()
        except Error as err:
            print("Record insertion failure.")
            print(f"Error: '{err}'")
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
            slq_script = ("""
            UPDATE {} SET {}
            WHERE {};
            """).format(table, update, where)
            self.cursor.execute(slq_script)
            print("Successfully update record.")
            self.commit()
        except mysql.IntegrityError:
            print("Updating Failure.")
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
            sql_script = ("""
            DELETE FROM {} 
            WHERE {}
            """).format(table, where)
            self.cursor.execute(sql_script)
            self.commit_on_db()
        except mysql.IntegrityError:
            print("Delete Failure.")
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
            sql_script = ("""
            SELECT {} FROM {}
            WHERE {}
            """).format(select_data, table, where)
            result = self.cursor.execute(sql_script)
            self.commit_on_db()
            return result.fetchone()
        except mysql.IntegrityError:
            print("Search Failure.")
            return False


if __name__ == '__main__':
    db = DBConnection()
    db.set_credentials("localhost","3306","root", "root", "Silver_POS")
    db.create_conn()
    db.insert_reg("accounts",{"login":"Matheus", "password":"12345678","token":"343hda34234qasd","role":"Operator","ip":"0.0.0.0","active":"1"})
    # example: db.update_register('USERS', "first_names = 'Matheus', last_names = 'Vigânigo', user_names = 'viga99',
    # passwords = '45456521'", 7)
else:
    Exception("Execution Error")
