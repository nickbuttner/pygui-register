import PySimpleGUI as gui 
from Customer import Customer

gui.theme('DarkAmber')

class CustomerForm:
    def __init__(self):
        content = [
            [gui.Text("nome: "), gui.Input(size=(30, 0), key='txtName')],
            [gui.Checkbox("aceita receber e-mail", key='email_accept')],
            [gui.Text("sexo: ")  ], 
            [gui.Radio("Feminino",'sexo', key='feminino'), 
                gui.Radio("masculino", 'sexo', key='masculino'), 
                gui.Radio("não informar", 'sexo', key='naoInformado')],
            [gui.Text("idade: ") , gui.Slider(range=(0,150), orientation='h' , key='age', default_value=18)],
            [gui.Button("enviar") ] 
        ]
        self.screen = gui.Window("eachstro de cliente").layout(content)
    def show(self):
        self.button , self.values = self.screen.Read()
        customer = Customer()
        customer.name = self.values['txtName']
        customer.email_accept = self.values['email_accept']
        if  self.values['feminino'] :
            customer.gender = "feminino"
        elif self.values['masculino']: 
            customer.gender = "masculino"
        else:
            customer.gender = "não informado"
        customer.age = self.values['idade']
        return customer

