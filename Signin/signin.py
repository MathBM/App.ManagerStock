from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file(r"D:\App.ManagerStock\signin\signin.kv")


class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field

        uname = user.text
        passw = pwd.text
        info = self.ids.info

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Username and password required.[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Logged In Successfully!!![/color]'
                self.parent.parent.current = 'scrn_admin'
            else:
                info.text = '[color=#FF0000]Invalid Password or Username.[/color]'


class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__ == "__main__":
    aplication = SigninApp()
    aplication.run()
