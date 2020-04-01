# Michael S.    Comp 3320   Python  Project Assignment #1  Sandwhich Recommendation Machine [Name Subject to Change]
#Imports
 #For writing and reading data
import json
 #For creation of the defaultList.txt (and customList.txt: if i get to it)
import os.path
from os import path

#to make use of the sleep function. Overall goal: create a sense that the program is "thinking really hard" to provide a satisfactory recommendation.
import time

#decision making
import random



#Text informs the User of What process occurs and Create a Sense of navigating a program rather than simple code.
print("Checking for Data!")
time.sleep(1)



#setting up: Creating the default list file and writing data to it

#Warning: If defaultList.txt exists in the same folder alongside this program and
#         does not contain the necessary data, it will fail during 
#         "#Setting up the dictionaries & list & user name for use by the program" located somewhere down below.

#Test to make sure text file exists, if not it create one
if not path.exists("defaultList.txt"):
	print("Data not Found!")
	time.sleep(1)
	print("Creating New Data!")	
	time.sleep(1)
	print()
#	print("False") #Test Data to check if the if statement worked.
	
    #Creates a new file: defaultList.txt 
	f= open("defaultList.txt", "w+")
	
	#The list to be added to the txt file
	SwDict = [
#----------------------------------------------------
#Primary: dlist[0]
			{"Meats":{"Ham":{"low":["Tuna","Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                 "mid":["Ham","Turkey","Pepper","Salt"],
			                 "high":["Cheddar","Mozzarella","Provolone","Mayo","Lettuce","Tomato","Pickles"]},
			        
			          "Turkey":{"low":["Tuna","Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                    "mid":["Ham","Turkey","Pepper","Salt"],
			                    "high":["Cheddar","Mozzarella","Provolone","Mayo","Lettuce","Tomato","Pickles"]},
			        
			          "Tuna":{"low":["Ham","Turkey","Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                  "mid":["Tuna","Cheddar","Mozzarella","Provolone","Pepper","Salt"],
			                  "high":["Mayo","Lettuce","Tomato","Pickles"]}},


			 "Cheese":{"Cheddar":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                      "mid":["Tuna","Mayo","Salt","Lettuce","Tomato","Pickles"],
			                      "high":["Ham","Turkey", "Cheddar","Mozzarella","Provolone","Pepper"]},
			           
			           "Mozzarella":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                         "mid":["Tuna","Mayo","Salt","Lettuce","Tomato","Pickles"],
			                         "high":["Ham","Turkey", "Cheddar","Mozzarella","Provolone","Pepper"]},
			           
			           "Provolone":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                        "mid":["Tuna","Mayo","Salt","Lettuce","Tomato","Pickles"],
			                        "high":["Ham","Turkey", "Cheddar","Mozzarella","Provolone","Pepper"]}},


			 "Spread": {"Peanut Butter":{"low":["Ham","Turkey","Tuna","Cheddar","Mozzarella","Provolone","Cream Cheese","Mayo","Pepper","Salt","Lettuce","Tomato","Pickles"],
			                         "mid":["Peanut Butter"],
			                         "high":["Jelly","Strawberries","Bananas"]},
			           
			           "Jelly":{"low":["Ham","Turkey","Tuna","Cheddar","Mozzarella","Provolone","Mayo","Pepper","Salt","Lettuce","Tomato","Pickles"],
			                    "mid":["Jelly"],
			                    "high":["Cream Cheese","Strawberries","Bananas"]},
			           
			           "Cream Cheese":{"low":["Ham","Turkey","Tuna","Cheddar","Mozzarella","Provolone","Peanut Butter","Mayo","Pepper","Salt","Lettuce","Tomato","Pickles"],
			                           "mid":["Cream Cheese"],
			                           "high":["Jelly","Strawberries","Bananas"]}}
			},
#-------------------------------------------------------
#Secondary: dlist[1]
			{"Condiments":{"Mayo":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                        "mid":["Cheddar","Mozzarella","Provolone","Mayo"],
			                        "high":["Ham","Turkey","Tuna","Pepper","Salt","Lettuce","Tomato","Pickles"]},
			               
			               "Pepper":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                        "mid":["Ham","Turkey","Tuna","Pepper"],
			                        "high":["Cheddar","Mozzarella","Provolone","Mayo","Salt","Lettuce","Tomato","Pickles"]},
			               
			                "Salt":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                        "mid":["Ham","Turkey","Tuna","Cheddar","Mozzarella","Provolone","Salt","Lettuce","Tomato","Pickles"],
			                        "high":["Mayo","Pepper"]}},


			 "Veggies":{"Lettuce":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                       "mid":["Cheddar","Mozzarella","Provolone","Salt","Lettuce"],
			                       "high":["Ham","Turkey","Tuna","Mayo","Pepper","Tomato","Pickles"]},
			            
			            "Tomato":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                      "mid":["Cheddar","Mozzarella","Provolone","Salt","Tomato"],
			                      "high":["Ham","Turkey","Tuna","Mayo","Pepper","Lettuce","Pickles"]},
			            
			            "Pickles":{"low":["Peanut Butter","Jelly","Cream Cheese","Strawberries","Bananas"],
			                       "mid":["Cheddar","Mozzarella","Provolone","Salt","Pickles"],
			                       "high":["Ham","Turkey","Tuna","Mayo","Pepper","Lettuce","Tomato"]}},


			 "Fruit":{"Strawberries":{"low":["Ham","Turkey","Tuna","Cheddar","Mozzarella","Provolone","Mayo","Pepper","Salt","Lettuce","Tomato","Pickles"],
			                          "mid":["Strawberries"],
			                          "high":["Peanut Butter","Jelly","Cream Cheese","Bananas"]},
			           
			           "Bananas":{"low":["Ham","Turkey","Tuna","Cheddar","Mozzarella","Provolone","Mayo","Pepper","Salt","Lettuce","Tomato","Pickles"],
			                      "mid":["Bananas"],
			                      "high":["Peanut Butter","Jelly","Cream Cheese","Strawberries"]}}
			},
