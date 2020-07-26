from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from Admin.admin import AdminWindow
from Signin.signin import SigninWindow
from Operating.operating import OperatingWindow


class MainWindow(BoxLayout):
    signin_widget = SigninWindow()
    # admin_widget = AdminWindow()
    # operator_widget = OperatingWindow()

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.ids.scrn_si.add_widget(self.signin_widget)
        # self.ids.scrn_admin.add_widget(self.admin_widget)
        # self.ids.scrn_op.add_widget(self.operator_widget)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
else:
    Exception("Execution Error")
