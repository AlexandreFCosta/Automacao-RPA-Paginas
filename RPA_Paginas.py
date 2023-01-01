import pyautogui
import time

pyautogui.alert("O codigo será executado, não mexa em nada no seu computador até o codigo terminar")
pyautogui.PAUSE = 0.5

# Abrir o navegador
pyautogui.press('winleft')
pyautogui.write('Brave')
pyautogui.press('enter')


# Abrir as paginas
pyautogui.write('https://www.youtube.com/')
pyautogui.press('enter')
pyautogui.moveTo(344, 44)
pyautogui.click()
pyautogui.write('https://www.linkedin.com/feed/')
pyautogui.press('enter')
pyautogui.moveTo(647, 42)
pyautogui.click()
pyautogui.write('https://github.com/AlexandreFCosta')
pyautogui.press('enter')


# Esperar 3 segundos
time.sleep(3)

pyautogui.alert("O codigo acabou pode usar o computador novamente")