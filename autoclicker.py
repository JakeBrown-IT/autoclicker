# File: autoclicker.py
# Author: Jake Brown
# Created: 25-09-2024
# Purpose: An autoclicker program using 'pyautogui'

# imports
import pyautogui
import keyboard
import time
import threading

# global variables
pyautogui.PAUSE = 0.1   # click interval
clicking = False        # clicking state
running = True          # running state 

### autoclick ###

def autoclick(x, y):
    clicks = 0
    start = time.time()

    while not keyboard.is_pressed('q'):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        clicks += 1

    end = time.time()
    duration = end - start

    print(f"{clicks} clicks in {duration:.3f} seconds."
          .format(clicks, duration))

    return

# we want to run autoclicker in a separate thread to the main program
# so we still have use of the mouse while it is clicking to perform other
# actions in the same window

### spawn thread ###

def spawn_thread():
    x, y = pyautogui.position()
    clicker = threading.Thread(target=autoclick(x, y))
    clicker.daemon = True
    clicker.start()

### main ###

def main():
    print("Move mouse to click location, then press enter...")
    
    keyboard.wait('enter')
    spawn_thread()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
