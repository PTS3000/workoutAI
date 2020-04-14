import winsound
import random
import time
import pyautogui

pyautogui.hotkey("win", "s")
time.sleep(2)
pyautogui.press("k")
pyautogui.press("a")
pyautogui.press("u")
pyautogui.press("n")
pyautogui.press("a")
time.sleep(1)
pyautogui.press("enter")

time.sleep(4)

winsound.PlaySound("ola", winsound.SND_FILENAME)

ligado = 1
while ligado == 1: 
    falas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    fala = random.choice(falas)
    musica = random.randint(1,8)
    
    print("o johnny sins vai dizer a fala nº " + fala)
    if musica == 8:
        print("o johny vai cantar")
        winsound.PlaySound("intro", winsound.SND_FILENAME)
        winsound.PlaySound("iwantit", winsound.SND_FILENAME)
    else:
        espera = random.randint(5,10)
        print(" o johny sins vai esperar " + str(espera) + " segundos")

        winsound.PlaySound(fala, winsound.SND_FILENAME)

        time.sleep(espera)

