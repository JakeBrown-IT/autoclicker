# File: autoclicker.py
# Author: Jake Brown
# Created: 25-09-2024
# Purpose: An autoclicker program using 'pyautogui'

# imports
import pyautogui
import keyboard
import time

# set click interval to 0.1 second (10 clicks per second)
interval = 0.1
pyautogui.PAUSE = interval 

def autoclick(x, y):
    clicks = 0
    start = time.time()

    while not keyboard.is_pressed('q'):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        clicks += 1

    end = time.time()
    duration = end - start

    print(f"{clicks} clicks in {duration} seconds."
          .format(duration, clicks))

    return

def main():
    while True:
        if keyboard.is_pressed('l'):
            x, y = pyautogui.position()
            autoclick(x, y)
            break

    return


if __name__ == "__main__":
    main()
