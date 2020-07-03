from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time
import random


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException]
        )

    def Digitando_como_uma_pessoa(self, texto, elemento):
        for letter in texto:
            elemento.send_keys(letter)
            time.sleep(random.randint(1, 10)/30)

    def escolha_os(self):
        try:
            os = input("Qual Sistema Operacional deseja selecionar ?")

            btn_radio = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH,f'//input[@value="{os}"]')))
            
            self.driver.execute_script("arguments[0].click()", btn_radio)

        except Exception:
                print("Opção inválida!!!\nOpções Válidas:\nMac\nWindows 10\nLinux\n")
                self.escolha_os()
        

    def comentario(self):
        try:
            self.texto = input("Qual Comentário gostaria de deixar ?")
            text_box = '//textarea[@placeholder="digite seu texto aqui"]'
            self.text_box = self.wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, text_box)))
            self.driver.execute_script("arguments[0].click()", self.text_box)
        except Exception:
            print("Ocorreu um erro. Tente Novamente")
            self.comentario()

    def niveis_acesso(self):
        try:
            acessos = input(
                "Quais níveis devem ser liberados?(Digite os valores separados por vírgula):")
            acessos = acessos.split(",")
            for acesso in acessos:
                time.sleep(3)
                os = f'//input[@id="acessoNivel{acesso}Checkbox"]'
                btn_radio = self.wait.until(expected_conditions.element_to_be_clickable(
                    (By.XPATH, os)))
                if btn_radio.is_selected() == False:
                    self.driver.execute_script(
                        "arguments[0].click()", btn_radio)
        except Exception:
            print('Ocorreu um erro digite o nivel de acesso entre virgula.')
            self.niveis_acesso()

    def iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app/')
        time.sleep(1)
        self.escolha_os()
        time.sleep(2)
        self.comentario()
        self.Digitando_como_uma_pessoa(self.texto, self.text_box)
        time.sleep(2)
        self.niveis_acesso()


curso = CursoAutomacao()
curso.iniciar()
