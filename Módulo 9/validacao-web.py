import newv as sg
from selenium import webdriver
import os
import threading
import time
from datetime import datetime


class Automator:
    def __init__(self):
        self.licencas_validas = ['h1337xvy', 'X#Fasa', 'SD23r23@!']

    def make_win1(self):
        layout = [[sg.Text('Digite a liçensa do produto'), sg.Input(default_text='h1337xvy', key='licenca')],
                  [sg.Button('Validar'), sg.Button('Sair')]]
        return sg.Window('Primeira Janela', layout, location=(800, 600), finalize=True)

    def make_win2(self):
        layout = [
            [sg.Text('Digite qual tarefa gostaria de automatizar!')],
            [sg.Button('Verificar preços', key='btn_verificar_precos')]
        ]
        return sg.Window('Bem vindo ao seu programa!', layout, finalize=True)

    def extrair_precos(self, window, values, sg):
        driver = webdriver.Chrome(
            executable_path=os.getcwd() + os.sep + 'chromedriver.exe')
        driver.get('https://cursoautomacao.netlify.app/produtos1.html')
        precos = driver.find_elements_by_xpath("//p[@class='price-container']")
        self.lista_precos = []
        for preco in precos:
            self.lista_precos.append(preco.text)
        print('done scrapping, quitting...')
        time.sleep(5)
        driver.quit()

    def processing_shit(self, thread_automacao_Web):
        while thread_automacao_Web.is_alive():
            print(f'{datetime.now()} Trabalhando')
            time.sleep(1)
        print(f'Finalizado: {datetime.now()}')

    def Iniciar(self):
        '''
        Chame aqui as funções para as janelas que deseja abrir, você precisa inicializar ao mínimo uma
        Caso não vá chamar as outras, apenas as defina como "None"
        '''
        window1, window2 = self.make_win1(), None
        thread_automacao_Web = None
        while True:             # Event Loop
            window, event, values = sg.read_all_windows()
            if event == sg.WIN_CLOSED or event == 'Sair':
                window.close()
                if window == window2:       # if closing win 2, mark as closed
                    window2 = None
                elif window == window1:     # if closing win 1, exit program
                    break
            elif event == 'Validar':
                if values['licenca'] in self.licencas_validas:
                    window1.close()
                    window2 = self.make_win2()
                    time.sleep(2)

            elif event == 'btn_verificar_precos' and thread_automacao_Web == None:
                thread_automacao_Web = threading.Thread(
                    target=self.extrair_precos, args=(window, values, sg), daemon=True)
                thread_automacao_Web.start()

            elif event == 'finalizado_automacao_web' and thread_automacao_Web == None:
                thread_automacao_Web.join()
                for preco in self.lista_precos:
                    sg.PopupOK(preco)
                thread = None

        window.close()


automate = Automator()
automate.Iniciar()
