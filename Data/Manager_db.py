import sqlite3


class Access:
    def __init__(self, db_name):
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
        self.conn.close()
        print("Close Connection")

    def commit_on_db(self):
        self.conn.commit()


class ClientDB(Access):
    def __init__(self, db_name):
        super().__init__(db_name)

    def create_schema(self, tb_name):
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

    def input_register(self, table, values):
        try:
            # data = list(input("Input coluns about database.\n"))
            data = ['first_name', 'last_name', 'user_name', 'password']
            for i in range(len(data)-1):
                slq_script = ("""
                INSERT INTO %s ( """ + data[i] + """) VALUES(?,?,?,?) """)
                if i == len(data)-1:
                    self.cursor.execute(slq_script, values)
            self.commit_on_db()
            print("Successfully inserted record.")
        except sqlite3.IntegrityError:
            print("Record insertion failure.")
            return False


if __name__ == '__main__':
    db = ClientDB("SilverPOS.db")
    db.input_register("USERS", ["Mario", "José", "MJ", "878kl94216"])
    db.close_db()
else:
    Exception("Execution Error")
