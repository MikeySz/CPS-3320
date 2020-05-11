#Michael Sanchez     Mis/In/Formed
#Mis/In/Formed is a puzzle/simulation game centered around a human AI that must sort/select between articles to be posted by a media/news website
#Note-to-Self: For further development, Focus on keeping this PY file for Animations and Menus.

#Basic Setup 
import pygame, sys
#-----------------------------------------------------------------------------
#Making use of Pandas to create GameData Sheets(for Week 1) and will also be used for Save Data
#Work on an auto in-game article generator would be best for beyond week 1. Truly only week 1 should be hard coded and adapted as a tutorial
#an in-game article generator could also make the game abit more rogue like
#Would all require more planning

import pandas as pd
import os.path
from os import path
from gdc import *

#Checks if the game data file exists if not creates it through function within gdc.py else is loads the csv file
if not path.exists("GameData.csv"):
	CreateGameData()
	gDF = pd.read_csv("GameData.csv")
#Default Game Week & lvl	
	week = 1
	lvl = 1
	#print('Creating Data')
	#print(gDF)
else:
	gDF = pd.read_csv("GameData.csv")
#Default Game Week & lvl	
	week = 1
	lvl = 1
	#print(gDF)

mainClock = pygame.time.Clock()
#-----------------------------------------------------------------------------
#Loads Image to be used later by the program
bgImg = pygame.image.load("Assets/MisInFormedBG.png")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#MainMenu Button images
qbImg = pygame.image.load("Assets/QButton.png")
ngImg = pygame.image.load("Assets/NGButton.png")
sImg = pygame.image.load("Assets/SButton.png")
cImg = pygame.image.load("Assets/ContinueButton.png")
#-orgirnally CLicked but should be Selected/hovered Main Menu Buttons
qbImgCL = pygame.image.load("Assets/QButtonClicked.png")
ngImgCL = pygame.image.load("Assets/NGButtonClicked.png")
sImgCL = pygame.image.load("Assets/SButtonClicked.png")
cImgCL = pygame.image.load("Assets/ContinueButtonClicked.png")
#New Game and Settings Buttons
POImg = pygame.image.load("Assets/POButton.png")
BImg= pygame.image.load("Assets/BButton.png")
daImg= pygame.image.load("Assets/DAButton1.png")
#-Selected Variants
POImgS = pygame.image.load("Assets/POButtonSelected.png")
BImgS = pygame.image.load("Assets/BButtonSelected.png")
daImgS = pygame.image.load("Assets/DAButton2.png")
#gameBG
GBgImg=pygame.image.load("Animations/S1/MS44.png")
#-------------------------------------------------------------------------------
#Variable to check if animations are on or off	
#Will be later attached to a save file	
disableAnimations= 0
disableTxt = "Animations Enabled"
#-----------------------------------------------------------------------------
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Menu Window")
#using 1280 X 720 for the game window
#pygame.FULLSCREEN,
screen = pygame.display.set_mode((1280,720),0,32)

#The Font to be used by Pygame
font = pygame.font.SysFont("Courier.tiff", 20)
#=============================================================================

#Function the creates text
def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x,y)
	surface.blit(textobj,textrect)
#---------------------------------------------------------------------------
#sets the click variable to be used with the mouse left button	
click = False



