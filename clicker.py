# -*- coding: utf-8 -*-
"""
Click on keypress

@author: Kalkberg
"""
import time
from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

def keepclicking():
    mouse.click(Button.left, 1)
    time.sleep(.5)

def on_press(key):
    try:
        if format(key.char) == 'w': #single click on w
            mouse.press(Button.left)
            mouse.release(Button.left)
        elif format(key.char) == 'e': #double click on e
            mouse.click(Button.left, 2)
        elif format(key.char) == 'r': #click 5 times with 1.5 sec delay on r
            for i in range(8):
                keepclicking()
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()