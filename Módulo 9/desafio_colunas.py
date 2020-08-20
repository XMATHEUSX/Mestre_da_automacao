import PySimpleGUI as sg

# Tema
sg.theme('Reddit')

# Layout
Coluna_esquerda = [[sg.Text("Olá estou na coluna 1")],
                   [sg.Ok()],
                   [sg.Text("Olá estou na coluna 1")],
                   [sg.Ok()],

                   ]
Coluna_meio = [
    [sg.Text("Olá estou na coluna 2")],
    [sg.Ok()],
    [sg.Text("Olá estou na coluna 2")],
    [sg.Ok()],
]
Coluna_direita = [[sg.Text("Olá estou na coluna 3")],
                   [sg.Ok()],

                  ]
Coluna_principal = [
    [sg.Column(Coluna_esquerda),
     sg.Column(Coluna_meio),
     sg.Column(Coluna_direita)],
]


# Janela
Janela = sg.Window('Opção de valores', Coluna_principal)
# leitura dos valores da tela
while True:
    evento, dados = Janela.Read()
    if evento in (sg.WIN_CLOSED, None):
        break
    if evento == 'OK':
        print(evento)
        print(dados)


Janela.close()
