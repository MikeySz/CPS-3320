#Hang Man HW Assignment            Michael S.        Comp 3320

from turtle import *
import random

#List of Animals and an empty List
A =["cat","dog","frog","wolf","horse","mouse","turtle","rabbit","giraffe","salamander"]
L =[] 

#orginal test data 
#A= ['h','a','n','g','m','a','n']
#L= ['_','_','_','_','_','_','_']

play = True
wrongC= 0  #counter for failed guesses
randoWord = random.randint(0,(len(A)-1))   #chooses a random int from 0 to the length of list A

#Hangman Post     Creates the post as the starting point. Shown on Turtle
ht()
forward(100)  #pos: X:100 Y:0
penup()
backward(50)  #pos: X:50 Y:0
pendown()
left(90)
forward(200)  #pos: X:50 Y:200
right(90)
forward(50)  #pos: X:100 Y:200
right(90)
forward(10) #pos: X:100 Y:190


#A draw function to draw the hangman in increments 
def Draw(c):
	
	if c==1:
		#Hangman Head
		penup()
		goto(90, 180)
		pendown()
		circle(10)
	if c==2:
		#Hangman Body
		penup()
		goto(100, 170)
		pendown()
		forward(50)
	if c==3:
		#Hangman Left Arm
		penup()
		goto(100, 160)
		pendown()
		right(30)
		forward(20)
		left(30)
	if c==4:
		#Hangman Right Arm
		penup()
		goto(100, 160)
		pendown()
		left(30)
		forward(20)
		right(30)
	if c==5:
		#Hangman Left leg
		penup()
		goto(100, 120)
		pendown()
		right(30)
		forward(20)
		left(30)
	if c==6:
		#Hangman Right leg
		penup()
		goto(100, 120)
		pendown()
		left(30)
		forward(20)
		right(30)
		


#Code to fill L[] with _ to the same length as A[randoWord]
i=0
for i in range(len(A[randoWord])):
	L.append('_')
	i+=1

#Start of the game
while play == True:
	#Ask's user to guess letter
	letter = input("Guess a letter: ")
	letter = letter.lower()
	notFound = True
    #Checks to see if the letter is in the Answer
	i=0
	for currentletter in A[randoWord]:
		#If letter is found, then underscore in L is 
		#set to that letter

		if letter == currentletter:
			notFound = False
			L[i] = letter
		i = i+1	

		#Displays what the player has so far in (L) 
	print(' '.join(str(n) for n in L))
	if notFound:
		wrongC +=1
		print("BAD GUESS!", wrongC)
		Draw(wrongC)
		if wrongC == 6:
			play = False




    #Test to see if  the word has been succefully completed
    #if so, game ends
	if '_' not in L:

	      play = False

if wrongC == 6:
	print("Failed")
else:
	print("Great Job")	

Screen().exitonclick()
	