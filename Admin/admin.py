from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Data.Data_Base_Conection import ClientDB
from collections import OrderedDict


class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = ClientDB("SilverPOS.db")
        self.get_users()
        self.get_products()

    def get_users(self):
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

        for line in self.db.cursor.fetchall():
            first_names.append(line[0])
            last_names.append(line[1])
            user_names.append(line[2])
            passwords.append(line[3])
        users_length = len(first_names)
        idx = 0
        while idx < users_length:
            _users['first_names'][idx] = first_names[idx]
            _users['last_names'][idx] = last_names[idx]
            _users['user_names'][idx] = user_names[idx]
            _users['passwords'][idx] = passwords[idx]

            idx += 1
            return _users

    def get_products(self):
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
        for line in self.db.cursor.fetchall():
            product_codes.append(line[0])
            product_names.append(line[1])
            product_weighs.append(line[2])
            qty_stocks.append(line[3])
        products_length = len(product_codes)
        idx = 0
        while idx < products_length:
            _stocks["product_codes"][idx] = product_codes[idx]
            _stocks["product_names"][idx] = product_names[idx]
            _stocks["product_weights"][idx] = product_weighs[idx]
            _stocks["qty_stocks"][idx] = qty_stocks[idx]
            idx += 1
        return _stocks


class AdminApp(App):
    def build(self):
        return AdminWindow()


if __name__ == "__main__":
    adminapplication = AdminApp()
    adminapplication.run()
