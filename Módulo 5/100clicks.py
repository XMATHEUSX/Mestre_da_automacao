from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import openpyxl
import pyautogui


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--disable-notifications')

        self.driver = webdriver.Chrome(
            executable_path=os.getcwd()+os.sep+'chromedriver.exe', options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException]
        )

    def iniciar(self):
        self.driver.get(
            f'https://cpstest.org/100-seconds.php')
        time.sleep(10)
        self.driver.maximize_window()
        pyautogui.moveTo(637, 436, duration=5)
        pyautogui.scroll(-1400)
        time.sleep(3)
        for click in range(0, 100):
            pyautogui.click()
        self.driver.quit()

    def criar_pasta(self):
        pyautogui.moveTo(1214, 411, duration=5)
        pyautogui.rightClick()
        pyautogui.move(0, (349-411), duration=5)
        pyautogui.move((936-1214), 0, duration=5)
        pyautogui.click()


curso = CursoAutomacao()
curso.iniciar()
curso.criar_pasta()
