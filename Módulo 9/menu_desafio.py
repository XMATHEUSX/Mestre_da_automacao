import PySimpleGUI as sg


# Layout
menu = [
    ['File',['New File','Save','Save as']],
    ['Edit',['Size',['Change Resolution','Change Height','Change Width']]],
    ['About',['About author']]
]

layout = [
    [sg.Menu(menu)],
    [sg.Text('Bem Vindo a este Aplicativo')],
    [sg.Output(size=(40,20))]

]
# Janela
Janela = sg.Window('Opção de valores', layout)
# leitura dos valores da tela
while True:
    evento, dados = Janela.Read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'OK':
        print(evento)
        print(dados)
    if evento == 'About author':
        sg.popup('Desenvolvido por Matheus Xavier 2020')


Janela.close()