#-------------------------------------------------------
# Bread: dlist[2] ["Bread"]
			{"Bread":["White Bread",
					  "Whole Grain Bread",
					  "Hero Roll",
					  "Bagel", 
					  "Pita"]},
#-------------------------------------------------------
#Like/Dislike: dlist[3]  ["Likes"/"Neutral"/"Dislikes"]
			{"Likes":[],
			 "Neutral":["Ham","Turkey","Tuna",
			 			"Cheddar","Mozzarella","Provolone",
			 			"Peanut Butter","Jelly","Cream Cheese",
			 			"Mayo","Pepper","Salt",
			 			"Lettuce","Tomato","Pickles",
			 			"Strawberries","Bananas",
			 			"White Bread","Whole Grain Bread",
					    "Hero Roll","Bagel","Pita"],
			 "Dislikes":[]},
#--------------------------------------------------------
#User Name here:   dlist[4]			 
			 "User"		  
		 ]


	with open('defaultList.txt','w') as filehandle:
		json.dump(SwDict, filehandle)	
    #After writing data to file, we load that same data back into a list
	with open('defaultList.txt') as f:
		dlist=json.load(f)		 

#If Text files exists, then we turn the data from defaultlist.txt to a list 
else:
	print("Data Found!")
	time.sleep(1)
	print("Loading Data!")	
	time.sleep(1)
	print()
#	print("True")# aslo Test Data to check if the if statement worked.	
	with open('defaultList.txt') as f:
		dlist=json.load(f)
#	print(dlist[2]["Bread"][1]) # Test Data to check how list dictionaries list would work

#=====================================================================
#Setting up the dictionaries & list & user name for use by the program
 #Primary dictionary
pD = dlist[0]
 #Secondary dictionary
sD = dlist[1]
 #Bread List
BreadL = dlist[2]["Bread"]  
 #Like/Dislike Dictionary
lD = dlist[3]  
 #User's Name:
