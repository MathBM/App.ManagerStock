# Class of Python module
import hashlib
from collections import OrderedDict
import matplotlib.pyplot as plt
# from datetime import datetime

# Class of Kivy-module
from kivy.app import App
from kivy.clock import ClockBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
# from kivy.uix.spinner import Spinner

# Class of Manager Data Base with sqlite
from Data.Manager_db import ClientDB
from Utils.datatable import DataTable

database_dir = r"D:\App.ManagerStock\Data\SilverPOS.db"


class Notify(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (.7, .7)


class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.notify = Notify()

        # Connection with DB
        self.db = ClientDB(database_dir)

        # Display Users
        content = self.ids.scrn_contents
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

        # Display Products
        product_scrn = self.ids.scrn_product_contents
        products = self.get_products()
        prod_table = DataTable(table=products)
        product_scrn.add_widget(prod_table)

    def kill_switch(self):
        self.notify.dismiss()
        self.notify.clear_widgets()

    # Fields for type information when add.
    def add_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_first = TextInput(hint_text='First Name', multiline=False)
        crud_last = TextInput(hint_text='Last Name', multiline=False)
        crud_user = TextInput(hint_text='User Name', multiline=False)
        crud_pwd = TextInput(hint_text='Password', multiline=False)
        # crud_des = Spinner(text='Operator', values=['Operator', 'Administrator'])
        crud_submit = Button(text='Add', size_hint_x=None, width=100,
                             on_release=lambda x: self.add_user(crud_first.text,
                                                                crud_last.text,
                                                                crud_user.text,
                                                                crud_pwd.text))
        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_pwd)
        # target.add_widget(crud_des)
        target.add_widget(crud_submit)

    # add user in DB
    def add_user(self, first, last, user, pwd):
        content = self.ids.scrn_contents
        content.clear_widgets()
        pwd = hashlib.sha3_512(pwd.encode()).hexdigest()
        if first == '' or last == '' or user == '' or pwd == '':
            self.notify.add_widget(Label(text='[color=#FF0000][b]All Fields Required[/b][/color]', markup=True))
            self.notify.open()
            ClockBase.schedule_once(self.kill_switch)

        self.db.input_register('USERS',
                               {'first_names': first, 'last_names': last, 'user_names': user, 'passwords': pwd})
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

    # Fields for type information when update.
    def update_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_first = TextInput(hint_text='First Name', multiline=False)
        crud_last = TextInput(hint_text='Last Name', multiline=False)
        crud_user = TextInput(hint_text='User Name', multiline=False)
        crud_pwd = TextInput(hint_text='Password', multiline=False)
        # crud_des = Spinner(text='Operator', values=['Operator', 'Administrator'])
        crud_submit = Button(text='Update', size_hint_x=None, width=100,
                             on_release=lambda x: self.update_user(crud_first.text,
                                                                   crud_last.text,
                                                                   crud_user.text,
                                                                   crud_pwd.text))
        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_pwd)
        # target.add_widget(crud_des)
        target.add_widget(crud_submit)

    # Update user in DB. The key is user_name
    def update_user(self, first, last, user, pwd):
        content = self.ids.scrn_contents
        content.clear_widgets()
        pwd = hashlib.sha3_512(pwd.encode()).hexdigest()
        update = "first_names = '{}', last_names = '{}', user_names = '{}', passwords = '{}'".format(first, last, user,
                                                                                                     pwd)
        where = "user_names = '{}'".format(user)
        self.db.update_register('USERS', update, where)
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

    # Fields for type information when remove.
    def remove_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_user = TextInput(hint_text='User Name', multiline=False)
        crud_submit = Button(text='Remove', size_hint_x=None, width=100,
                             on_release=lambda x: self.remove_user(crud_user.text))

        target.add_widget(crud_user)
        target.add_widget(crud_submit)

    # Removes User in DB. The key is user_name
    def remove_user(self, user):
        content = self.ids.scrn_contents
        content.clear_widgets()

        where = "user_names = '{}'".format(user)
        self.db.delete_register('USERS', where)

        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

    # Read information on DB about users.
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

    # Fields for type information about products when add.
    def add_product_fields(self):
        target = self.ids.ops_fields_p
        target.clear_widgets()

        crud_code = TextInput(hint_text='Product Code', multiline=False)
        crud_name = TextInput(hint_text='Product Name', multiline=False)
        crud_weight = TextInput(hint_text='Product Weight', multiline=False)
        crud_qty = TextInput(hint_text='Qty Stocks', multiline=False)
        crud_submit = Button(text='Add', size_hint_x=None, width=100,
                             on_release=lambda x: self.add_product(crud_code.text, crud_name.text, crud_weight.text,
                                                                   crud_qty.text))
        target.add_widget(crud_code)
        target.add_widget(crud_name)
        target.add_widget(crud_weight)
        target.add_widget(crud_qty)
        target.add_widget(crud_submit)

    def add_product(self, code, name, weight, qty):
        content = self.ids.scrn_product_contents
        content.clear_widgets()
        self.db.input_register('STOCKS', {'product_code': code, 'product_name': name, 'product_weight': weight,
                                          'qty_stock': qty})

        products = self.get_products()
        prod_table = DataTable(table=products)
        content.add_widget(prod_table)

    # Fields for type information about product when update.
    def update_product_fields(self):
        target = self.ids.ops_fields_p
        target.clear_widgets()
        crud_code = TextInput(hint_text='Product Code', multiline=False)
        crud_name = TextInput(hint_text='Product Name', multiline=False)
        crud_weight = TextInput(hint_text='Product Weight', multiline=False)
        crud_qty = TextInput(hint_text='Qty Stocks', multiline=False)
        crud_submit = Button(text='Update', size_hint_x=None, width=100,
                             on_release=lambda x: self.update_product(crud_code.text, crud_name.text, crud_weight.text,
                                                                      crud_qty.text))
        target.add_widget(crud_code)
        target.add_widget(crud_name)
        target.add_widget(crud_weight)
        target.add_widget(crud_qty)
        target.add_widget(crud_submit)

    # Update product in DB. The key is product code
    def update_product(self, code, name, weight, qty):
        content = self.ids.scrn_product_contents
        content.clear_widgets()

        update = "product_code = '{}', product_name = '{}', product_weight = '{}', qty_stock = '{}'".format(code, name,
                                                                                                            weight, qty)
        where = "product_code = '{}'".format(code)
        self.db.update_register('STOCKS', update, where)

        products = self.get_products()
        prod_table = DataTable(table=products)
        content.add_widget(prod_table)

    # Fields for type information about product when remove.
    def remove_product_fields(self):
        target = self.ids.ops_fields_p
        target.clear_widgets()
        crud_code = TextInput(hint_text='Product Code', multiline=False)
        crud_submit = Button(text='Remove', size_hint_x=None, width=100, on_release=lambda x: self.remove_product(
            crud_code.text))

        target.add_widget(crud_code)
        target.add_widget(crud_submit)

        # Removes product in DB. The key is product.

    def remove_product(self, code):
        content = self.ids.scrn_product_contents
        content.clear_widgets()

        where = "product_code = '{}'".format(code)
        self.db.delete_register('STOCKS', where)

        products = self.get_products()
        prod_table = DataTable(table=products)
        content.add_widget(prod_table)

    # Read information in DB about products
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

    # Change Screens of admin menu
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
