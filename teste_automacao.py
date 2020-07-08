from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)
        self.email = 'matheusxavier2302@gmail.com'
        self.senha = "TEca@#02"

    def Digitando_como_uma_pessoa(self, texto, elemento):
        for letter in texto:
            elemento.send_keys(letter)
            time.sleep(random.randint(1, 10)/30)

    def iniciar(self):
        self.driver.get('https://amazon.com.br')
        botao_dropdown = self.driver.find_element_by_id('nav-link-accountList')
        botao_dropdown.click()
        email_box = self.driver.find_element_by_xpath(
            "//input[@id='ap_email']")
        self.Digitando_como_uma_pessoa(self.email, email_box)
        btn_continue = self.driver.find_element_by_xpath(
            "//input[@id='continue']")
        btn_continue.click()
        time.sleep(3)
        senha = self.driver.find_element_by_xpath(
            "//input[@id='ap_password']")
        self.Digitando_como_uma_pessoa(self.senha, senha)
        btn_login = self.driver.find_element_by_id('signInSubmit')
        btn_login.click()


curso = CursoAutomacao()
curso.iniciar()
