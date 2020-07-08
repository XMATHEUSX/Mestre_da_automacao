import time
import random
import os
import pyautogui
from tqdm import tqdm


class CursoAutomacao:

    def criar_pasta(self):
        for i in tqdm(range(6)):
            time.sleep(1)
        pyautogui.moveTo(175, 130, duration=2)
        pyautogui.dragTo(525, 550, duration=2)
        pyautogui.moveTo(125, 130, duration=2)
        pyautogui.click()
        pyautogui.move(0, 150-130, duration=2)
        pyautogui.click()
        pyautogui.moveTo(175, 130, duration=2)
        pyautogui.dragTo(525, 550, duration=2)
        pyautogui.moveTo(105, 130, duration=2)
        pyautogui.dragTo(280, 150, duration=2)
        pyautogui.dragTo(950, 180, duration=2)


curso = CursoAutomacao()
curso.criar_pasta()
