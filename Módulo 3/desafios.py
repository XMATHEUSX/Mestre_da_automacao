from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    def iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.app/')
        desafio1 = self.driver.find_element_by_xpath(
            '//*[text()="Parágrafo"]')
        desafio2 = self.driver.find_elements_by_xpath(
            '//*[contains(text(),"Dropdown") or contains( text(), "Clássico" )]')
        desafio3 = self.driver.find_element_by_xpath(
            '//*[contains(text(),"Elementos") and contains( text(), "botões" )]')
        desafio4 = self.driver.find_element_by_xpath(
            '//*[contains(text(),"Exemplo abrir Nova Janela")]')
        desafio5 = self.driver.find_element_by_id(
            'divBotao')
        desafio6 = self.driver.find_elements_by_class_name(
            'form-control')
            #
        if desafio6 is not None:
            print("Botão encontrado")
        if desafio6 is None:
            print("Botão não encontrado")
        print(desafio6)


curso = CursoAutomacao()
curso.iniciar()
