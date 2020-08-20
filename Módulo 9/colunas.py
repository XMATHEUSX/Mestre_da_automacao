import PySimpleGUI as sg

# Layout
Coluna_esquerda = [[sg.Text("Insira Seu usuario")],
               [sg.Input()],
               [sg.Text("Insira Sua Senha")],
               [sg.Input()],

               ]
Coluna_meio = [
    [sg.Output(size=(40, 5))]
]
Coluna_direita = [[sg.Text("Qual site Automatizar")],
               [sg.Checkbox('opção 1'), sg.Checkbox('opção 2')]

               ]
Coluna_principal = [
    [sg.Frame("Configurações Login",(Coluna_esquerda)),
    sg.Column(Coluna_meio),
    sg.Frame("Configurações Site",(Coluna_direita))],
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
