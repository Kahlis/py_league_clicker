import os.path
import pyautogui
import time

absolute_path = os.path.abspath('assets/accept.png')
accept = True
accept_png = 'assets/accept.png'
deny_png = 'assets/deny.png'

if os.path.exists(absolute_path):
    print('Assets OK')

while True:
    try:
        location = pyautogui.locateOnScreen(accept_png if accept else deny_png, confidence=0.75)
        pyautogui.moveTo(location)
        pyautogui.click()
        print("Match found.")
        break
    except pyautogui.ImageNotFoundException as e:
        time.sleep(3)
