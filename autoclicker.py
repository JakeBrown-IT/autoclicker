# File: autoclicker.py
# Author: Jake Brown
# Created: 25-09-2024
# Purpose: AutoClicker program using threads and 'pyautogui'

# Imports
import pyautogui
import keyboard
import time
import threading

# AutoClicker Class
class AutoClicker:
    def __init__(self):
        self.click_position = self.set_click_position()
        self.click_rate = pyautogui.PAUSE = 0.1
        self.clicking = False
        self.running = True
        self.click_thread = None    # Initialise thread to None

        keyboard.add_hotkey('ctrl+shift+f', self.toggle_clicking)
        #keyboard.add_hotkey('ctrl+shift+p', self.set_click_position)

    def autoclick(self):
        while self.running:
            if self.clicking:
                pyautogui.click(self.click_position)
            else:
                # Sleep if not clicking to prevent high CPU usage
                time.sleep(0.1)

    def toggle_clicking(self):
        if not self.clicking:
            self.clicking = True

            print("AutoClicker started.")

            if self.click_thread is None:
                self.click_thread = threading.Thread(target=self.autoclick)
                self.click_thread.daemon = True
                self.click_thread.start()

        else:
            self.clicking = False
            print("AutoClicker stopped.")

    def set_click_position(self):
        print("Move mouse into position and press Enter.")
        keyboard.wait('enter')
        self.click_position = pyautogui.position()
        print(f"Click position set to: {self.click_position}")

    def kill(self):        
        self.running = False

        if self.click_thread is not None:
            self.click_thread.join()
        
        print("AutoClicker killed.")



    def run(self):
        print("Press '<C-F>' to toggle the AutoClicker on/off.")
        #print("Press '<C-P>' to set the click position.")
        print("Press '<C-c>' to exit.")
        
        try:
            keyboard.wait()

        except KeyboardInterrupt:
            self.kill()
            exit()
            

if __name__ == "__main__":
    autoclicker = AutoClicker()
    autoclicker.run()






    








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

    print(f"{clicks} clicks in {duration:.3f} seconds."
          .format(clicks, duration))

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
