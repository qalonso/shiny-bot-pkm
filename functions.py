import time
from pynput.keyboard import Key, Controller
import numpy as np
import pyautogui
import imutils
import cv2

key_a = 'a'
key_b = Key.space
key_r = 'r'
key_right = 'd'

timeskip = 18

def press_key(key):
    keyboard = Controller()
    keyboard.press(key)
    time.sleep(0.5)
    keyboard.release(key)

def press_key_long(key):
    keyboard = Controller()
    keyboard.press(key)
    time.sleep(0.5)
    keyboard.release(key)
    time.sleep(0.1)

def press_double_key(key1, key2):
    keyboard = Controller()
    keyboard.press(key1)
    keyboard.press(key2)
    time.sleep(0.25)
    keyboard.release(key1)
    keyboard.release(key2)

#Function for resetting and reloading the game to the save point
def reset_reload():
    press_double_key(key_r, Key.shift)

def leave_title_screen():
    time.sleep(2)
    press_key(key_a)
    time.sleep(0.5)
    press_key(key_a)
    time.sleep(0.5)
    press_key(key_a)

def select_pkmn():
    press_key(key_a)
    time.sleep(1)
    press_key(key_a)
    time.sleep(0.1)
    press_key(key_right)
    time.sleep(0.1)
    press_key(key_right)
    time.sleep(0.1)
    press_key(key_a)
    time.sleep(0.1)
    press_key(key_a)

def encounter_pkmn():
    leave_title_screen()
    time.sleep(1)
    select_pkmn()
    time.sleep(0.5)
    depart = time.time()
    while time.time() - depart < timeskip:
        press_key_long(key_a)

#Returns True if pokemon is shiny
def isShiny(non_shiny):
    #Taking screenshot and cropping out Giratina from the image
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # image = imutils.resize(image, width=600)
    current = image[145:563,345:738]
    current = imutils.resize(current, width=600)

    non_shiny = imutils.resize(non_shiny, width=600)
    #Comparing with a non shiny reference
    difference = cv2.subtract(non_shiny, current)
    #If there is no difference between the reference and the image, then the encountered pokemon is not shiny
    if(not np.any(difference)):
        return(False)
    else:
        return(True)



    #Capture Screenshot
