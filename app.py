import os, pyautogui as py
from time import sleep
#posição x y
with open("save.txt","r") as position:
    cord=position.read().strip()
    x,y = map(int, cord.split(","))
    sleep(5)
    py.click(x,y)

'''py.hotkey("win","r")
py.write("msedge https://saladofuturo.educacao.sp.gov.br/escolha-de-perfil")
py.press("enter")
sleep(4)'''