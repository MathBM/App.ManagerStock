import sys
sys.path.append('../')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from collections import OrderedDict
from Data.Manager_db import DBConnection


Builder.load_string('''
<DataTable>:
    id: main_win
    RecycleView:
        viewclass: 'CustLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 5
            default_size: (None, 250)
            default_size_hint: (1, None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
<CustLabel@Label>:
    bcolor: (1, 1, 1 ,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos
        
''')


class DataTable(BoxLayout):
    def __init__(self, table='', **kwargs):
        super().__init__(**kwargs)

        # Connection with DB
        self.db = DBConnection()
        self.db.set_credentials("localhost","3306","root", "root", "Silver_POS")
        self.db.create_conn()

        products = table
        products = self.get_products()
        col_titles = [k for k in products.keys()]
        rows_len = len(products[col_titles[0]])
        self.columns = len(col_titles)
        table_data = []
        for t in col_titles:
            table_data.append({'text': str(t), 'size_hint_y': None, 'height': 50, 'bcolor': (.06, .45, .45, 1)})
        for r in range(rows_len):
            for t in col_titles:
                table_data.append({'text': str(products[t][r]), 'size_hint_y': None, 'height': 30, 'bcolor': (.06, .45, .45, 1)})
        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

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
        self.db.execute("SELECT * FROM STOCKS")
        for line in self.db._cursor.fetchall():
            product_codes.append(line[0])
            product_names.append(line[1])
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


"""
class DataTableApp(App):
    def build(self):
        return DataTable()


if __name__ == '__main__':
    datatable = DataTableApp()
    datatable.run()
"""