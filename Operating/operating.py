import sys
import re
sys.path.append('./')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from Data.Manager_db import DBConnection

Builder.load_file("Operating/operating.kv")

class OperatingWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DBConnection()
        self.db.set_credentials("localhost","3306","root", "root", "Silver_POS")
        self.db.create_conn()

        self.stocks = self.db
        self.cart = []
        self.qty = []
        self.total = 0.00

    def update_purchases(self):
        pcode = self.ids.code_inp.text
        products_container = self.ids.products
        target_code = self.stocks.search_register('*', 'STOCKS', where=f"""product_code='{pcode}'""")
        if target_code is None:
            pass
        else:
            details = BoxLayout(size_hint_y=None, height=30, pos_hint={'top': 1})
            products_container.add_widget(details)

            code = Label(text=pcode, size_hint_x=.2, color=(.06, .45, .45, 1))
            name = Label(text=target_code[1], size_hint_x=.3, color=(.06, .45, .45, 1))
            qty = Label(text="1", size_hint_x=.1, color=(.06, .45, .45, 1))
            disc = Label(text="0.00", size_hint_x=.1, color=(.06, .45, .45, 1))
            price = Label(text="0.00", size_hint_x=.1, color=(.06, .45, .45, 1))
            total = Label(text="0.00", size_hint_x=.2, color=(.06, .45, .45, 1))
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)

            # Update Preview
            pname = "Product One"
            pprice = float(price.text)
            pqty = str(1)
            self.total += pprice
            purchase_total = '`\n\nTotal\t\t\t\t\t\t\t\t'+str(self.total)
            self.ids.cur_product.text = pname
            self.ids.cur_price.txt = str(pprice)
            preview = self.ids.recept_preview
            prev_text = preview.text
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]
            ptarget = -1
            for i, c in enumerate(self.cart):
                if c == pcode:
                    ptarget = i

            if ptarget >= 0:
                pqty = self.qty[ptarget]+1
                self.qty[ptarget] = pqty
                expr = '%s\t\tx\d\t' % pname
                rexpr = pname + '\t\tx' + str(pqty) + '\t'
                nu_text = re.sub(expr, rexpr, prev_text)
                preview.text = nu_text + purchase_total
            else:
                self.cart.append(pcode)
                self.qty.append(1)
                nu_preview = '\n'.join([prev_text, pname + '\t\tx' + pqty + '\t\t' + str(pprice), purchase_total])
                preview.text = nu_preview


class OperatingApp(App):
    def build(self):
        return OperatingWindow()


if __name__ == "__main__":
    application = OperatingApp()
    application.run()
