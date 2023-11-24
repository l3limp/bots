import time
import random
import pyautogui
import keyboard
import win32api as win
import win32con as con

# print(pyautogui.displayMousePosition())

time.sleep(2)

def click(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.004)
    win.mouse_event(con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    
    pic = pyautogui.screenshot(region = (450, 400, 1000, 600))
    flag = False
    
    width, height = pic.size 
    
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            
            r, g, b = pic.getpixel((x, y))
            if g==87 and b==34:
                flag = True
                click(x+450, y+400)
                time.sleep(0.05)
                break
        if flag: 
            break