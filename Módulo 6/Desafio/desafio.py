from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import base
from models.db_models import Produto
import time
import os
import itertools


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=os.getcwd()+os.sep+'chromedriver.exe', options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException]
        )

    def acessar_site(self):
        self.driver.get('https://cursoautomacao.netlify.app/produtos1.html')

    def coleta_informacoes(self):
        self.nome = self.driver.find_elements_by_xpath(
            (f'//h5[@class="name"]'))

        self.valores = self.driver.find_elements_by_xpath(
            (f'//p[@class="price-container"]'))

        self.descricao = self.driver.find_elements_by_xpath(
            (f'//div[@class="description"]'))

    def proxima_pagina(self):
        try:
            self.wait.until(expected_conditions.element_to_be_clickable(
                (By.ID, "proxima_pagina"))).click()
            # self.driver.find_element_by_link_text("Próxima pagina").click()
            self.pagina()
        except Exception:
            pass

    def configurar_bd(self):
        engine = create_engine('sqlite:///produtos.db', echo=False)
        base.metadata.drop_all(bind=engine)
        base.metadata.create_all(bind=engine)
        Conexao = sessionmaker(bind=engine)
        self.conexao = Conexao()

    def cria_produto(self):
        for indice in range(0, len(self.nome)):
            novo_produto = Produto()
            novo_produto.nome = self.nome[indice].text
            novo_produto.preco = self.valores[indice].text[1:]
            novo_produto.descricao = self.descricao[indice].text
            self.conexao.add(novo_produto)
            self.conexao.commit()

    def pagina(self):
        self.coleta_informacoes()
        self.cria_produto()

    def iniciar(self):
        self.configurar_bd()
        self.acessar_site()
        time.sleep(2)
        self.pagina()
        time.sleep(3)
        self.proxima_pagina()

    def verificar_bd(self):
        for item in self.conexao.query(Produto).all():
            print(
                f'\nID:{item.produto_id}\n Nome:{item.nome}\n Preço:{item.preco}\n Descrição:{item.descricao}\n')


curso = CursoAutomacao()
curso.iniciar()
curso.verificar_bd()
