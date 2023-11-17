import time
from pynput.keyboard import Key, Controller
import functions as fn
import screenshooter as sc
import cv2
import pygetwindow as gw

# fenetre = gw.getWindowsWithTitle('DeSmuME 0.9.11 x64 SSE2 | Pokémon Platine')
# print(fenetre)
# fenetre.activate()
non_shiny = cv2.imread("./screen/reference.png")
key_p = "p"
keyboard = Controller()
c = 0

fn.press_double_key(Key.tab, Key.alt)

with keyboard.pressed(Key.tab):
    fn.reset_reload()
    time.sleep(0.75)
    while True:
        fn.reset_encounter_starter()
        time.sleep(1)
        fn.press_double_key(key_p, Key.shift)
        time.sleep(1)
        if(fn.isShiny(non_shiny)):
            #Code when shiny pokemon is encountered
            print("Shiny pokemon encountered after ",c+1,"encounters")
            break
        c+=1
        print("Not Shiny, Encounter: ",c)
        fn.press_double_key(key_p, Key.shift)
        fn.reset_reload()
        time.sleep(0.5)
