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
    sleep(0.5)
    
    for i in dados[:-1]:
        py.write(i)
        py.press("tab")
        sleep(0.5)
    for _ in range(2):
        py.press("tab")
    py.write(dados[2])
    sleep(0.5)
    py.press("enter")
    sleep(7)
    py.click(x=812, y=291)
    sleep(0.5)
    py.scroll(-250)
    sleep(1)
    py.click(x=375,y=602)
    sleep(3)
    py.click(x=585, y=229)  
    py.click(x=585, y=315)  
     

Entrar()
sleep(3)
Logar()