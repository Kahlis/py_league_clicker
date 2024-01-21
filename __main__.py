import os.path

import pyautogui
import time

if os.path.exists('/home/kahlis/Documentos/Projects/python/py_league_clicker/assets/accept.png'):
    print('Correct path')

try:
    location = pyautogui.locateOnScreen('assets/accept.png', confidence=0.75)
    pyautogui.moveTo(location)
    pyautogui.click()
except pyautogui.ImageNotFoundException as e:
    print(f'Match not found')