import PySimpleGUI as sg
import sys
# Crie um função que retorna uma janela, para cada nova janela
# Janela1


def criar_janela1():
    layout = [
        [sg.Text('Registre seu nome na competição')],
        [sg.Button('Abrir segunda janela'), sg.Button('Sair')]
    ]
    return sg.Window('Janela', layout, finalize=True)


def criar_janela2():
    layout = [
        [sg.Text('Bem vindo a segunda tela!')],
        [sg.OK()]
    ]
    return sg.Window('Janela 2', layout, finalize=True)


# layout
janela1, janela2 = criar_janela1(), None
# Ler eventos
while True:
    janela, evento, valores = sg.read_all_windows()
    if evento in (sg.WIN_CLOSED, None):
        janela.close()
        sys.exit()
    if janela == janela1 and evento == 'Abrir segunda janela':
        janela2 = criar_janela2()
        janela1.close()
    if janela == janela2 and evento == 'OK':
        sg.popup('Botão OK foi pressionado')
