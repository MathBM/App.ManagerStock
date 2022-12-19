from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from Admin.admin import AdminWindow
from Signing.signing import SigninWindow
from Operating.operating import OperatingWindow

class MainWindown(BoxLayout):

    signing_widget = SigninWindow()
    admin_widget = AdminWindow()
    operator_widget = OperatingWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.scrn_si.add_widget(self.signing_widget)
        self.ids.scrn_admin.add_widget(self.admin_widget)
        self.ids.scrn_op.add_widget(self.operator_widget)

class MainApp(App):
    def build(self):
        return MainWindown()


if __name__ == '__main__':
    MainApp().run()

else:
    Exception("Execution Error")
