# instale o PySimpleGUI antes de rodar este arquivo:
# pip install PySimpleGUI
# para mac/linux
# pip3 install PySimpleGUI
import PySimpleGUI as sg
from pages import pag_1


sg.theme('TealMono')

def pag_inicial():
    buttons = [
        [sg.Button('Cadastrar Caso'),
         sg.Button('Sair')],
    ]

    layout = [
        [sg.Text('Ola seja bem vindo!', font=('Arial Bold',13), justification='center')],
        [sg.Text('Este é um sistema de RBC para doenças em plantações!', font=('Arial Bold', 13), justification='center')],
        [sg.Text('')],
        [sg.Column(buttons, element_justification='right', expand_x=True)]
    ]

    window = sg.Window('Sistema RBC', layout)


    while True:
        event, values = window.read()
        cnf = 0
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            break

        elif event == 'Cadastrar Caso':
            window.close()
            pag_1.pag_1()



pag_inicial()