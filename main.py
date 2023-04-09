#!/usr/bin/env python3

#pip install pyautogui
#pip install pywin32
#pip install keyboard
#pip install pillow
#pip install opencv-python

import pyautogui as pg
import win32api, win32con
import keyboard
import time
import sys

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

number_of_games = 0

while keyboard.is_pressed('q') == False:

# This section finds or starts games
#######################################
    #Home Screen Online
    if pg.locateOnScreen(r"Images\\home_screen\\home_screen_online.png", region=(965,635,355,150), grayscale=True, confidence=0.8) != None:
        print("Home Screen For Online Button")
        click(1137, 709)
        time.sleep(0.5)

    #Find Game Online
    elif pg.locateOnScreen(r"Images\\home_screen\\find_game_online.png", region=(782,650,360,100), grayscale=True, confidence=0.8) != None:
        print("Find Game Online")
        click(947, 698)
        time.sleep(0.5)

    #Create Game Online
    elif pg.locateOnScreen(r"Images\\home_screen\\create_game_online.png", region=(782,350,360,100), grayscale=True, confidence=0.8) != None:
        print("Create Game Online")
        click(964, 400)
        time.sleep(0.5)

    #Confirm Host Game
    elif pg.locateOnScreen(r"Images\\home_screen\\confirm_host_game.png", region=(1600, 965, 280, 80), grayscale=True, confidence=0.8) != None:
        print("Confirm Host Game")
        click(1744, 1000)
        time.sleep(0.5)

    #Switch Private To Public
    elif pg.locateOnScreen(r"Images\\home_screen\\switch_private_to_public.png", region=(590, 946, 200, 70), grayscale=True, confidence=0.8) != None:
        print("Switch Private To Public")
        click(680, 980)
        time.sleep(0.5)
    
    #Check For Max Lobby Count
    elif pg.locateOnScreen(r"Images\\home_screen\\max_lobby_count.png", region=(1182, 957, 130, 50), grayscale=True, confidence=0.6) != None:
        print("Max Lobby Count")
        # Start Hosted Lobby
        if pg.locateOnScreen(r"Images\\home_screen\\start_hosted_lobby.png", region=(793, 712, 335, 196), grayscale=True, confidence=0.8) != None:
            print("Start Hosted Lobby")
            click(915, 800)
            time.sleep(0.5)

    #Public Game Search
    elif pg.locateOnScreen(r"Images\\home_screen\\public_game_search.png", region=(435, 335, 1050, 650), grayscale=True, confidence=0.8) != None:
        print("Public Game Search")
        # Trys to click the first game available
        click(950, 420)
        time.sleep(0.5)

    #Public Game Refresh
    elif pg.locateOnScreen(r"Images\\home_screen\\public_game_refresh.png", region=(1480, 335, 135, 135), grayscale=True, confidence=0.8) != None:
        print("Public Game Refresh")
        click(1550, 400)
        time.sleep(0.5)
###########################################
# End of section that finds or starts games

# This section is for automating tasks
#######################################

    #Downloads Data
    elif pg.locateOnScreen(r"Images\\automating_tasks\\download_data.png", region=(850,310,575,400), grayscale=True, confidence=0.8) != None:
        print("Download Data")
        click(959, 655)
        time.sleep(0.5)

    #Uploads Data
    elif pg.locateOnScreen(r"Images\\automating_tasks\\upload_data.png", region=(850,240,590,455), grayscale=True, confidence=0.8) != None:
        print("Upload Data")
        click(959, 655)
        time.sleep(0.5)

    #Calibrate Light Blue Distributor
    elif pg.locateOnScreen(r"Images\\automating_tasks\\calibrate_light_blue_distributor.png", region=(580,140,780,800), grayscale=True, confidence=0.8) != None:
        print("Calibrate Light Blue Distributor")
        click(1234, 835)
        time.sleep(0.2)

    #Calibrate Dark Blue Distributor
    elif pg.locateOnScreen(r"Images\\automating_tasks\\calibrate_dark_blue_distributor.png", region=(580,140,780,530), grayscale=True, confidence=0.8) != None:
        print("Calibrate Dark Blue Distributor")
        click(1234, 580)
        time.sleep(0.2)

    #Calibrate Yellow Distributor
    elif pg.locateOnScreen(r"Images\\automating_tasks\\calibrate_yellow_distributor.png", region=(580,140,780,260), grayscale=True, confidence=0.6) != None:
        print("Calibrate Yellow Distributor")
        click(1234, 306)
        time.sleep(0.2)