uN = dlist[4]
#List of All Items currently avaible in the program
itemsL = ["Ham","Turkey","Tuna",
			  "Cheddar","Mozzarella","Provolone",
			  "Peanut Butter","Jelly","Cream Cheese",
			  "Mayo","Pepper","Salt",
			  "Lettuce","Tomato","Pickles",
			  "Strawberries","Bananas",
			  "White Bread","Whole Grain Bread",
			  "Hero Roll","Bagel","Pita"]


#=====================================================================

#Functions
	#Function to change userName
def changeUsername(uN):
	print("Do you want to change username?")
	time.sleep(.3)
	#Gives the user two choices
	uInput = input("Yes[1] or No[2]: ")
	#if user inputs Yes , 1 or yes
	if uInput in ["Yes", "1", "yes"]:
		nInput = input("Enter Name: ")
		uN = nInput
		dlist[4]= uN
		print("Saving Name")
		time.sleep(.3)
		with open('defaultList.txt','w') as f:
			json.dump(dlist, f)	
		print("Name Saved!")
		print()
		time.sleep(.3)
		print("Welcome " +uN)
		print()
		time.sleep(.6)
	
	elif uInput in[ "No" ,"2" ,"no"]:
		print("Welcome "+ uN)
		print()
		time.sleep(.6)
		return
	
	else:
		print("Invalid Input!")
		time.sleep(.6)
		print()
		changeUsername(uN)

#-------------------------------------------------------------------------		
#Change Likes/Dislikes    
def changeLD(lD,itemsL,i,c,f):
	if c == i and f < 2:
		dlist[3] = lD
		print()
		print("Saving Likes and Dislikes")
		time.sleep(.3)
		with open('defaultList.txt','w') as f:
			json.dump(dlist,f)	
		#print(lD)
		print("Succesfully Saved!")
		print()
		time.sleep(.2)
		f = 2
		return
	elif c== i:
		return	
	#when the function is first called, it setsup	
	if f < 1:
	    	print("Starting Like/Dislike Program:")
	    	lD["Likes"] = []
	    	lD["Neutral"] = []
	    	lD["Dislikes"]= []
	    	f = f+1
	    	print()
	    	time.sleep(.2) 
	print("What is your opinion on: "+itemsL[c])
	print("[1]Like" +"\n"+"[2]Neutral" +"\n"+"[3]Dislike"+"\n"+"[4]restore default")
	nInput = input("Select an Option Number: ")
	print()
	#Like
	if nInput in ['1','Like','like']:
		lD["Likes"].append(itemsL[c])
		c =c+1
		changeLD(lD,itemsL,i,c,f)
		
	#Neutral
	elif nInput in ['2','Neutral','neutral']:
		lD["Neutral"].append(itemsL[c])
		c =c+1
		changeLD(lD,itemsL,i,c,f)

    #Dislike 
	elif nInput in ['3','Dislike','dislike',]:
		lD["Dislikes"].append(itemsL[c])
		c =c+1
		changeLD(lD,itemsL,i,c,f)
	#restore default  #Adding a warning to this would be good.
	#                  Such as asking if the user is sure.(If statment)
	elif nInput in ['4','Restore','restore']:
		lD["Likes"] = []
		lD["Neutral"] = itemsL
		lD["Dislikes"]= []
		c = i
		changeLD(lD,itemsL,i,c,f)
		print()	
	#If no valid input is found then we run through the Program Again	
	else:
		print("Not Valid Input Try Again")
		print()
		time.sleep(.3)
		changeLD(lD,itemsL,i,c,f)

