import sqlite3


class Access:
    def __init__(self, db_name):
        """ Access data base.

            Args:
                db_name(str): Path or name of DataBase for connection.
        """
        self.db = db_name
        try:
            self.conn = sqlite3.connect(self.db)
            self.cursor = self.conn.cursor()
            print("Data Base:\t", self.db)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQlite version:\t %s" % self.data)
        except sqlite3.Error:
            print("Data Base Error Opening.")

    def close_db(self):
        """ Close connection with DataBase.
        """
        self.conn.close()
        print("Close Connection")

    def commit_on_db(self):
        """ Save changes in DataBase.
        """
        self.conn.commit()


class ClientDB(Access):
    def __init__(self, db_name):
        """ ClientDB class is a class for access somes methods for
        write or read values in db.

        Args:
            db_name(str): Data Base name.
        """
        super().__init__(db_name)

    def create_schema(self, tb_name):
        """ Create schema and create new table in DB.

            Args:
                tb_name(str): Table name for create.
            Return:
                False, if table for created is exist.
            Except:
                sqlite Error:
                Warning: The table exist,
        """
        schema_name = 'sql/%s_schema.sql' % tb_name
        print("Creating table %s ..." % tb_name)
        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.cursor.executescript(schema)
        except sqlite3.Error:
            print("Warning: The table %s exist." % tb_name)
            return False
        print("Table %s created successfully" % tb_name)

    def input_register(self, table, d_values):
        """ Input Register on Local DB.
            Args:
                table(str): Choose table for input data
                d_values(dict): Keys, cols about Db and Dict Values(D.V.) is a values for data input.

            Return:
                False, if data input failure.

            Except:
                Error about sqlite integrity Error, duplicate value or other SQL Error.
        """
        try:
            into = tuple(d_values.keys())
            slq_script = ("""
            INSERT INTO {} {}
            VALUES(?,?,?,?) 
            """).format(table, into)
            values = list(d_values.values())
            self.cursor.execute(slq_script, values)
            print("Successfully insertion record.")
            self.commit_on_db()
        except sqlite3.IntegrityError:
            print("Record insertion failure.")
            return False

    def update_register(self, table, update, where):
        """ Input Register in Local DB.
            Args:
                table(str): Choose table for update data.
                update(str): Set a data for Database.
                where(str): Choose column with condition.

            Return:
                False, if data update failure.

            Except:
                Error about sqlite integrity Error, duplicate value or other SQL Error.

        """
        try:
            slq_script = ("""
            UPDATE {} SET {}
            WHERE {};
            """).format(table, update, where)
            self.cursor.execute(slq_script)
            print("Successfully update record.")
            self.commit_on_db()
        except sqlite3.IntegrityError:
            print("Updating Failure.")
            return False

    def delete_register(self, table, where):
        """ Delete Register in Data Base.

            Args:
                table(str):
                where(str):

            Return:
                False, if data delete failure.

            Except:
                Error about sqlite integrity Error, duplicate value or other SQL Error.

        """
        try:
            sql_script = ("""
            DELETE FROM {}
            WHERE {}
        """).format(table, where)
            self.cursor.execute(sql_script)
            self.commit_on_db()
        except sqlite3.IntegrityError:
            print("Delete Failure.")
            return False


if __name__ == '__main__':
    db = ClientDB("SilverPOS.db")
    # example: db.update_register('USERS', "first_names = 'Matheus', last_names = 'Vigânigo', user_names = 'viga99',
    # passwords = '45456521'", 7)
    # db.close_db()
else:
    Exception("Execution Error")
