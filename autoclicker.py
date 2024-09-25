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
    """
    A class to envelope all methods to do with the AutoClicker.

    Attributes:
        click_position (list): The (x, y) position to click at.
        click_rate (float): The rate of clicks per second.
        clicking (bool): The state of the autoclicker actively clicking.
        running (bool): The state of the autoclicker running.
        click_thread (Thread): The thread for the autoclicker.
    """
    def __init__(self):
        """ Initialises the AutoClicker instance. """
        self.click_position = self.set_click_position()
        self.click_rate = pyautogui.PAUSE = 0.1
        self.clicking = False
        self.running = True
        self.click_thread = None    # Set thread to None while not configured.

        keyboard.add_hotkey('ctrl+shift+f', self.toggle_clicking)
        #keyboard.add_hotkey('ctrl+shift+p', self.set_click_position)

    def autoclick(self):
        """ Automatically clicks the set position using the click_rate. """
        while self.running:
            if self.clicking:
                pyautogui.click(self.click_position)
            else:
                # Sleep if not clicking to prevent high CPU usage
                time.sleep(0.1)

    def toggle_clicking(self):
        """ Toggle the AutoClicker for performing other tasks. """
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
        """ Set the position for the AutoClicker to click. """
        print("Move mouse into position and press Enter.")
        keyboard.wait('enter')
        self.click_position = pyautogui.position()
        print(f"Click position set to: {self.click_position}")

    def kill(self):
        """ Kill the AutoClicker thread. """        
        self.running = False

        if self.click_thread is not None:
            self.click_thread.join()
        
        print("AutoClicker killed.")

    def run(self):
        """ Run the autoclicker until killed. """
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
