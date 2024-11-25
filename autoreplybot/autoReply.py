import pyautogui
import pyperclip
import time

pyautogui.click(1070, 1052)
time.sleep(1)

pyautogui.moveTo(679, 260)
pyautogui.dragTo(1835, 900, duration=0.5)

pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

text = pyperclip.paste()

print(text)
