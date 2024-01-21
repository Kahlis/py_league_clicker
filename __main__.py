import pyautogui
import time

time.sleep(1)
location = pyautogui.locateOnScreen('example.png')
print(location)