#######################################
# End Of section for automating tasks

# This section is to figure out if user is imposter or crewmate and comment in meetings 
########################################################################################

    #User Is Imposter
    elif pg.locateOnScreen(r"Images\\user_is_imposter.png", region=(375,88,1200,275), confidence=0.8) != None:
        print("User Is Imposter")
        imposter_status = True
        crewmate_status = False
        time.sleep(0.5)
    
    #User Is Crewmate
    elif pg.locateOnScreen(r"Images\\user_is_crewmate.png", region=(365,88,1200,275), grayscale=True, confidence=0.7) != None:
        print("User Is Crewmate")
        crewmate_status = True
        imposter_status = False
        time.sleep(0.5)

    #Who is imposter
    elif pg.locateOnScreen(r"Images\\who_is_imposter.png", region=(550, 100, 728, 88), grayscale=True, confidence=0.9) != None:
        print("Who is imposter")
        time.sleep(0.5)
        # Meeting Game Comment with no new notification
        if pg.locateOnScreen(r"Images\\meeting_game_comment_icon2.png", region=(1450, 70, 125, 125), grayscale=True, confidence=0.9) != None:
            print("Meeting Game comment Icon 2")
            click(1513, 128)
            time.sleep(0.5)
            if pg.locateOnScreen(r"Images\\comment_box.png", region=(270, 850, 1150, 130), grayscale=True, confidence=0.9) != None:
                print("Comment Box")
                if imposter_status == True:
                    pg.typewrite("I am the imposter!",.1)
                    print("I am the imposter!")
                    time.sleep(.5)
                    #########################
                    if pg.locateOnScreen(r"Images\\comment_submit.png", region=(1320, 875, 80, 75), grayscale=True, confidence=0.9) != None:
                        print("Comment Submit")
                        click(1360, 906)
                        time.sleep(.5)
                        if pg.locateOnScreen(r"Images\\open_meeting_game_comment_icon.png", region=(1450, 70, 125, 125), grayscale=True, confidence=0.8) != None:
                            print("Open meeting Game comment Icon")
                            click(1513, 128)
                            time.sleep(25)
                            if pg.locateOnScreen(r"Images\\vote_to_skip.png", region=(290,910,205,55), grayscale=True, confidence=0.8) != None:
                                print("Vote To Skip")
                                click(398, 940)
                                time.sleep(0.5)
                                if pg.locateOnScreen(r"Images\\confirm_vote_skip.png", region=(525, 890, 95, 95), grayscale=True, confidence=0.8) != None:
                                    print("Confirm Vote Skip")
                                    click(569, 939)
                                    time.sleep(50)
                    #########################
                elif crewmate_status == True:
                    pg.typewrite("I am a crewmate!",.1)
                    print("I am a crewmate!")
                    time.sleep(.5)
                    #########################
                    if pg.locateOnScreen(r"Images\\comment_submit.png", region=(1320, 875, 80, 75), grayscale=True, confidence=0.9) != None:
                        print("Comment Submit")
                        click(1360, 906)
                        time.sleep(.5)
                        if pg.locateOnScreen(r"Images\\open_meeting_game_comment_icon.png", region=(1450, 70, 125, 125), grayscale=True, confidence=0.8) != None:
                            print("Open Meeting Game comment Icon")
                            click(1513, 128)
                            time.sleep(25)
                            if pg.locateOnScreen(r"Images\\vote_to_skip.png", region=(290,910,205,55), grayscale=True, confidence=0.8) != None:
                                print("Vote To Skip")
                                click(398, 940)
                                time.sleep(0.5)
                                if pg.locateOnScreen(r"Images\\confirm_vote_skip.png", region=(525, 890, 95, 95), grayscale=True, confidence=0.8) != None:
                                    print("Confirm Vote Skip")
                                    click(569, 939)
                                    time.sleep(50)
                    #########################

######################################################################################
# End of section to figure out if user is imposter or crewmate and comment in meetings 

