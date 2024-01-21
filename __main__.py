import pyautogui
import time

time.sleep(1)
location = pyautogui.locateOnScreen('assets/accept.png')
pyautogui.moveTo(location)
pyautogui.click()