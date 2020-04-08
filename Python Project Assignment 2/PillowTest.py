# Michael S.    Comp 3320   Python  Project Assignment #2 Pillow Program
#Program Title: The Generic Gaming Youtuber's goto Thumbnails
#All images/character based/from copy righted material include: Pokemon(Pikachu) fromm Nintendo , Minecraft(In game screenshot) from Microsoft. And are being used under fair use for educational purposes
#---------------------------------------------------------------------------------------
from PIL import Image 
from PIL import ImageFilter
from PIL import PSDraw
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageEnhance
import random

#---------------------------------------------------------------------------------------
#Images are loaded in through Pillow's Image module's open function
#Background Image
bgImg= Image.open("CreeperMansion.png",'r')
#bgImg.show()
#An example of retrieving image properties. Size was used to understand the window size of the image. 
#The code in this example is set to work with a background image of 1920 X 1080
print(bgImg.size) 
#foreground image   *should have a Transparent background
#Will be place on top of the background
fgImg= Image.open("SurprisePikachu.png",'r')
#fgImg.show()
#---------------------------------------------------------------------------------------
#List used for choices of positoning used later down
posL =["Left","Center","Right"] 

#Based on the choice the postion, these values are subtracted from 1920 to get a postion on either bottom left, center or right
positionChoice = random.choice(posL)
if positionChoice == 'Left':
	positionX = 1920
elif positionChoice == 'Center':
	positionX = 1250
else:
	positionX = 600		

#flip is a random int from 0 to 1
flip = random.randint(0,1)
#if flip is 1 then we use a transpose to flip the foreground image over the vertical axis 
if flip == 1:
	fgImg = fgImg.transpose(Image.FLIP_LEFT_RIGHT)	
#expan is a random int from 0 to 1
expand = random.randint(0,1)
#if random int is 1 than the Image is Resized to be bigger/expanded
if expand == 1:
	fgImg = fgImg.resize((1200,1200))
	#The positionY is set, to later be subtracted from 1080
	positionY = 1200
	#The Coordinates of x must be accomadate for this bigger image
	positionX= positionX+300
else:
	#image is resized to a 600 by 600 square and the position Y is set
	fgImg = fgImg.resize((600,600))
	positionY = 600

#---------------------------------------------------------------------------------------
#A filter is added to the Background(through the filter function and ImageFilter module) to create a blur effect that will help drive focu to the foreground
fBgImg= bgImg.filter(ImageFilter.BLUR)
#The ImageEnhance module is used to add abit of contrast to the filtered background
Enhance = ImageEnhance.Contrast(fBgImg)
fBgImg = Enhance.enhance(1.5)
#Through the paste function we are able to add the foreground image to the filtered background
#Here we use the positionX and PositionY to set the foreground image's postion, the mask is set equal to the foreground image, thus keeping the Transparent background
fbgImg = fBgImg.paste(fgImg, (1920-positionX, 1080-positionY), mask=fgImg)

#Text Add is an ImageDraw object that allows us to write text, change font type and color.
textAdd =  ImageDraw.Draw(fBgImg)
#The Font is selected here through a true type file and the font size is also set here. Uses the ImageFont module and truetype function to retrieve a font style
font =ImageFont.truetype('impact.ttf',120)

#Random ints between 0 to 255 for random colors
randR = random.randint(0,255)
randG = random.randint(0,255)
randB = random.randint(0,255)

#another random int from 0 to 1, testpos decides wether the text will be position to the top left or more towards the top left/center.
testPos = random.randint(0,1)
xPos=0
if testPos == 1:
	xPos = 350
#using text function lets use pick the position, set the text, set the font color and finally set the font style(from the ImageFont object created above)
textAdd.text((xPos,0),"Creepers Invaded My Mansion!",(randR,randG,randB), font = font)
#The Final Product is shown
fBgImg.show()
#Tested on a Windows PC, The Image opens up in Window's photo viewer as a temporary file and can be saved from there.
#With a bit more extra coding and an IO import, this code could ask users for inputs,
#and create a thumbnail based user's inputted background img file, foreground img file,
#and text string. An IO import could also save the file for the user instead of using their computer's photo viewer to save