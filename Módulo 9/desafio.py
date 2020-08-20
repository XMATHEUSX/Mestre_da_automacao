import PySimpleGUI as sg

usuarios = [
    {
        'usuario': 'matheus',
        'senha': '1234'

    },
    {
        'usuario': 'joao',
        'senha': '7890'

    }
]
licenca = ['ALOI', 'ASDF', 'GHJK']


# Layout
def criar_janela1():
    Janela1 = [
        [sg.Text('Digite Seu usuario', size=(35, 1))],
        [sg.Input(key=('usuario'), size=(35, 10))],
        [sg.Text('Digite Sua Senha', size=(35, 1))],
        [sg.Input(key=('senha'), size=(35, 15))],
        [sg.Text(key="acesso_login", size=(20, 1))],
        [sg.Button("Login"), sg.Button("Sair")]
    ]
    return sg.Window('Janela', layout, finalize=True)


def criar_janela2():
    Janela2 = [
        [sg.Text('Digite Sua Licença para continuar', size=(35, 1))],
        [sg.Input(key=('licenca'), size=(35, 10))],
        [sg.Text(key="valida", size=(20, 1))],
        [sg.Button("Validar licença")]
    ]


# def criar_janela3():
coluna_1 = [
    [sg.Text('Qual site gostaria de automatizar ?')],
    [sg.Radio('Site 1', group_id='Sites'),
     sg.Radio('Site 2', group_id='Sites'),
     sg.Radio('Site 3', group_id='Sites')],
    [sg.Checkbox('Opção 1', key='Google'), sg.Checkbox(
        'Opção 2', key='Yahoo'), sg.Checkbox('Opção 3 ', key='Bing')],
    [sg.Text('Quantas Dias o programa ira rodar?')],
    [sg.Slider(key='qtd', range=(1, 14), orientation='h',
               size=(34, 20), default_value=1)]
]
coluna_2 = [
    [sg.Multiline(autoscroll=True, size=(30, 5),
                  default_text='Digite a mensagem a ser enviada aqui')],
    [sg.Text('Quantas mensagens por dia')],
    [sg.Combo(values=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
              default_value=2)],
    [sg.Text('Qual é o Perfil da Sua conta')],
    [sg.Combo(values=["Bronze", "Prata", "Ouro", 'Diamante'],
              default_value="Bronze")],
    [sg.Text('Quantos Sites Processar por dia ?')],
    [sg.Spin(values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
             initial_value=1, key='velocidade_de_envio_msg')],
]
janela3 = [[sg.Frame("Configurações Inicial", (coluna_1)),
            sg.Frame("Configurações Mensagem", (coluna_2))],
           [sg.OK("Iniciar")]]


# Janela
Janela = sg.Window('Opção de valores', janela3)
# leitura dos valores da tela
while True:
    evento, dados = Janela.Read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Login':
        for usuario in usuarios:
            if usuario['usuario'] == dados['usuario']:
                if usuario['senha'] == dados['senha']:
                    Janela['acesso_login'].update("")
                    sg.popup('login Correto', auto_close_duration=8)
                    break
            print(usuarios)
            # if dados['nome'] in usuarios
        else:
            Janela['acesso_login'].update("Login Inválido")
            Janela['acesso_login'].update(text_color='red')
    if evento == 'Validar licença':
        if dados['licenca'] in licenca:
            Janela['valida'].update("")
            sg.popup('Licença Validada Com Sucesso', auto_close_duration=8)
        else:
            Janela['valida'].update("Licença Inválida")
            Janela['valida'].update(text_color='red')
    if evento == 'Iniciar':
            print("OLa")
    if evento == 'Sair':
        Janela.close()


Janela.close()
