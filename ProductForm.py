import PySimpleGUI as gui 
from Product import Product

gui.theme('DarkAmber')

class ProductForm:
    def __init__(self):
        content = [
            [gui.Text("nome: "), gui.Input()],
            [gui.Text("preço: "), gui.Input(key='txtPreco') ],
            [gui.Text("quantidade: "), gui.Input(key='txtQtd') ],
            [gui.Button("enviar")]
        ]
        self.screen = gui.Window("eachstro produto").layout(content)

    def show(self):
        self.button, self.values = self.screen.Read()
        prod = Product()
        prod.name = self.values[0]
        price = self.values['txtPreco']
        price = float(price.replace(",", ".") )
        prod.price = price
        quantity = self.values['txtquantity']
        quantity = float(quantity.replace(",", ".") )
        prod.quantity = quantity
        return prod