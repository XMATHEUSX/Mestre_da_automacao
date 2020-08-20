import PySimpleGUI as sg

# Tema
sg.theme('Reddit')

# Layout
layout = [
    [sg.Text('Digite Um Site')],
    [sg.Slider(key='qtd', range=(1, 100), orientation='h',
               size=(34, 20), default_value=1)],
    [sg.Text('Digite Um Site')],
    [sg.Spin(values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
             initial_value=1, key='velocidade_de_envio_msg')],
    [sg.Text('Digite Um Site')],
    [sg.Spin(values=("Bronze", "Prata", "Ouro", 'Diamante'),
             initial_value='Bronze', key='Medalha,', size=(10,20))],
    [sg.Text('Digite Um Site')],
    [sg.Combo(values=['Iniciante', 'Intermediário', 'Avançado'],
              default_value='Iniciante')]
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


Janela.close()
