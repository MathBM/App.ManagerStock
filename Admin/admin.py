# Class of Python module
from collections import OrderedDict
from datetime import datetime

# Class of Kivy module
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

# Class of Manager Data Base with sqlite
from Data.Manager_db import ClientDB
from Utils.datatable import DataTable
database_dir = r"D:\App.ManagerStock\Data\SilverPOS.db"


class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = ClientDB(database_dir)

        # Display Users
        content = self.ids.scrn_contents
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

        # Display Products
        product_scrn = self.ids.scrn_product_content
        products = self.get_products()
        prod_table = DataTable(table=products)
        product_scrn.add_widget(prod_table)

    def add_user_fields(self):
        target = self.ids.ops_fields
        crud_first = TextInput(hint_text='First Name', multiline=False)
        crud_last = TextInput(hint_text='Last Name', multiline=False)
        crud_user = TextInput(hint_text='User Name', multiline=False)
        crud_pwd = TextInput(hint_text='Password', multiline=False)
        # crud_des = Spinner(text='Operator', values=['Operator', 'Administrator'])
        # crud_sumit = Button(text='Add', size_hint_x=None, width=100,on_release=lambda x)
        self.add_user(crud_first.text, crud_last.txt, crud_user.txt, crud_pwd.txt)
        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_pwd)
        # target.add_widget(crud_des)
        target.add_widget(crud_sumit)

    def add_user(self, first, last, user, pwd):
        content = self.ids.scrn_contents
        content.clear_widgets()

        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

    # Read information on DB about users
    def get_users(self):
        _users = OrderedDict()
        _users['first_names'] = {}
        _users['last_names'] = {}
        _users['user_names'] = {}
        _users['passwords'] = {}
        first_names = []
        last_names = []
        user_names = []
        passwords = []
        self.db.cursor.execute("SELECT first_names, Last_names, user_names, passwords FROM USERS")
        for line in self.db.cursor.fetchall():
            first_names.append(line[0])
            last_names.append(line[1])
            user_names.append(line[2])
            pwd = line[3]
            if len(pwd) > 10:
                pwd = pwd[:10] + '...'
            passwords.append(pwd)
        users_length = len(first_names)
        idx = 0
        while idx < users_length:
            _users['first_names'][idx] = first_names[idx]
            _users['last_names'][idx] = last_names[idx]
            _users['user_names'][idx] = user_names[idx]
            _users['passwords'][idx] = passwords[idx]

            idx += 1
        return _users

    # Read information on DB about products
    def get_products(self):
        _stocks = OrderedDict()
        _stocks['product_codes'] = {}
        _stocks['product_names'] = {}
        _stocks['product_weights'] = {}
        _stocks['qty_stocks'] = {}
        product_codes = []
        product_names = []
        product_weighs = []
        qty_stocks = []
        self.db.cursor.execute("SELECT product_code, product_name, product_weight, qty_stock FROM STOCKS")
        for line in self.db.cursor.fetchall():
            product_codes.append(line[0])
            name = line[1]
            if len(name) > 10:
                name = name[:10] + '...'
            product_names.append(name)
            product_weighs.append(line[2])
            qty_stocks.append(line[3])
        products_length = len(product_codes)
        idx = 0
        while idx < products_length:
            _stocks['product_codes'][idx] = product_codes[idx]
            _stocks['product_names'][idx] = product_names[idx]
            _stocks['product_weights'][idx] = product_weighs[idx]
            _stocks['qty_stocks'][idx] = qty_stocks[idx]
            idx += 1
        return _stocks

    # Change Screens about admin menu
    def change_screen(self, instance):
        if instance.text == 'Manage Products':
            self.ids.scrn_mngr.current = 'scrn_product_content'
        elif instance.text == 'Manage Users':
            self.ids.scrn_mngr.current = 'scrn_content'
        else:
            self.ids.scrn_mngr.current = 'scrn_analysis' 


class AdminApp(App):
    def build(self):
        return AdminWindow()


if __name__ == "__main__":
    adminapplication = AdminApp()
    adminapplication.run()
