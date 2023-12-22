import pyautogui as pag
import random
import time

while True:
    x=random.randint(1000,1900)
    y=random.randint(600,1000)
    pag.moveTo(x,y,0.4)
    time.sleep(1)
    