#===============================================================================
# Function to text wrap retrieved from PYGAME WIKI  #SideNote: If any changes are made, I will Comment with #MyEDIT:
# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
#MyEDIT: Changed the order of the Arguments to be in line with the draw_text function above
def draw_Text__Wrap(text, font, color, surface, rect, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text	
#End of PYGAME WIKI Text Wrap CODE


#=============================================================================
#The Main Menu Screen
#Nearly All other screens are identical in coding and setup
def main_menu() :
	global click
	while True:
		#Fills the screen, Adds a Background and Displays a small text on the top to indicate the screen/menu
		screen.fill((0,0,0))
		screen.blit(bgImg, [0,0])
		draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
#-----------------------------------------------------------------------------
		#Coordinates for the Mouse Used to detect collision between the mouse and rectangles/buttons
		mx, my = pygame.mouse.get_pos()
#-----------------------------------------------------------------------------
#Creates the Buttons on the Main Menu
		NGButton = pygame.Rect(50, 100, 100, 50)
		CButton = pygame.Rect(50, 200, 100, 50)
		SButton = pygame.Rect(50, 300, 100, 50)
		QButton = pygame.Rect(50, 400, 100, 50)
#Draws the Buttons
		pygame.draw.rect(screen, (0, 0, 0),NGButton)
		pygame.draw.rect(screen, (0, 0, 0),CButton)
		pygame.draw.rect(screen, (0, 0, 0),SButton)
		pygame.draw.rect(screen,(0,0,0) ,QButton)
#Adds an image to the Buttons
		screen.blit(ngImg, NGButton)
		screen.blit(cImg, CButton)
		screen.blit(sImg, SButton)
		screen.blit(qbImg, QButton)
		
#-----------------------------------------------------------------------------
#Button Collision/Event
#First checks for a collision
#Then checks if a click is set to true
#If so it goes to it's respective screen or exits the game
		if NGButton.collidepoint((mx,my)):
			screen.blit(ngImgCL, NGButton)
			if click:
				NG_menu()
				pass
		if CButton.collidepoint((mx,my)):
			screen.blit(cImgCL, CButton)
			if click:
				continue_menu()
				pass
		if SButton.collidepoint((mx,my)):
			screen.blit(sImgCL, SButton)
			if click:
				settings_menu()
				pass
		if QButton.collidepoint((mx,my)):
			screen.blit(qbImgCL, QButton)
			if click:
				pygame.quit()
				sys.exit()
				pass
							
	

#----------------------------------------------------------------------------
		#Keeps the Click variable set false with every refresh of the game
		click = False
		#Checks for different event types and keys
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:    #When the left mouse button is held/pressed then click is equal to true
				if event.button == 1:
					click = True
					

		pygame.display.update()    #Display updates
		mainClock.tick(60)
#=============================================================================
def NG_menu():
	click = False
	running = True
	while running:
		screen.fill((0,0,0))
		screen.blit(bgImg, [0,0])
		draw_text('New Game',font,(255,255,255), screen, 20,20)
#-----------------------------------------------------------------------------
		mx, my = pygame.mouse.get_pos()
#-----------------------------------------------------------------------------
		POButton = pygame.Rect(50, 100, 100, 50)
		BButton = pygame.Rect(50, 200, 100, 50)

		pygame.draw.rect(screen, (0, 0, 0), POButton)
		pygame.draw.rect(screen, (0, 0, 0),BButton)

		screen.blit(POImg, POButton)
		screen.blit(BImg, BButton)

#----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#Button Collision/Event
		if POButton.collidepoint((mx,my)):
			screen.blit(POImgS, POButton)
			if click:
				level =1
				playScene(1)
				gameScreen(1,1,1)
				pass
		if BButton.collidepoint((mx,my)):
			screen.blit(BImgS, BButton)
			if click:
				running = False
				pass	
	

#----------------------------------------------------------------------------
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:    #Notable Change from main menu. Escape doesnt quit the game, instead it returns the user to previous screen
					running = False
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True				
		pygame.display.update()
		mainClock.tick(60)			
#=============================================================================

#=============================================================================
#As of this build, The continue menu only exists but has no purpose. Will be built alongside the Save/Load System. 
def continue_menu():
	running = True
	while running:
		screen.fill((0,0,0))
		screen.blit(bgImg, [0,0])
		draw_text('continue',font,(255,255,255), screen, 20,20)
#-----------------------------------------------------------------------------
		mx, my = pygame.mouse.get_pos()
#-----------------------------------------------------------------------------

#----------------------------------------------------------------------------
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True		
		pygame.display.update()
		mainClock.tick(60)			
#=============================================================================

#=============================================================================
#Settings currently can only disable animations/cutscenes for right now.
#Down the line will also handle sound and save data deletion
def settings_menu():
	running = True
	while running:
		screen.fill((0,0,0))
		screen.blit(bgImg, [0,0])
		draw_text('game',font,(255,255,255), screen, 20,20)
#-----------------------------------------------------------------------------
		mx, my = pygame.mouse.get_pos()
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
		DAButton = pygame.Rect(50, 100, 100, 50)
		BButton = pygame.Rect(50, 200, 100, 50)

		pygame.draw.rect(screen, (0, 0, 0), DAButton)
		pygame.draw.rect(screen, (0, 0, 0),BButton)

		screen.blit(daImg, DAButton)
		screen.blit(BImg, BButton)

#----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#Button Collision/Event
#The Disable Animations button will be useful for devloping the gameplay as it removes any of the in game animations
		global disableAnimations
		global disableTxt
		if disableAnimations == 0:
			disableTxt = "Animations Enabled"
		elif disableAnimations == 1:
			disableTxt = "Animations Disabled"	
		if DAButton.collidepoint((mx,my)):
			screen.blit(daImgS, DAButton)
			draw_text(disableTxt,font, (255,255,255),screen, 500, 20)
			if click:
				if disableAnimations == 0:
					disableAnimations = 1
					print("Animations Disabled")
				elif disableAnimations == 1:
					disableAnimations = 0
					print("Animations Enabled")
				pass
		if BButton.collidepoint((mx,my)):
			screen.blit(BImgS, BButton)
			if click:
				running = False
				pass	
	

#----------------------------------------------------------------------------
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True		
		pygame.display.update()
		mainClock.tick(60)			
#=============================================================================
#Scenes will be created through this function
#Takes in a number return a scene
def playScene(num):
	print("Animation Start")
	#will use a counter/timer to keep track of frame switching
	start_ticks= pygame.time.get_ticks()
	running = True
	i=0
	#if animations were disabled through the settings menu then this function will not run anything past this point
	if disableAnimations == 1:
		running = False
	#Scene 1	
	if num == 1:
		while running:
			#Loads an image from position i each time when running
			ms = pygame.image.load("Animations/S1/ms"+str(i+1)+".png")
			if i == 43:
				running = False
			if i == 42:
				pygame.time.delay(300) #Adds a delay to hold onto a single frame for abit more, less data used than using more frames/pngs 
			screen.fill((0,0,0))                                                         #however delay makes user input to be ignored, so a skip button may be frustrating
			screen.blit(ms,[0,0])
			#Counter and Start_ticks are used to calculate time in which a frame should appear
			counter=(pygame.time.get_ticks()-start_ticks)/100
			if counter > 1 and i<43:
				i = i+1
				start_ticks = pygame.time.get_ticks()		
	#----------------------------------------------------------------------------
			click = False
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						running = False
					if event.key == K_SPACE:   #Space button skips to nearly the last frame of the animations
						i = 42	
				if event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						click = True				
			pygame.display.update()
			mainClock.tick(60)	
#----------------------------------------------------------------------------
	#Scene 2
	if num == 2:
		while running:
			#Loads an image from position i each time when running
			ms = pygame.image.load("Animations/S2/ws"+str(i+1)+".png")
			#Making Use of the Delay function to Add Pauses to a Scene
			if i == 3 or i== 4 or i==5 or i == 6 or i == 7 or i==8 or i==9 :
				pygame.time.delay(1000)			
			if i == 21:
				pygame.time.delay(2000)
				running = False
			if i == 22:
				running = False
			screen.fill((0,0,0))
			screen.blit(ms,[0,0])
			counter=(pygame.time.get_ticks()-start_ticks)/100
			if counter > 1 and i<21:
				i = i+1
				start_ticks = pygame.time.get_ticks()		
	#----------------------------------------------------------------------------
			click = False
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						running = False
					if event.key == K_SPACE:
						i = 21	
				if event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						click = True				
			pygame.display.update()
			mainClock.tick(60)	
#----------------------------------------------------------------------------
#=============================================================================


def gameScreen(num,week,lvl):
#-----------------------------------------------------------------------------
	#pygame run variables
	running = True
	click = False
	global gDF
	s1= s2 = s3 = 0    #Scoring variables;   SideNote: Scoring system will definately need more work in the future

#-----------------------------------------------------------------------------	
	#Text Variables
	dTxt= CreateGameText(0)
	dCRGB=[255,255,255]

#-----------------------------------------------------------------------------
#GameAssets/Variables
	#Plays a scene if week/lvl condition are met
	if week == 1 and lvl == 1:
		playScene(2)
	#Article Icons
	AImg1=AImg2=AImg3 = pygame.image.load("Assets/Ar1.png")
	AImg1S=AImg2S=AImg3S = pygame.image.load("Assets/Ar1S.png")
	ADBImg = pygame.image.load("Assets/ADB.png")
	#Right Box and Button Icons
	rBImg= pygame.image.load("Assets/rBox.png")

	lgImg = pygame.image.load("Assets/rB/rB1.png")
	lgImgS = pygame.image.load("Assets/rB/rB2.png")
	dbImg = pygame.image.load("Assets/rB/rB3.png")
	dbImgS = pygame.image.load("Assets/rB/rB4.png")
	awImg = pygame.image.load("Assets/rB/rB5.png")
	awImgS = pygame.image.load("Assets/rB/rB6.png")

#-----------------------------------------------------------------------------	
	while running:
		screen.fill((0,0,0))
		screen.blit(GBgImg, [0,0])
		draw_text('game',font,(255,255,255), screen, 20,20)
#-----------------------------------------------------------------------------
		mx, my = pygame.mouse.get_pos()
#-----------------------------------------------------------------------------
		#Article Icons
		A1 = pygame.Rect(50, 100, 100, 150)
		A2 = pygame.Rect(200, 100, 100, 150)
		A3 = pygame.Rect(350, 100, 100, 150)

		pygame.draw.rect(screen, (0, 0, 0), A1)
		pygame.draw.rect(screen, (0, 0, 0), A2)
		pygame.draw.rect(screen, (0, 0, 0), A3)

		screen.blit(AImg1, A1)
		screen.blit(AImg2, A2)
		screen.blit(AImg3, A3)

		#Right Box- Main Text area for the "Hints"
		rBox = pygame.Rect(600,10,670,630)
		pygame.draw.rect(screen,(255,255,255),rBox)
		screen.blit(rBImg, rBox)

		rBaw = pygame.Rect(600,10,100,50)
		rBlg = pygame.Rect(885,10,100,50)
		rBdb = pygame.Rect(1170,10,100,50)
		pygame.draw.rect(screen,(255,255,255),rBaw)
		pygame.draw.rect(screen,(255,255,255),rBlg)
		pygame.draw.rect(screen,(255,255,255),rBdb)
		screen.blit(awImg, rBaw)
		screen.blit(lgImg, rBlg)
		screen.blit(dbImg, rBdb)



		#Lower Article Description Box
		ADB = pygame.Rect(10,454,450,200)
		dTBox = pygame.Rect(30, 464, 400,180)
		pygame.draw.rect(screen, (255,255,255), ADB)
		screen.blit(ADBImg, ADB)
		#Use of the Text Wrap Function to help insure that a paragraph does not continue in one line
		draw_Text__Wrap(dTxt,font,(dCRGB[0],dCRGB[1],dCRGB[2]),screen, dTBox )

#----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#Button Collision/Event
   #Allows for the Articles be swapped to three different icons/states to decide if they are "good", "bad" or not labelled	
		if A1.collidepoint((mx,my)):
			screen.blit(AImg1S, A1)
			dTxt = CreateGameText(1)
			if click:
				if s1 == 0:
					AImg1 = pygame.image.load("Assets/Ar3.png")
					AImg1S = pygame.image.load("Assets/Ar3S.png")
					s1 = s1+ 1
					print(s1)
				elif s1 == 1:
					AImg1 =pygame.image.load("Assets/Ar2.png")
					AImg1S = pygame.image.load("Assets/Ar2S.png")
				
					s1 = s1+ 1
					print(s1)
				elif s1 == 2:
					AImg1 = pygame.image.load("Assets/Ar1.png")
					AImg1S = pygame.image.load("Assets/Ar1S.png")
					s1 = 0
					print(s1)		

				pass
		if A2.collidepoint((mx,my)):
			screen.blit(AImg2S, A2)
			dTxt = CreateGameText(2)
			if click:
				if s2 == 0:
					AImg2 = pygame.image.load("Assets/Ar3.png")
					AImg2S = pygame.image.load("Assets/Ar3S.png")
					s2 = s2+ 1
				elif s2 == 1:
					AImg2 = pygame.image.load("Assets/Ar2.png")
					AImg2S = pygame.image.load("Assets/Ar2S.png")
					
					s2 = s2+ 1
				elif s2 == 2:
					AImg2 = pygame.image.load("Assets/Ar1.png")
					AImg2S = pygame.image.load("Assets/Ar1S.png")
					s2 = 0	
				pass
		if A3.collidepoint((mx,my)):
			screen.blit(AImg3S, A3)
			dTxt = CreateGameText(3)
			if click:
				if s3 == 0:
					AImg3 = pygame.image.load("Assets/Ar3.png")
					AImg3S = pygame.image.load("Assets/Ar3S.png")
					s3 = s3+ 1
				elif s3 == 1:
					AImg3 = pygame.image.load("Assets/Ar2.png")
					AImg3S = pygame.image.load("Assets/Ar2S.png")
					s3 = s3+ 1
				elif s3 == 2:
					AImg3 = pygame.image.load("Assets/Ar1.png")
					AImg3S = pygame.image.load("Assets/Ar1S.png")
					s3 = 0	
				pass

		if rBaw.collidepoint((mx,my)):
			screen.blit(awImgS, rBaw)
			if click:
				rBImg= pygame.image.load("Assets/rBoxG.png")
				pass
		if rBlg.collidepoint((mx,my)):
			screen.blit(lgImgS, rBlg)
			if click:
				rBImg= pygame.image.load("Assets/rBox.png")
				pass
		if rBdb.collidepoint((mx,my)):
			screen.blit(dbImgS, rBdb)
			if click:
				rBImg= pygame.image.load("Assets/rBoxB.png")
				pass										
#----------------------------------------------------------------------------
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
				if event.key == K_RETURN:
					if not s1 == 0 or s2 == 0 or s3 == 0:       #Needs some troubleshooting but goal is to prevent the results screen if any object is not labelled
						score = scoreGame(gDF,week, lvl, (s1-1), (s2-1), (s3-1))
						results_menu(score)		
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True			
		pygame.display.update()
		mainClock.tick(60)			
#=============================================================================
#=============================================================================
#Screen to present Results. Will eventually be used to present all actions/changes to the player's stats and in-game world changes
def results_menu(score):
	running = True
	while running:
		screen.fill((0,0,0))
		screen.blit(bgImg, [0,0])
		draw_text('Results',font,(255,255,255), screen, 20,20)
#-----------------------------------------------------------------------------
		mx, my = pygame.mouse.get_pos()
	##	resultTxt = "Results "+ str(score) 
#-----------------------------------------------------------------------------
		draw_text(resultTxt,font,(255,255,255), screen, 20,30)
		draw_text(reliablity(score),font,(255,255,255), screen, 20,40)

#----------------------------------------------------------------------------
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
				if event.key == K_q:
					pygame.quit()
					sys.exit()	
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True				
		pygame.display.update()
		mainClock.tick(60)			
#=============================================================================
#=============================================================================
#Most likely will not need but being kept just in case
# def pause_menu():
# 	running = True
# 	while running:
# 		screen.fill((0,0,0))
# 		screen.blit(bgImg, [0,0])
# 		draw_text('game',font,(255,255,255), screen, 20,20)
# #-----------------------------------------------------------------------------
# 		mx, my = pygame.mouse.get_pos()
# #-----------------------------------------------------------------------------

# #----------------------------------------------------------------------------
# 		click = False
# 		for event in pygame.event.get():
# 			if event.type == QUIT:
# 				pygame.quit()
# 				sys.exit()
# 			if event.type == KEYDOWN:
# 				if event.key == K_ESCAPE:
# 					running = False
# 			if event.type == MOUSEBUTTONDOWN:
# 				if event.button == 1:
# 					click = True		
# 		pygame.display.update()
# 		mainClock.tick(60)			
# #=============================================================================

#Runs the game starting from the main menu
main_menu()		

#Devloper End Notes:
#This Game started development as an assigment for a python course
#The scope of this game is pretty large for my vision as a one-man team
#But in doing so, There is so much more to continue building onto this game and building of programming, art,music and research skills.
#Some goals for the future include:
#-Generating paragraphs using most likely NLTK to provide for the in game articles
#-Heavy Reasearch into Misinformation overall, 
# both on paragraph/headline structure/grammar/punctuation,
# Real-world effects, groups/organizations who spread, political/religious connections, etc...
#-Continue Developing skills in using various python libraries
#-Continue Developing skills in Aseprite(Pixel Art)
#There is much more work to be done, For as of 5/11/2020 and last week of COMP 3320, Mis/In/Formed is very much a Work in Progress.
#This is only the Beginning
