import hashlib
import sys
sys.path.append('./')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from Data.Manager_db import DBConnection



Builder.load_file('Signing/signing.kv')

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        self.db = DBConnection()
        self.db.set_credentials("localhost","3306","root", "root", "Silver_POS")
        self.db.create_conn()

        user = self.ids.username_field
        pwd = self.ids.pwd_field

        uname = user.text
        passw = pwd.text
        info = self.ids.info

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Username and password required.[/color]'
        else:
            user = self.db.execute(f"""SELECT * FROM USERS WHERE user_names='{uname}';""")
            if user == None:
                info.text = '[color=#FF0000]Invalid Username.[/color]'
            else:
                passw = hashlib.sha256(passw.encode()).hexdigest()
                if passw == user[4]:
                    if user[5] == 'Admin':
                        info.text = '[color=#00FF00]Logged In Successfully!!![/color]'
                        self.chance_screen('scrn_admin')
                    else:
                        info.text = '[color=#00FF00]Logged In Successfully!!![/color]'
                        self.chance_screen('scrn_op')
                else:
                    info.text = '[color=#FF0000]Invalid Password.[/color]'
        
        self.db.conclose()

    def chance_screen(self, screen_name):
        """ Method to chance Screen

            Args:
                screen_name(str): Name of screen to change.
            
            Execept:
                Error to change Screen.
            Returns:
                None.
        """
        try:
            self.parent.parent.current = screen_name
        except:
            print("Error: Not Possible change Screen.")

class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__ == "__main__":
    aplication = SigninApp()
    aplication.run()
