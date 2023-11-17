import time
import numpy as np
import pyautogui
from pynput.keyboard import Key, Controller
import imutils
import cv2
import functions as fn

keyboard = Controller()

def take_screen():
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    time.sleep(2.5)
    
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    x, y, w, h = 190, 650, 20, 20
    cropped = image[y : y + h, x : x + w]
    cv2.imwrite("./shiny-bot-pokemon/screen/in_memory_to_disk2.png", image)
    cv2.imwrite("./shiny-bot-pokemon/screen/reference.png", cropped)


if (__name__ == "__main__"):
    take_screen()
