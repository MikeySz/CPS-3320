#Michael Sanchez
#gdc.py will be centered around functions that create/handle data for the game

import pandas as pd
import pygame

#for right now, Week 1 is required to be hard coded into the game
# most of the level data will be handled in this fashion  EDIT- only the first few stages and special stages will be handled like this
#                                                              A Level generator may be best to avoid a large column of 0s 1s and any other numbers
#however as the game evolves, it may stretch beyond two columns and may go beyond variable 0 and 1
def CreateGameData():
	AcT = [1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1]
	HAt = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]

	gDict = {'Article Content Type':AcT, 'Has Author?':HAt}

	gDF = pd.DataFrame(gDict)

	gDF.to_csv("GameData.csv")

#===================================================================================================
#As of right now returns four diferent amounts of text
#May be evolved into a NLTK program to write artificial game text for the in game articles
def CreateGameText(num):
	if num == 0:
		return " "
	elif num == 1:	
		return "A paragraph is a self-contained unit of a discourse in writing dealing with a particular point or idea. A paragraph consists of one or more sentences. Though not required by the syntax of any language, paragraphs are usually an expected part of formal writing, used to organize longer prose."
	elif num == 2: 
		return "Squares are shapes. Circles are shapes. Yet Circles are not Squares. This is why....."
	elif num == 3:
		return "The sun is blue! The Grass is red! And this is FACT!"
	else: 
		return "Error " 
# The Current System to score the Game
# a Good Way to handle scoring but will need more work down the line
def scoreGame(Pandas, week, lvl, s1, s2, s3):
	score = 0
	if week == 1:
		if lvl == 1:
			if Pandas.loc[0, 'Article Content Type'] == s1:
				score = score +1
			if Pandas.loc[1, 'Article Content Type'] == s2:
				score = score +1
			if Pandas.loc[2, 'Article Content Type'] == s3:
				score = score +1		
	return score
#Returns a Ranking string to tell wether the player did perfect to very bad.
#Evolve eventually into the reliablity bar and take in more than score eventually.	
def reliablity(score):
	if score == 3:
		return "PERFECT"
	elif score == 2:
		return "OKAY"
	elif score == 1:
		return "BAD"
	elif score == 0:
		return "VERY BAD"	
