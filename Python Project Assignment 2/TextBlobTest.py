# Michael S.    Comp 3320   Python  Project Assignment #2 TextBlob Showcase    *May Require a NLTK download, command prompt line: python -m textblob.download_corpora
#Written using Sublime Text: use toggle block comment to enable/disable certain parts of the code; highlight then ctrl+shift+/ on Sublime
#ShowCase Title: Simplified Poem Analysis Machine!!! aka SPAM!!!
#SideNote: at it's current state, the goal is to showcase some of TextBlob's functions. If added features such as user input, ability to change user language settings, etc... are added, then name must be changed to Super Poem Analysis Machine aka SPAM 1.0 

#Credits to the poets: poem1: Edgar Allan Poe A Dream within a Dream 1850        poem2: Langston Hughes Harlem 1990
import os.path
from os import path
from textblob import *
#---------------------------------------------------------------------------------------
#Import the Poems as TextBlob Objects
with open('Poem1.txt','r') as file:
	Poem1 = TextBlob(file.read())
with open('Poem2.txt','r') as file:
	Poem2 = TextBlob(file.read())

#---------------------------------------------------------------------------------------
# #Translations   
# #Translates the poems into spanish through google translate; I (Michael Sanchez) can confirm the spanish translation is solid. 
# print("Edgar Allan Poe:")
# print(Poem1.translate(to = 'es'))
# print()
# print("Langston Hughes: ")
# print(Poem2.translate(to = 'es'))
# print()
# #The translation option would be great in instances in which you would want to change UI based on Language but don't have access to a professional translator/localizer
# #Google Translate provides a pretty decent translation 
# #*Remember Sometimes google translate may at times not always translate so well, Also certain phrases/sayings may not retain the same meaning if not localized

#---------------------------------------------------------------------------------------
#Finding and printing counts
#turns the poems in word lists, "Does not include " " or punctation marks 
p1Words= Poem1.words
p2Words= Poem2.words
p1NounPhr = Poem1.noun_phrases
p2NounPhr = Poem2.noun_phrases

#Prints out the list of words   * uncomment the print(nounPhr) line to see the list of noun phrases
print()
print(p1Words)
#print(p1NounPhr)
print()
print(p2Words)
#print(p2NounPhr)

#turns poems into sentence list  *doesn't work too well with the formatting of poetry would work better with regular text
# p1Sen= Poem1.sentences
# p2Sen= Poem2.sentences

#We can use python's built in length function to count the number of words in the created word lists
print()
print("Poem 1 has ",len(p1Words)," words")
print("Poem 1 has ",len(p1NounPhr)," noun phrases")
print()
print("Poem 2 has ",len(p2Words)," words")
print("Poem 1 has ",len(p1NounPhr)," noun phrases")

print()

# This also opens up the door for creating other comparisons
if(len(p2Words)> len(p1Words)):
	print("Poem 2 has more words than Poem 1")
elif (len(p1Words)> len(p2Words)):
	print("Poem 1 has more words than Poem 2")

#We could also count that amount of times a word appears
print("The word Dream appears in Poem 1 ", Poem1.words.count("Dream"), "times")	
print("The appears in Poem 1 ", Poem1.words.count("The"), "times")	
print()
print("The word Dream appears in Poem 2 ", Poem2.words.count("Dream"), "times")	
print("The appears in Poem 2 ", Poem2.words.count("The"), "times")
print()
#---------------------------------------------------------------------------------------
#Sentiment Analysis   *Polarity- negative = negative tone, positive = positive tone, closer to zero is neutral tone
#                     *Subjectivity- 0.0 is very objective, while 1.0 is very subjective
# with this data we could make comparisons and makes conlusions based on them
#
print()
#Prints out the sentiment for Poem1
print("Poem 1 sentiment analysis results: " ,Poem1.sentiment)	
print()
#Checks whether the polarity is on the Positive or Negative side # Checks also if polarity is closer to neutral or positive/negative
if(Poem1.sentiment.polarity > 0):
	print("Poem 1 is on the Positive")
	if(round(Poem1.sentiment.polarity)==0):
		print("Poem 1 is neutral Positive")
	elif(round(Poem1.sentiment.polarity)==1):
		print("Poem 1 is positive Positive")

elif(Poem1.sentiment.polarity < 0):
	print("Poem 1 is on the Negative")
	if(round(Poem1.sentiment.polarity)==0):
		print("Poem 1 is neutral Negative")
	elif(round(Poem1.sentiment.polarity)==-1):
		print("Poem 1 is negative Negative")		
print()
#Checks if subjectivity is close to Objective(0) or Subjective(1)   *Currently doesnt check for neutrality
if(round(Poem1.sentiment.subjectivity)==0):
	print("Poem 1 can be considered Objective")
elif(round(Poem1.sentiment.subjectivity)==1):
	print("Poem 1 can be considered subjective ")	
print()

#Prints out sentiment for Poem2
print("Poem 2 sentiment alaysis results: ",Poem2.sentiment)
print()
#Checks whether the polarity is on the Positive or Negative side # Checks also if polarity is closer to neutral or positive/negative
if(Poem2.sentiment.polarity > 0):
	print("Poem 2 is on the Positive")
	if(round(Poem2.sentiment.polarity)==0):
		print("Poem 2 is neutral Positive")
	elif(round(Poem2.sentiment.polarity)==1):
		print("Poem 2 is positive Positive")

elif(Poem2.sentiment.polarity < 0):
	print("Poem 1 is on the Negative")
	if(round(Poem1.sentiment.polarity)==0):
		print("Poem 1 is neutral Negative")
	elif(round(Poem1.sentiment.polarity)==-1):
		print("Poem 1 is negative Negative")		
print()
#Checks if subjectivity is close to Objective(0) or Subjective(1)   *Currently doesnt check for neutrality
if(round(Poem2.sentiment.subjectivity)==0):
	print("Poem 2 can be considered Objective")
elif(round(Poem2.sentiment.subjectivity)==1):
	print("Poem 2 can be considered subjective ")	
print()
print()

#Looks for which poem is more positve and which is more negative
#only displays the most positive if  polarity > 0
if( Poem1.sentiment.polarity > Poem2.sentiment.polarity and Poem1.sentiment.polarity > 0):
	print("Poem 1 is more postive than Poem 2")
elif(Poem1.sentiment.polarity < Poem2.sentiment.polarity and Poem2.sentiment.polarity > 0):
	print("Poem 2 is more postive than Poem 1")	
elif(Poem1.sentiment.polarity == Poem2.sentiment.polarity and Poem2.sentiment.polarity > 0):
	print("Poem 1 is as postive as Poem 2")	
#only displays the most Negative if  polarity > 0
if( Poem1.sentiment.polarity < Poem2.sentiment.polarity and Poem1.sentiment.polarity < 0):
	print("Poem 1 is more Negative than Poem 2")
elif(Poem1.sentiment.polarity > Poem2.sentiment.polarity and Poem2.sentiment.polarity < 0):
	print("Poem 2 is more Negative  than Poem 1")
elif(Poem1.sentiment.polarity == Poem2.sentiment.polarity and Poem2.sentiment.polarity < 0):
	print("Poem 1 is as Negative as Poem 2")		