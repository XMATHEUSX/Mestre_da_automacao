import PySimpleGUI as sg

# Tema
sg.theme('Reddit')

# Layout
layout = [
    [sg.Text('Digite Um Site', size=(17, 1)),
     sg.Text('Digite Seu Nome', size=(22, 1))],
    [sg.Input(key=('site'), size=(20, 1)), sg.Input(key=('nome'), size=(25, 1))],
    [sg.Text('Digite Um Site', size=(17, 1))],
    [sg.Multiline(autoscroll=True,size=(40,5))]
]

# Janela
Janela = sg.Window('Buscador De Site', layout)
# leitura dos valores da tela
while True:
    evento, dados = Janela.Read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'enviar_dados':
        print(evento)
        print(dados)
    if evento == 'salvar':
        sg.popup('As informações foram salvas')
        print("As informações foram salvas")


Janela.close()
