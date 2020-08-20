import PySimpleGUI as sg

# Tema
sg.theme('Reddit')

# Layout
layout = [
    [sg.Text('Digite Um Site')],
    [sg.Input(key=('site'))],
    [sg.Text('Digite Seu Nome')],
    [sg.Input(key=('nome'))],
    [sg.Text('Fazer pesquisas em quais sites')],
    [sg.Checkbox('Google', key='Google'), sg.Checkbox(
        'Yahoo', key='Yahoo'), sg.Checkbox('Bing', key='Bing')],
    [sg.Text('Quais periodos o programa deve rodar?')],
    [sg.Checkbox('Manhã', key='manha'), sg.Checkbox(
        'Tarde', key='tarde'), sg.Checkbox('Noite', key='noite')],
    [sg.Text('Rodar o programa de madrugada ?')],
    [sg.Radio('Sim', group_id='HorarioExecucao'),
     sg.Radio('Não', group_id='HorarioExecucao')],
    [sg.Text('Quantas Dias o programa ira rodar?')],
    [sg.Slider(key='qtd', range=(1, 14), orientation='h',
               size=(34, 20), default_value=1)],
    [sg.Text('Quantas mensagens por dia ?')],
    [sg.Slider(key='qtd', range=(1, 100), orientation='h',
               size=(34, 20), default_value=1)],
    [sg.Button('Enviar dados', key=("enviar_dados")),
     sg.Text(key="acesso", size=(20, 1))],
    [sg.Button('Salvar configurações', key=("salvar"))]
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
