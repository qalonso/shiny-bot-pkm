import time
from pynput.keyboard import Key, Controller
import numpy as np
import pyautogui
import imutils
import cv2

keyboard = Controller()

key_a = "a"
key_b = Key.space
key_r = "r"
key_p = "p"
key_right = "d"

timeskip = 18


def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)


def press_key_long(key):
    keyboard.press(key)
    time.sleep(0.2)
    keyboard.release(key)
    time.sleep(0.2)


def press_double_key(key1, key2):
    with keyboard.pressed(key2):
        press_key(key1)


# Function for resetting and reloading the game to the save point
def reset_reload():
    press_double_key(key_r, Key.shift)


def leave_title_screen():
    time.sleep(2)
    for i in range(3):
        press_key(key_a)
        time.sleep(1)


def select_pkmn():
    time.sleep(1)
    for i in range(2):
        press_key(key_a)
        time.sleep(1.5)
    for i in range(2):
        press_key(key_right)
        time.sleep(0.5)
    press_key(key_a)


def reset_encounter_starter():
    leave_title_screen()
    time.sleep(2)
    select_pkmn()
    time.sleep(0.5)
    depart = time.time()
    while time.time() - depart < timeskip:
        press_key_long(key_a)


def encounter_pkmn():
    return False


# Returns True if pokemon is shiny
def isShiny(non_shiny):
    press_key(key_p)
    # Taking screenshot and cropping out Giratina from the image
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    x, y, w, h = 190, 650, 20, 20
    # current = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    current = image[y : y + h, x : x + w]
    cv2.imwrite("./screen/current.png", current)
    cv2.imwrite("./screen/in_memory_to_disk.png", image)
    
    # Comparing with a non shiny reference
    if (non_shiny.shape != current.shape):
        # print("Different shapes")
        # print("reference :" + non_shiny.shape)
        # print("current :" + current.shape)
        return False
    
    difference = cv2.subtract(non_shiny, current)
    
    # If there is no difference between the reference and the image, then the encountered pokemon is not shiny
    if not np.any(difference):
        return False
    else:
        return True

    # Capture Screenshot
