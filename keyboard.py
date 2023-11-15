import time
from pynput.keyboard import Key, Controller
import functions as fn
import cv2

non_shiny = cv2.imread('shiny-bot-pokemon/screen/reference.png')
keyboard = Controller()
c = 0

#Switching tabs and getting to Desmume
with keyboard.pressed(Key.alt):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

with keyboard.pressed(Key.tab):
    fn.reset_reload()
    time.sleep(2)
    while True:
        fn.encounter_pkmn()
        time.sleep(3)
        if(fn.isShiny(non_shiny)):
            #Code when shiny pokemon is encountered
            keyboard.press('p')
            time.sleep(1)
            keyboard.release('p')
            print("Shiny pokemon encountered after ",c+1,"encounters")
            break
        c+=1
        print("Not Shiny, Encounter: ",c)
        fn.reset_reload()
        time.sleep(0.5)
