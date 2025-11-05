import pyautogui as py, time
time.sleep(5)
x,y=py.position()
with open("save.txt","w") as save:
    save.write(f"log-in: {x}, {y}")