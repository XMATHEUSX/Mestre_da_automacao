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
        self.email = 'joaopexavier@gmail.com'
        self.senha = "Gabriel3004"

    def Digitando_como_uma_pessoa(self, texto, elemento):
        for letter in texto:
            elemento.send_keys(letter)
            time.sleep(0.1)

    def iniciar(self):
        self.driver.get(
            'https://www.nike.com.br/Snkrs/Produto/Air-Jordan-3/153-169-211-222049')
        time.sleep(4)
        '''
        passar = self.driver.find_element_by_xpath(
            "//button[@id='details-button']")
        passar.click()
        time.sleep(2)
        link = self.driver.find_element_by_xpath(
            "//a[@id='proceed-link']")
        link.click()
        time.sleep(10)
        '''
        login = self.driver.find_element_by_id('anchor-acessar')
        login.click()
        time.sleep(2)
        email = self.driver.find_element_by_xpath(
            "//input[@placeholder='Endereço de e-mail']")
        email.click()
        self.Digitando_como_uma_pessoa(self.email, email)
        time.sleep(1)
        senha = self.driver.find_element_by_xpath(
            "//input[@placeholder='Senha']")
        email.click()
        self.Digitando_como_uma_pessoa(self.senha, senha)
        time.sleep(1)
        continuar = self.driver.find_element_by_xpath(
            "//input[@value='ENTRAR']")
        continuar.click()
        '''
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
'''


curso = CursoAutomacao()
curso.iniciar()
