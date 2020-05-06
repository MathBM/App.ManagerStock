from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Data.Manager_db import ClientDB
from collections import OrderedDict
database = r"D:\App.ManagerStock\Data\SilverPOS.db"


class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = ClientDB(database)
        self.get_users()

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
        print(_users)
        return _users


class AdminApp(App):
    def build(self):
        return AdminWindow()


if __name__ == "__main__":
    adminapplication = AdminApp()
    adminapplication.run()
