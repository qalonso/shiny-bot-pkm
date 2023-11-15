import numpy as np
import pyautogui
from pynput.keyboard import Key, Controller
import imutils
import cv2
import functions as fn

keyboard = Controller()

with keyboard.pressed(Key.alt):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("./shiny-bot-pokemon/screen/in_memory_to_disk2.png", image)