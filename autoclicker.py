import time
import random
import pyautogui
import keyboard
import win32api as win
import win32con as con

def click(x, y):
    win.SetCursorPos((x, y))
    win.mouse_event(con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.006)
    win.mouse_event(con.MOUSEEVENTF_LEFTUP, 0, 0)
    
while keyboard.is_pressed('q') == False: 
    if pyautogui.pixel(624, 500)[0] == 0:
        click(624, 500)
    if pyautogui.pixel(720, 500)[0] == 0:
        click(720, 500)
    if pyautogui.pixel(808, 500)[0] == 0:
        click(808, 500)
    if pyautogui.pixel(890, 500)[0] == 0:
        click(890, 500)