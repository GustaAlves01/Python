import os, pyautogui as py
from time import sleep
#posição x y

with open("ra.txt","r") as log:
    dados=(log.read().strip().split(","))


def Entrar():
    py.hotkey("win","r")
    py.write("msedge -inprivate https://saladofuturo.educacao.sp.gov.br/escolha-de-perfil")
    py.press("enter")

def Logar():
    with open("save.txt","r") as position:
        x,y=map(int, position.read().strip().split(","))
    sleep(3)
    for _ in range(2):
        py.click(x,y)
    sleep(0,5)
    for i in dados:
        py.write(i)
        py.press("tab")
        sleep(0,5)
    py.press("enter")
     

Entrar()
sleep(3)
Logar()