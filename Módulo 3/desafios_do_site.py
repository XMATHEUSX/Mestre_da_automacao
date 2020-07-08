from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import random
import os


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        i = 0
        self.driver = webdriver.Chrome(
            executable_path=os.getcwd()+os.sep+'chromedriver.exe', options=chrome_options)
        self.texto = 'Observo a noite fria e chuvosa'

    def iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app/desafios.html')
        self.screenshot()

    def Digitando_como_uma_pessoa(self, texto, elemento):
        for letter in texto:
            elemento.send_keys(letter)
            time.sleep(random.randint(1, 10)/30)

    def screenshot(self):
        nome_arquivo = str(round(time.time()*1000)) + ".png"
        nome_arquivo_com_diretorio = os.path.join("fotos", nome_arquivo)
        self.driver.save_screenshot(nome_arquivo_com_diretorio)

    def movimentando_a_página(self):
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight);')
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollTop);')

        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.execute_script('window.scrollBy(1000,0)')

    def desafio1(self):
        desafio1_btn1 = self.driver.find_element_by_id('btn1')
        desafio1_btn2 = self.driver.find_element_by_class_name('btn2')
        desafio1_btn3 = self.driver.find_element_by_xpath(
            '//*[text()="Botão 3"]')
        if desafio1_btn1.is_enabled():
            print("Botão 1 Habilitado")
        if desafio1_btn1.is_enabled() == False:
            print("Botão 1 Desabilitado")
        if desafio1_btn2.is_enabled():
            print("Botão 2 Habilitado")
        if desafio1_btn2.is_enabled() == False:
            print("Botão 2 Desabilitado")
        if desafio1_btn3.is_enabled():
            print("Botão 3 Habilitado")
        if desafio1_btn3.is_enabled() == False:
            print("Botão 3 Desabilitado")

    def desafio2(self):
        text_box_1 = self.driver.find_element_by_id("dadosusuario")
        text_box_1.click()
        text_box_1.send_keys('matheusxavier2302@gmail.com')
        time.sleep(5)

        btn_1 = self.driver.find_element_by_xpath(
            "//button[@id='desafio2']")
        self.driver.execute_script("arguments[0].click()", btn_1)
        time.sleep(5)

        text_box_2 = self.driver.find_element_by_id("escondido")
        self.driver.execute_script("arguments[0].click()", text_box_2)
        text_box_2.send_keys('matheusxavier2302@gmail.com')
        time.sleep(5)

        btn_2 = self.driver.find_element_by_xpath(
            "//button[@id='validarDesafio2']")
        self.driver.execute_script("arguments[0].click()", btn_2)
        time.sleep(5)

        # desafio2_btn.click()
        # self.driver.execute_script("arguments[0].click(),desafio2_btn")

    def desafio3(self):
        Checkbox_1 = self.driver.find_element_by_xpath(
            "//input[@onclick='activateSucessCheckbox1()']")
        # Checkbox_1.click()
        self.driver.execute_script("arguments[0].click()", Checkbox_1)

        Checkbox_2 = self.driver.find_element_by_id("offroadcheckbox")
        # Checkbox_2.click()
        self.driver.execute_script("arguments[0].click()", Checkbox_2)

    def desafio4(self):
        text_box = self.driver.find_element_by_id("campoparagrafo")
        self.Digitando_como_uma_pessoa(self.texto, text_box)
        btn = self.driver.find_element_by_xpath(
            "//button[@onclick='ValidarDesafio4()']")
        self.driver.execute_script("arguments[0].click()", btn)

    def desafio5(self):
        try:
            i = 0
            Checkboxes = self.driver.find_elements_by_xpath(
                '//section[@class="jumbotron desafios5"]//input[@id="conversivelcheckbox"]')
            for Checkbox in Checkboxes:
                if Checkbox.is_selected() == False and i != 0 and i != 2:
                    self.driver.execute_script(
                        "arguments[0].click()", Checkbox)
                i = i + 1
            cidades = self.driver.find_elements_by_class_name(
                'form-control.cidadesinput')
            for cidade in cidades:
                self.driver.execute_script("arguments[0].click()", cidade)
                cidade.send_keys("Jundiaí")
            btns = self.driver.find_elements_by_class_name("btn.btn-warning")
            for btn in btns:
                self.driver.execute_script("arguments[0].click()", btn)
        except Exception:
            self.desafio5()

    def desafio6(self):
        pais = self.driver.find_element_by_xpath(
            "//select[@id='paisesselect']")
        opcoes = Select(pais)
        opcoes.select_by_visible_text("Estados Unidos")
        opcoes.select_by_visible_text("Africa")
        opcoes.select_by_visible_text("Chille")

    def sair(self):
        self.driver.quit()
