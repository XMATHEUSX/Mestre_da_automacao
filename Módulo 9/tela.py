import PySimpleGUI as sg

#Tema
sg.theme('Reddit')

#Layout
layout = [
    [sg.Text('Digite Seu Nome')],
    [sg.Input(key=('nome'))],
    [sg.Text('Digite Sua Idade')],
    [sg.Input(key=('idade'))],
    [sg.OK(),sg.Cancel(),sg.Button('Enviar dados',key=("enviar_dados")),
    sg.Text(key="acesso",size =(20,1))]
]

#Janela 
Janela = sg.Window('Minha Janela',layout)
#leitura dos valores da tela
while True:
    evento,valores = Janela.Read()
    if evento == sg.WIN_CLOSED:
        break;
    if evento == 'OK':
        print(valores['nome'])
        if int(valores['idade']) >= 18:
            Janela['acesso'].update("Acesso Concedido")
        else:
            Janela['acesso'].update("Acesso Negado")
            Janela['enviar_dados'].update(disabled=True)
            Janela['idade'].update(text_color='red')


Janela.close()
