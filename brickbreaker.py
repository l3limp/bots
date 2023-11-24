import time
import random
import pyautogui
import keyboard
import win32api as win
import win32con as con
from PIL import Image


# print(pyautogui.qdisplayMousePosition())
img = Image.open(r'C:\Users\vardaan\OneDrive\Desktop\ps\hehe\ball.png')

while keyboard.is_pressed('q') == False:
    loc = pyautogui.locateOnScreen(img, confidence=0.8, grayscale=True, region=(400, 125, 300, 450))
    win.SetCursorPos((loc.left+5, 300))
    