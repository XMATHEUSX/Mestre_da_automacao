from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=os.getcwd()+os.sep+'chromedriver.exe', options=chrome_options)

            
    def iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app/')


    def encontra_botao_e_clica(self):
            self.checkbox = self.driver.find_element_by_xpath(
            '//input[@id="acessoNivel1Checkbox"]')
            self.driver.execute_script(
            "arguments[0].click()", self.checkbox)


    def verifica_se_botao_foi_selecionado(self):
        if self.checkbox.is_selected():
            print("Botão encontrado")
        else:
            print("Botão não encontrado")


curso = CursoAutomacao()
curso.iniciar()
curso.encontra_botao_e_clica()
curso.verifica_se_botao_foi_selecionado()
