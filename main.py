import pyautogui
import keyboard
import time

while 1:
    pyautogui.move(0, 200)
    pyautogui.move(0, -200)
    time.sleep(1)

    if keyboard.is_pressed('space'):
        quit()