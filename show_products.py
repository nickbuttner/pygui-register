import PySimpleGUI as gui 
from product_list import product_list 

gui.theme('DarkAmber')

class show_products:
    def __init__(self):
        content = []
        result = product_list()

        for i, each, in enumerate(result):
            id = each[0]
            name = each[1]
            price = each[2]
            quantity = each[3]

            product = [gui.Text("Id: " + str(id), size=(8,2), font=(18)), gui.Text("Nome: " + name, size=(8,2), font=(18)), gui.Text("Preço: " + str(price), font=(18), size=(8,2)), gui.Text("Quantidade: " + str(quantity), size=(8,2), font=(18))]
            content.append(product)

        self.screen = gui.Window("lista de produtos").layout(content)
    def show(self):
        self.values = self.screen.Read()

products = show_products()
products.show()
