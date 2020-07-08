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
        botao_dropdown = self.driver.find_element_by_xpath()
        if botao_dropdown is not None:
            print("Botão encontrado")
        if botao_dropdown is None:
            print("Botão não encontrado")


curso = CursoAutomacao()
curso.iniciar()