#-------------------------------------------------------------------------
#used to get the next item based oon if the previous item is atleast at mid-high compatible
def selectNextItem(pD, sD, lD,type,previousC):
	nextList = []
	if type in pD.keys():
		#The next item is chosen based on: ignore low compatible items, pick mid compatible items once (1/3) and pick high compatible items twice (2/3)
		nextList = pD[type][previousC]["mid"]+ pD[type][previousC]["high"]+ pD[type][previousC]["high"]
		testDislike = all(elem in lD["Dislikes"] for elem in nextList)
		randC =" "
		if testDislike:
			randC = random.choice(nextList)
		else:
			while randC in lD["Dislikes"] or randC ==" ":
				randC = random.choice(nextList)
	elif type in sD.keys():
		nextList =sD[type][previousC]["mid"]+ sD[type][previousC]["high"]+ sD[type][previousC]["high"]
		testDislike = all(elem in lD["Dislikes"] for elem in nextList)
		randC =" "
		if testDislike:
			randC = random.choice(nextList)
		else:
			while randC in lD["Dislikes"] or randC ==" ":
				randC = random.choice(nextList)
	if randC in pD["Meats"]:
		type ="Meats"
	elif randC in pD["Cheese"]:
		type ="Cheese"
	elif randC in pD["Spread"]:
		type ="Spread" 
	elif randC in sD["Condiments"]:
		type ="Condiments"	
	elif randC in sD["Veggies"]:
		type ="Veggies"	
	elif randC in sD["Fruit"]:
		type =	"Fruit"		
	return [randC, type]
#---Selects a Bread that is atleast neutral or Like; if all are disliked, any bread is choosen
def selectBread(BreadL,lD):
	testDislike = all(elem in lD["Dislikes"] for elem in BreadL)
	randBread =" "
	if testDislike:
		randBread = random.choice(BreadL)
	else:
		while randBread in lD["Dislikes"] or randBread ==" ":
			randBread = random.choice(BreadL)
	return randBread		


#---Make Sandwhich SubPrograms- Actuall Process of adding items together
def mSw(pD, sD, BreadL, lD,type):
	print("Preparing to make Sandwich")
	time.sleep(.4)
	customSandwhich = []
	count = 0
	testDislike = all(elem in lD["Dislikes"] for elem in list(pD[type].keys()))
	randC =" "
	if testDislike:
		randC = random.choice(list(pD[type].keys()))
	else:
		while randC in lD["Dislikes"] or randC ==" ":
			randC = random.choice(list(pD[type].keys()))
	customSandwhich.append(randC)
	customSandwhich.append(" ")
	print("Primary ready!")
	time.sleep(.3)
	count = count +1
	print("selecting other options...")
	time.sleep(.3)
	while count < 4:
		nextItems = selectNextItem(pD, sD, lD,type,randC)
		type = nextItems[1]
		randC = nextItems[0]
		if randC in customSandwhich:
			#customSandwhich.append("")
			count = count +1
		else:
			customSandwhich.append(randC)
			customSandwhich.append(" ")
			count = count +1			
	if count == 4:
		print("Picking Bread...")
		time.sleep(.3)
		bread = selectBread(BreadL,lD)
		customSandwhich.append("on ")
		customSandwhich.append(bread)
	print("Putting it all together!")
	time.sleep(.2)	
	print("Here is your sandwich Recommendation: ")
	time.sleep(.4)
	print()
	cSw = ""
	cSw = cSw.join(customSandwhich)
	print(cSw)		
	print()

#Wild Card Program; everythin is ignored except for repeats and one bread.
def wildCard(pD,sD,BreadL):
	print("Preparing Creation!")
	time.sleep(.5)
	wList = []
	listAll = list(pD["Meats"].keys())+list(pD["Cheese"].keys())+list(pD["Spread"].keys())+list(sD["Condiments"].keys())+list(sD["Veggies"].keys())+list(sD["Fruit"].keys())
	randC = " "
	i = 0
	print("Gathering Ingredients!")
	time.sleep(.3)
	while i < 5:
		randC = random.choice(listAll)
		if randC in wList:
			i = i+1
		else:	
			wList.append(randC)
			wList.append(" ")
			i = i+1
	wBread = random.choice(BreadL)
	wList.append("on ")
	wList.append(wBread)
	print("Your Creation is ready: ")
	print()
	time.sleep(.2)
	cSw = ""
	cSw = cSw.join(wList)
	print(cSw)		
	print()


