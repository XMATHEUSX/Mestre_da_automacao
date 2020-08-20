import PySimpleGUI as sg

# Tema
sg.theme('Reddit')

# Layout
layout = [
    [sg.Text('Log De informação')],
    [sg.Output(size=(50,5))],
    [sg.Input(key=('input'))],
    [sg.Button('Salvar Dados')]
]

# Janela
Janela = sg.Window('Opção de valores', layout)
# leitura dos valores da tela
while True:
    evento, dados = Janela.Read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Salvar Dados':
        print(dados['input'])


Janela.close()
