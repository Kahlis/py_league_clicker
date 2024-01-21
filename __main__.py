import os.path

import pyautogui
import time


absolute_path = os.path.abspath('assets/accept.png')
if os.path.exists(absolute_path):
    print('Assets OK')

try:
    location = pyautogui.locateOnScreen('assets/accept.png', confidence=0.75)
    pyautogui.moveTo(location)
    pyautogui.click()
except pyautogui.ImageNotFoundException as e:
    print(f'Match not found')