#-------------------------------------------------------------------------
#Main Sandwhich Program Menu- Gets the Primary type
def createSw(pD, sD, BreadL, lD):
	print("Choose a Sandwich type")	
	print("[1]Meats" +"\n"+"[2]Cheese" +"\n"+"[3]Spread"+"\n"+"[4]WildCard")
	nInput = input("Select an Option Number: ")
	#Meat
	if nInput in ['1','Meats','meats']:
		mSw(pD, sD, BreadL, lD,"Meats")
		return
	#Cheese	
	elif nInput in ['2','Cheese','cheese']:
		mSw(pD, sD, BreadL, lD,"Cheese")
		return
    #Spreads 
	elif nInput in ['3','Spread','spread']:
		mSw(pD, sD, BreadL, lD,"Spread")
		return
	#WildCard
	elif nInput in ['4','WildCard','Wildcard','wildcard']:
		wildCard(pD,sD,BreadL)
		return
	#If no valid input is found then we run through the MainMenu Program Again	
	else:
		print("Not Valid Input Try Again")
		print()
		time.sleep(.3)
		createSw(pD, sD, BreadL, lD)
	time.sleep(.3)	

#-------------------------------------------------------------------------
#Main Menu
def MainMenu(pD, sD, BreadL, lD, uN,itemsL):
	print("Main Menu")
	time.sleep(.3)

	print("[1]Sandwich Recommendations"  +"\n"+"[2]Like/Dislike setup" +"\n"+"[3]Change Username" +"\n"+"[4]quit")
	time.sleep(.3)

	nInput = input("Select an Option Number: ")
	#Main Sandwhich Program
	if nInput in ['1','Sandwich','sandwich','Sandwich Recommendations','sandwich recommendations']:
		print()
		time.sleep(.3)
		createSw(pD, sD, BreadL, lD)
		print()
		MainMenu(pD, sD, BreadL, lD, uN,itemsL)
    #Change User's Like/Neutral/Dislike 
	elif nInput in ['2','Like/Dislike','Like','Dislike','like/dislike','like','dislike']:
		i = len(itemsL)
		changeLD(lD,itemsL,i,0,0)
		MainMenu(pD,sD,BreadL,lD,uN,itemsL)
    #Change Username
	elif nInput in ['3','Change Username','Change username','change username','change','Change']:
		changeUsername(uN)
		MainMenu(pD, sD, BreadL, lD, uN,itemsL)
	#Quits the program	
	elif nInput in ['4','Quit','quit']:
		quit()
	#If no valid input is found then we run through the MainMenu Program Again	
	else:
		print("Not Valid Input Try Again")
		print()
		time.sleep(.3)
		MainMenu(pD, sD, BreadL, lD, uN,itemsL)
	
#========================================================================
#Welcome/Greeting Message
greetings = ["Welcome","Hello","Greetings"]
randGreeting = random.choice(greetings)

#Main process
 #If default User name is detected, it prompts the user to change it(only appears when username is default)
if uN == "User" or "":
	print("Default Usename Detected!!!")
	time.sleep(.2)
	changeUsername(uN)
 #if default user name is not detected, it welcomes the user's current name
else:
 print(randGreeting +" "+uN)	
 print()
 time.sleep(.6)

MainMenu(pD, sD, BreadL, lD, uN,itemsL)


#End Notes: Overall the Program can give ONE recommendation based on the primary groups(Meats, Cheese and Spread).
#          Takes the approach where if X is compatible with Y and Y is compatible Z, thus X is compatible with Z.(Transitive)
#		   This leads to certain low compatiblities to take place but Overall isn't too Bad.
#          Like/Dislike system is rudimentary and requires more work alongside the compatiblities.
#          The Main Menu is navigated through recursion, but never returns to the original.(Which in current state is acceptable)
#          Cheese sandwhich may intersect often with meats(due to compatiblity), one possible solution would be to create a separate funciton to deal with strictly cheese