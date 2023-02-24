from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

Y = 400 # mouse position for Y

X1 = 439 # mouse position of tile 1
X2 = 498 # mouse position of tile 1
X3 = 555 # mouse position of tile 1
X4 = 611 # mouse position of tile 1


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pause for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def start():
    while keyboard.is_pressed('q') == False:

        if pyautogui.pixel(X1, Y)[0] == 0:
            click(X1, Y)
        if pyautogui.pixel(X2, Y)[0] == 0:
            click(X2, Y)
        if pyautogui.pixel(X3, Y)[0] == 0:
            click(X3, Y)
        if pyautogui.pixel(X4, Y)[0] == 0:
            click(X4, Y)

#qtime.sleep(5) 
start()
