import pyautogui

import pyperclip


class CursoAutomacao:

    def escrevendo(self):
        pyautogui.moveTo(965, 277, duration=2)
        pyautogui.click()
        pyautogui.typewrite("Mestres Da Automação")

    def copiar_frases_com_caracteres_especiais(self, frase):
        pyperclip.copy(frase)
        pyautogui.hotkey('ctrl', 'v')


curso = CursoAutomacao()
curso.escrevendo()
curso.copiar_frases_com_caracteres_especiais("\nMestres Da Automação")
