from sqlite3 import connect
import os.path
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "SilverPOS.db")


class GetInformation:

    def get_users():
        client = connect(db_path)
        db = client.cursor()
        db.execute("""
        SELECT first_names, last_names, user_names, passwords FROM USERS
        """)
        _users = OrderedDict(
            first_names={},
            last_names={},
            user_names={},
            passwords={},
        )
        first_names = []
        last_names = []
        user_names = []
        passwords = []
        for line in db.fetchall():
            first_names.append(line[0])
            last_names.append(line[1])
            user_names.append(line[2])
            passwords.append(line[3])
        db.close()
        users_length = len(first_names)
        idx = 0
        while idx < users_length:
            _users['first_names'][idx] = first_names[idx]
            _users['last_names'][idx] = last_names[idx]
            _users['user_names'][idx] = user_names[idx]
            _users['passwords'][idx] = passwords[idx]

            idx += 1
        return _users

    def get_products():
        client = connect(db_path)
        db = client.cursor()
        db.execute("""
        SELECT product_code, product_name, product_weight, qty_stock FROM STOCKS
        """)
        _stocks = OrderedDict(
            product_codes={},
            product_names={},
            product_weights={},
            qty_stocks={},
        )
        product_codes = []
        product_names = []
        product_weighs = []
        qty_stocks = []
        for line in db.fetchall():
            product_codes.append(line[0])
            product_names.append(line[1])
            product_weighs.append(line[2])
            qty_stocks.append(line[3])
        db.close()
        products_length = len(product_codes)
        idx = 0
        while idx < products_length:
            _stocks["product_codes"][idx] = product_codes[idx]
            _stocks["product_names"][idx] = product_names[idx]
            _stocks["product_weights"][idx] = product_weighs[idx]
            _stocks["qty_stocks"][idx] = qty_stocks[idx]
            idx += 1
        return _stocks