# This section is for Notifications
###########################################
    #Announcements
    elif pg.locateOnScreen(r"Images\\notifications\\announcements.png", region=(420,88,1000,145), grayscale=True, confidence=0.9) != None:
        print("Announcements")
        click(464, 133)
        time.sleep(0.5)
    
    #Matchmaker is full
    elif pg.locateOnScreen(r"Images\\notifications\\matchmaker_is_full.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Matchmaker is full")
        click(463, 450)
        time.sleep(0.5)

    #Game Requires Update
    elif pg.locateOnScreen(r"Images\\notifications\\game_requires_update.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Game Requires Update")
        click(463, 450)
        time.sleep(0.5)

    #Disconnected From Server
    elif pg.locateOnScreen(r"Images\\notifications\\disconnected_from_server.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Disconnected From Server")
        click(463, 450)
        time.sleep(0.5)

    #Game Ban for Disconnecting for 5 min
    elif pg.locateOnScreen(r"Images\\notifications\\game_ban_for_disconnecting.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Game Ban for Disconnecting, Going to sleep for 5 min")
        click(463, 450)
        time.sleep(305)

    #Packets No Response
    elif pg.locateOnScreen(r"Images\\notifications\\packets_no_response.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Packets No Response")
        click(463, 450)
        time.sleep(0.5)

    # Game session is full
    elif pg.locateOnScreen(r"Images\\notifications\\game_session_full.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Game Session Is Full")
        click(463, 450)
        time.sleep(0.5)

    #Game Session Is Kicked
    elif pg.locateOnScreen(r"Images\\notifications\\game_session_kicked.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Game Session Is Kicked")
        click(463, 450)
        time.sleep(0.5)

    #Game Session is banned
    elif pg.locateOnScreen(r"Images\\notifications\\game_session_banned.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Game Session Is Banned")
        click(463, 450)
        time.sleep(0.5)

    #Game Session Has Already Started
    elif pg.locateOnScreen(r"Images\\notifications\\game_session_started.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Game Session Has Already Started")
        click(463, 450)
        time.sleep(0.5)

    #Matchmaker Disconnected
    elif pg.locateOnScreen(r"Images\\notifications\\matchmaker_disconnected.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Matchmacker Disconnected")
        click(463, 450)
        time.sleep(0.5)

    #Server Closed To Inactivity
    elif pg.locateOnScreen(r"Images\\notifications\\server_closed_inactivity.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Server Closed To Inactivity")
        click(463, 450)
        time.sleep(0.5)

    #Game is not upto date
    elif pg.locateOnScreen(r"Images\\notifications\\game_not_updated.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Game is not upto date")
        click(463, 450)
        time.sleep(0.5)

    #Game not found
    elif pg.locateOnScreen(r"Images\\notifications\\game_not_found.png", region=(420,400,1000,280), grayscale=True, confidence=0.9) != None:
        print("Game not found")
        click(463, 450)
        time.sleep(0.5)

    ## Game Comment with no new notification
    ## elif pg.locateOnScreen(r"Images\\game_comment_icon.png", region=(1650, 0, 125, 125), grayscale=True, confidence=0.9) != None:
    ##     print("Game comment Icon")
    ##     time.sleep(0.5)

    ##Game Comment with new notification
    ## elif pg.locateOnScreen(r"Images\\game_comment_icon2.png", region=(1650, 0, 125, 125), grayscale=True, confidence=0.9) != None:
    ##     print("Game comment Icon 2")
    ##     time.sleep(0.5)

    ############################
    # End of Notifications

# This section is for the rest
###############################

    #Game Play Again Button
    elif pg.locateOnScreen(r"Images\\play_again_button.png", region=(1680, 770, 210, 300), grayscale=True, confidence=0.8) != None:
        print("Game Play Again Button")
        click(1790, 849)
        time.sleep(0.5)

        #Number Of games played
        number_of_games = number_of_games + 1
        original_stdout = sys.stdout # Save a reference to the original standard output
        with open('number_of_games.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print(f'The game has been played {number_of_games} times.')
            sys.stdout = original_stdout # Reset the standard output to its original value

    #Confirm Vote Skip
    elif pg.locateOnScreen(r"Images\\confirm_vote_skip.png", region=(525, 890, 95, 95), grayscale=True, confidence=0.8) != None:
        print("Confirm Vote Skip")
        click(569, 939)
        time.sleep(0.5)

    #Vote to skip
    elif pg.locateOnScreen(r"Images\\vote_to_skip.png", region=(290,910,205,55), grayscale=True, confidence=0.8) != None:
        print("Vote To Skip")
        click(398, 940)
        time.sleep(0.5)

    # No Action Taken
    else:
        print("No Action Taken")
        time.sleep(0.5)

##############################
# End Of the rest