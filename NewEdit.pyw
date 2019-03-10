from pynput import keyboard
from pynput.keyboard import Key, Controller
from pynput.keyboard import Listener, KeyCode

pressedKey = Controller()
pressed = False

def on_press(key): 
    global pressed

    if pressed == False:
        if key == KeyCode(char='f'):
            pressed = True
            pressedKey.press('p')
            pressedKey.release('p')

def on_release(key):
    global pressed
    if key == KeyCode(char='f'):
        pressedKey.press('p')
        pressedKey.release('p')
        pressed = False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
