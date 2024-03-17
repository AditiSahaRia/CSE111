#install pyautogui in the terminal
import pyautogui
import time
string = input()
time.sleep(5)
for i in string:
    pyautogui.typewrite(i)
    pyautogui.press('enter')