import os.path
import pyautogui
import time

accept = True
accept_png = 'assets/accept.png'
deny_png = 'assets/deny.png'

print("Waiting match...")
while True:
    try:
        location = pyautogui.locateOnScreen(accept_png if accept else deny_png, confidence=0.75)
        pyautogui.moveTo(location)
        pyautogui.click()
        print("Match found.")
        break
    except pyautogui.ImageNotFoundException as e:
        time.sleep(3)
