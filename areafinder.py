#!/usr/bin/env python3

import pyautogui as pg

# im = pg.screenshot(region=(600,635,720,150)) #local and online
# im = pg.screenshot(region=(965,635,355,150)) #online only
# im = pg.screenshot(region=(782,650,360,100)) #find public game
# im = pg.screenshot(region=(435, 335, 1050, 650)) #public game search
# im = pg.screenshot(region=(1480, 335, 135, 135)) # public game refresh X: 1550  Y: 400
# im = pg.screenshot(region=(782,350,360,100)) #Create Game Online
# im = pg.screenshot(region=(1600, 965, 280, 80)) #Confirm Host Game
# im = pg.screenshot(region=(590, 946, 200, 70)) # switch private to public
# im = pg.screenshot(region=(1182, 957, 130, 50)) #max lobby count
# im = pg.screenshot(region=(793, 712, 335, 196)) #start hosted lobby
# im = pg.screenshot(region=(420,88,1000,145)) #announcements X:464 Y:133
# im = pg.screenshot(region=(420,400,1000,280)) #Disconnected From Server
# im = pg.screenshot(region=(420,400,1000,280)) #Game ban for disconnecting X: Y:
# im = pg.screenshot(region=(420,400,1000,280)) #Matchmaker is full
# im = pg.screenshot(region=(420,400,1000,280)) #Game Session Is Full
# im = pg.screenshot(region=(420,400,1000,280)) #Game Session Kicked
# im = pg.screenshot(region=(420,400,1000,280)) #Game Session Banned
# im = pg.screenshot(region=(420,400,1000,280)) #Game Session Has Started
# im = pg.screenshot(region=(420,400,1000,280)) #Game Matchmacker Has Been Disconnected
# im = pg.screenshot(region=(420,400,1000,280)) #Server Closed to inactivity
# im = pg.screenshot(region=(420,400,1000,280)) #Game is not upto date
# im = pg.screenshot(region=(420,400,1000,280)) #Matchmaker disconnected
# im = pg.screenshot(region=(420,400,1000,280)) #Game not found
#im = pg.screenshot(region=(1650, 0, 125, 125)) #Game Comment Icon X:1518 Y:130
# im = pg.screenshot(region=(1650, 0, 125, 125)) #Game Comment Icon2 X:1518 Y:130
# im = pg.screenshot(region=(1450, 70, 125, 125)) # Meeting Game Comment Icon X: 1513 Y: 128
# im = pg.screenshot(region=(1450, 70, 125, 125)) # Meeting Game Comment Icon2 X:1513 Y: 128
# im = pg.screenshot(region=(1450, 70, 125, 125)) # open meeting game comment icon X: 1513 Y: 128
# im = pg.screenshot(region=(1680, 770, 210, 300)) #Play Again Button
# im = pg.screenshot(region=(290,910,205,55)) # Click Vote to skip
# im = pg.screenshot(region=(525, 890, 95, 95)) #Confirm Vote To Skip
# im = pg.screenshot(region=(270, 850, 1150, 130)) #Comment Box X:  Y: 
# im = pg.screenshot(region=(1320, 875, 80, 75)) #Comment submit X: 1360 Y: 906
# im = pg.screenshot(region=(550, 100, 728, 88)) #Who is imposter X:  Y: 
# im = pg.screenshot(region=(420,400,1000,280)) # game requires update X: 1513 Y: 128
# im = pg.screenshot(region=(420,400,1000,280)) #Packets no response
# im = pg.screenshot(region=(850,240,590,455)) #upload data X:959 Y: 655
# im = pg.screenshot(region=(850,310,575,400)) #download dataX:959 Y: 655
# im = pg.screenshot(region=(580,140,780,260)) #calibrate yellow distributor X:1234 Y:306
# im = pg.screenshot(region=(580,140,780,530)) #calibrate dark blue distributor X:1234 Y:580
# im = pg.screenshot(region=(580,140,780,800)) #calibrate light blue distributor X:1234 Y:835
#im = pg.screenshot(region=(375,88,1200,275)) #User is Imposter X: Y:
# im = pg.screenshot(region=(365,88,1200,275)) #User is crewmate X: Y:
# im = pg.screenshot(region=(909,477,99,121)) #Get user on screen X: Y:

#####For Keyboard Moving########
# im = pg.screenshot(region=(0,0,908,485)) #Screen Area 1 X: Y:
# im = pg.screenshot(region=(900,0,125,454)) #Screen Area 2  X: Y: 
# im = pg.screenshot(region=(1000,0,908,485)) #Screen Area 3 X: Y:
# im = pg.screenshot(region=(0,450,908,160)) #Screen Area 4 X: Y:
# im = pg.screenshot(region=(1012,450,908,160)) #Screen Area 5 X: Y:
# im = pg.screenshot(region=(0,580,908,500)) #Screen Area 6 X: Y:
# im = pg.screenshot(region=(900,580,125,500)) #Screen Area 7  X: Y: 
# im = pg.screenshot(region=(1000,580,908,500)) #Screen Area 8 X: Y:
#####For Keyboard Moving########

#im = pg.screenshot(region=(70,100,1600,890)) #Get area on screen for mouse moving X: Y:

# im = pg.screenshot(region=(0,0,1700,485)) #Top of screen X: Y:
# im = pg.screenshot(region=(0,300,908,450)) #Left side of screen X: Y:
im = pg.screenshot(region=(1012,300,700,450)) #Right side of screen X: Y:

# im = pg.screenshot(region=(0,580,1700,500)) #Bottom Of screenX: Y:


# Todo for tasks for the skeld
# admin swipe card
# weapons clear asteroids
# Electrical Divert Power
# Fix Wiring
# Medbay inspect sample
# Medbay Submit Scan
# Empty Garbage
# Navigation Stabilize Steering
# Align Engine output
# Clean o2 filter
# Fuel Engines
# Start Reactor
# Navigation chart course
# Reactor start manifolds

im.save(r"savedimage.png")