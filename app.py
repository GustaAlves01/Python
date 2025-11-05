import os, pyautogui as py
from time import sleep
#posição x y

with open ("ra.txt","r") as ra:
    ra = ra.read().strip


def Entrar():
    py.hotkey("win","r")
    py.write("msedge -inprivate https://saladofuturo.educacao.sp.gov.br/escolha-de-perfil")
    py.press("enter")

def Logar():
    with open("save.txt","r") as position:
        cord=position.read().strip()
    x,y = map(int, cord.split(","))
    sleep(4)

Logar()
sleep(3)
Entrar()