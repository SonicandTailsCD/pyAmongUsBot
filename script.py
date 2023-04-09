import pyautogui as pg
import keyboard
import time
import random
locationX = 250
locationY = 750
speed = 2

def setMouseCursorLocation():
    print("Setting Mouse Location...")
    pg.moveTo(locationX, locationY, speed)
def up():
        print("Up")
        pg.mouseDown()
        time.sleep(.5)
        pg.mouseUp()

def up_right():
        print("Up Right")
        pg.mouseDown()
        time.sleep(.5)
        pg.mouseUp()

def up_left():
        print("Up Left")
        pg.mouseDown()
        time.sleep(.5)
        pg.mouseUp()

def left():
        print("left")
        pg.mouseDown()
        time.sleep(.5)
        pg.mouseUp()

def down():
        print("down")
        pg.mouseDown()
        time.sleep(.5)
        pg.mouseUp()

def down_right():
        print("Down Right")
        pg.mouseDown()
        time.sleep(.5)
        pg.mouseUp()

def down_left():
        print("Down Left")
        pg.mouseDown()
        time.sleep(.5)
        pg.mouseUp()

def right():
        print("right")
        pg.mouseDown()
        time.sleep(.5)
        pg.mouseUp()

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