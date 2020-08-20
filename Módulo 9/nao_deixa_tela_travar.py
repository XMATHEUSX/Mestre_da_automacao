import PySimpleGUI as sg
import time
import threading
from selenium import webdriver
import os

# Crie uma função que inicializa a interface
# Crie uma funcão que lida com qualquer tarefa demorada
# A tarefa demorada é executada dentro de uma thread


def OperacaoDemorada(janela, valores):
    driver = webdriver.Chrome(
        executable_path=os.getcwd() + os.sep + 'chromedriver.exe')
    print(f"Navegando para o site {valores['site']}")
    driver.get(valores["site"])
    time.sleep(10)  # Demora de 10 segundos
    site_navegado = driver.current_url
    driver.quit()
    # Crie um evento que exemplifica que a thread foi finalizada e passe qualquer valor(caso necessário), de volta para a tela
    janela.write_event_value('automacao_web_finalizada', site_navegado)


def IniciarInterface():
    # Criamos o layout
    sg.theme('Reddit')

    layout = [
        [sg.Text('Para qual site devemos navegar?')],
        [sg.Input(key='site')],
        [sg.Button('Iniciar'), sg.Button('Parar')],
    ]
    # Criando a janela
    janela = sg.Window('Automatizando TUDO!', layout)
    # Loop de eventos
    thread_automacao_web = None
    while True:
        evento, valores = janela.read()
        if evento in (sg.WIN_CLOSED, 'Exit'):
            break
        elif evento == "Iniciar" and thread_automacao_web == None:
            thread_automacao_web = threading.Thread(target=OperacaoDemorada,
                                                    args=(janela, valores,), daemon=True)
            thread_automacao_web.start()
        elif evento == 'automacao_web_finalizada':
            thread_automacao_web.join()
            thread_automacao_web = None
            print(valores['automacao_web_finalizada'])

    janela.close()


IniciarInterface()
