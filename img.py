import pyautogui

loc = pyautogui.locateAllOnScreen(r'C:\Users\vardaan\OneDrive\Desktop\ps\hehe\p.png', confidence=0.99)
for tp in loc:
    print(tp)
# print(loc)