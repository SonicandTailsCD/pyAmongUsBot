#!/usr/bin/env python3

import pyautogui as pg
import keyboard
import time
import random


def up():
        print("Up")
        pg.keyDown("w")
        time.sleep(.5)
        pg.keyUp("w")

def up_right():
        print("Up Right")
        pg.keyDown("w")
        pg.keyDown("d")
        time.sleep(.5)
        pg.keyUp("w")
        pg.keyUp("d")

def up_left():
        print("Up Left")
        pg.keyDown("w")
        pg.keyDown("a")
        time.sleep(.5)
        pg.keyUp("w")
        pg.keyUp("a")

def left():
        print("left")
        pg.keyDown("a")
        time.sleep(.5)
        pg.keyUp("a")

def down():
        print("down")
        pg.keyDown("s")
        time.sleep(.5)
        pg.keyUp("s")

def down_right():
        print("Down Right")
        pg.keyDown("s")
        pg.keyDown("d")
        time.sleep(.5)
        pg.keyUp("s")
        pg.keyUp("d")

def down_left():
        print("Down Left")
        pg.keyDown("s")
        pg.keyDown("a")
        time.sleep(.5)
        pg.keyUp("s")
        pg.keyUp("a")

def right():
        print("right")
        pg.keyDown("d")
        time.sleep(.5)
        pg.keyUp("d")

all_keys = [up, up_right, up_left, left, down, down_right, down_left, right]
horizontal_keys = [left, right]
vertical_keys = [up, up_right, up_left, down, down_right, down_left]
# random.choice(keys)()

characters = [r"Images\\character_colors\\character_black_left.png", r"Images\\character_colors\\character_black_right.png"]


while keyboard.is_pressed('q') == False:

        #Screen Area 1 (Top left of screen)
        if pg.locateOnScreen(characters[0], region=(0,0,908,485), grayscale=True, confidence=0.5) or pg.locateOnScreen(characters[1], region=(0,0,908,485), grayscale=True, confidence=0.5) != None:
                print("Screen Area 1")
                up_left()
                time.sleep(0.5)

        #Screen Area 2 (Top middle of screen)
        elif pg.locateOnScreen(characters[0], region=(900,0,125,454), grayscale=True, confidence=0.5) or pg.locateOnScreen(characters[1], region=(900,0,125,454), grayscale=True, confidence=0.5) != None:
                print("Screen Area 2")
                up()
                time.sleep(0.5)

        # Screen Area 3 (Top right of screen)
        elif pg.locateOnScreen(characters[0], region=(1000,0,908,485), grayscale=True, confidence=0.5) or pg.locateOnScreen(characters[1], region=(1000,0,908,485), grayscale=True, confidence=0.5) != None:
                print("Screen Area 3")
                up_right()
                time.sleep(0.5)

        # Screen Area 4 (Left side Middle)
        elif pg.locateOnScreen(characters[0], region=(0,450,908,160), grayscale=True, confidence=0.5) or pg.locateOnScreen(characters[1], region=(0,450,908,160), grayscale=True, confidence=0.5) != None:
                print("Screen Area 4")
                left()
                time.sleep(0.5)

        # Screen Area 5 (Right side Middle)
        elif pg.locateOnScreen(characters[0], region=(1012,450,908,160), grayscale=True, confidence=0.5) or pg.locateOnScreen(characters[1], region=(1012,450,908,160), grayscale=True, confidence=0.5) != None:
                print("Screen Area 5")
                right()
                time.sleep(0.5)

        # Screen Area 6 (Bottom left side)
        elif pg.locateOnScreen(characters[0], region=(0,580,908,500), grayscale=True, confidence=0.5) or pg.locateOnScreen(characters[1], region=(0,580,908,500), grayscale=True, confidence=0.5) != None:
                print("Screen Area 6")
                down_left()
                time.sleep(0.5)
        
        # Screen Area 7 (Bottom middle)
        elif pg.locateOnScreen(characters[0], region=(900,580,125,500), grayscale=True, confidence=0.5) or pg.locateOnScreen(characters[1], region=(900,580,125,500), grayscale=True, confidence=0.5) != None:
                print("Screen Area 7")
                down()
                time.sleep(0.5)

        # Screen Area 8 (Bottom right side)
        elif pg.locateOnScreen(characters[0], region=(1000,580,908,500), grayscale=True, confidence=0.5) or pg.locateOnScreen(characters[1], region=(1000,580,908,500), grayscale=True, confidence=0.5) != None:
                print("Screen Area 8")
                down_right()
                time.sleep(0.5)

        else:
                print("Doing Random Moves")
                random.choice(horizontal_keys)()
                random.choice(vertical_keys)()
                time.sleep(0.5)
