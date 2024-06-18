import PySimpleGUI as gui 
from customer_list import customer_list

gui.theme('DarkAmber')

class show_customer:
    def __init__(self):
        content = []
        result = customer_list()

        for i, each, in enumerate(result):
            id = each[0]
            name = each[1]
            email = each[2]
            gender = each[3]
            age = each[4]
            if email == 1:
                email = "aceita receber email"
            else:
                email = "nao aceita receber email"

            customer = [gui.Text("Id: " + str(id), size=(8,2), font=(18)), gui.Text("Nome: " + name, size=(8,2), font=(18)), gui.Text("Email: " + email, size=(15,2), font=(18)), gui.Text("Sexo: " + gender, size=(8,2), font=(18)), gui.Text("Idade: " + str(age), font=(18), size=(8,2))]
            content.append(customer)

        self.screen = gui.Window("lista de clientes").layout(content)
    def show(self):
        self.values = self.screen.Read()

customer = show_customer()
customer.show()
