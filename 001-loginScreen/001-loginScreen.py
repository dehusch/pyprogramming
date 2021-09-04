#Criar uma tela de login
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

#LAYOUT
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#JANELA
janela = sg.Window('Tela de login', layout)
#EVENTOS
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'denis' and valores['senha'] == '123456':
            print('Bem vindo')
