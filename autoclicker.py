# File: autoclicker.py
# Author: Jake Brown
# Created: 25-09-2024
# Purpose: An autoclicker program using 'pyautogui'

# the loop will start when the user enters the l key
# at this point, the program captures the position of the cursor
# it locks this position in, and 
# the loop will autoclick at 10 clicks per second
# 

# imports
import pyautogui
import keyboard

# set click interval to 0.1 second (10 clicks per second)
interval = 0.1
pyautogui.PAUSE = interval 

def autoclick(x, y):
    print(f"[log] locked mouse position at ({x}, {y})...".format(x, y))
    print(f"[log] starting autoclicks at {interval}s...".format(interval))

    while not keyboard.is_pressed('q'):
        pyautogui.moveTo(x, y)
        pyautogui.click()

    # print 
    print("[log] 'q' pressed, quitting...")

    exit()

def main():
    print("[log] autoclicker launched...")
    print("[log] waiting for 'l' keypress...")
    
    while True:
        if keyboard.is_pressed('l'):
            x, y = pyautogui.position()

            autoclick(x, y)
            break

    return


if __name__ == "__main__":
    main()
