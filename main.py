import pyautogui as py
import time
import keyboard
import win32api
import win32con
import threading

# RGB is is (17, 17, 17)
# Only need one color as they are all the same.
R = 17

# Position of each tile when on second monitor
TILE_LEFT = [2721, 684]
TILE_LEFT_MID = [2821, 684]
TILE_RIGHT_MID = [2922, 684]
TILE_RIGHT = [3021, 684]


# Found this code for a faster click on https://github.com/KianBrose/Image-Recognition-Botting-Tutorial
# This was needed as pyautogui's click is slower
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Reports where mouse position a number of times determined by the parameter.
def display_mouse_position(duration):
    for i in range(0, duration):
        print(py.position())
        time.sleep(1)


# Shows location + the pixel color in RGB at the given location
def display_mouse_pixel_color(duration):
    for i in range(0, duration):
        point = py.position()
        print(point, py.pixel(point[0], point[1]))
        time.sleep(1)


# Positions are relative to one of my monitors. These will need to be changed for your use.
def tile1():
    while not keyboard.is_pressed('esc'):
        if py.pixel(2721, 684)[0] == R:
            print("t1")
            click(2721, 684)


def tile2():
    while not keyboard.is_pressed('esc'):
        if py.pixel(2821, 684)[0] == R:
            print("t2")
            click(2821, 684)


def tile3():
    while not keyboard.is_pressed('esc'):
        if py.pixel(2922, 684)[0] == R:
            print("t3")
            click(2922, 684)


def tile4():
    while not keyboard.is_pressed('esc'):
        if py.pixel(3021, 684)[0] == R:
            print("t4")
            click(3021, 684)


# Each row get a thread that watches for a clickable tile.
if __name__ == '__main__':
    py.FAILSAFE = True
    print("Countdown", end=' ')
    py.countdown(5)
    t1 = threading.Thread(target=tile1)
    t2 = threading.Thread(target=tile2)
    t3 = threading.Thread(target=tile3)
    t4 = threading.Thread(target=tile4)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

# if py.pixel(TILE_LEFT[0], TILE_LEFT[1])[0] == R:
#     click(TILE_LEFT[0], TILE_LEFT[1])
# if py.pixel(TILE_LEFT_MID[0], TILE_LEFT_MID[1])[0] == R:
#     click(TILE_LEFT_MID[0], TILE_LEFT_MID[1])
# if py.pixel(TILE_RIGHT_MID[0], TILE_RIGHT_MID[1])[0] == R:
#     click(TILE_RIGHT_MID[0], TILE_RIGHT_MID[1])
# if py.pixel(TILE_RIGHT[0], TILE_RIGHT[1])[0] == R:
#     click(TILE_RIGHT[0], TILE_RIGHT[1])
