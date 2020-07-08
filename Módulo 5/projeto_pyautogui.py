import webbrowser
import pyautogui
import time

# firefox
# webbrowser.open('https://cursoautomacao.netlify.app/')
# time.sleep(15)
# pyautogui.moveTo(750, 350, 2)
# time.sleep(1)
# pyautogui.scroll(-3200)
# pyautogui.moveTo(1045, 594, 2)
# pyautogui.click()
# pyautogui.typewrite('Matheus Henrique Xavier')
# pyautogui.screenshot('Desafio.jpg')
# time.sleep(2)
# pyautogui.scroll(3200)
# pyautogui.moveTo(42, 286, 2)
# pyautogui.click()
# time.sleep(2)
# pyautogui.scroll(-5000)
# pyautogui.scroll(-5000)
# pyautogui.scroll(-1250)
# x = [189,393,564,725,949,1119]
# y = [543,548,560,571,553,553]
# for num in range(0,len(x)):
#     pyautogui.moveTo(x =x[num] , y = y[num] , duration = 2)
#     pyautogui.click()
#     time.sleep(8)
# pyautogui.alert("Terminou", "Automção Finalizada")

# google
# webbrowser.open('https://cursoautomacao.netlify.app/')
time.sleep(5)
pyautogui.moveTo(750, 350, 2)
time.sleep(1)
pyautogui.scroll(-1650)
pyautogui.moveTo(1045, 594, 2)
pyautogui.click()
pyautogui.typewrite('Matheus Henrique Xavier')
pyautogui.screenshot('Desafio.jpg')
time.sleep(2)
pyautogui.scroll(1650)
pyautogui.moveTo(40, 310, 2)
pyautogui.click()
time.sleep(2)
pyautogui.scroll(-5250)
x = [198, 398, 553, 769, 942, 1141]
y = [540, 542, 539, 569, 538, 567]
for num in range(0, len(x)):
    pyautogui.moveTo(x=x[num], y=y[num], duration=2)
    pyautogui.click()
    time.sleep(5)
pyautogui.alert("Terminou", "Automção Finalizada")
