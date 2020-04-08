# Michael S.    Comp 3320   Python  Project Assignment #2  Arrow Showcase
#Written using Sublime Text: use toggle block comment to enable/disable examples; highlight then ctrl+shift+/ on Sublime
#Showcase Title: 3 simple programs to show off arrow
#---------------------------------------------------------------------------------------
##Timezone Converter
#conversion between timezones and built in format function
import arrow
#Creates a datetime based on the current time in pacific
now = arrow.now("US/Pacific")
#takes the previously created times zone and converts it to eastern 
nowA = now.to("US/Eastern")

nowB = now.to("GMT")
nowC = now.to("UTC")
nowD = now.to("Europe/London")
#prints the times using the format function, shows a few of the tokens possible
print(now.format("YYYY, MMMM dddd Do hh:mm:ss A ZZZ"))
print()
print("Year "+ nowA.format("YY MMM ddd D,  h:mm:ss A ZZZ"))
print()
print(nowB.format("YYYY, MMMM dddd Do hh:mm:ss A ZZZ"))
print(nowC.format("YYYY, MMMM dddd Do hh:mm:ss A ZZZ"))
print(nowD.format("YYYY, MMMM dddd Do hh:mm:ss A ZZZ"))

#---------------------------------------------------------------------------------------
##Age Calculator
# #Showcasing of the get function and humanize to calucate age in years, minutes, and in everything possible.
# import arrow
# #Current time to gather our current age
# now = arrow.now("US/Eastern")
# #The String which the date will be retrieved from *You could replace January 7 1998 with your own birthdate; must match MMMM D YYYY format ex: December 9 2000 
# birthday = "My Birthday is on January 7 1998 ! "
# #the get function retrieves the date from the birthday string * format must match with how the date appears in the string
# HBday= arrow.get(birthday, "MMMM D YYYY")
# #age in years      - only_distance checks only gets the time from HBday to Now, otherwise the humanize function would return 22 years ago
# print("You are "+ HBday.humanize(now, only_distance=True)+ " old")
# print()
# #age in minutes
# print("You are "+ HBday.humanize(now, only_distance=True, granularity="minute")+ " old")
# print()
# #age in every possible granulity
# print("You are "+ HBday.humanize(now, only_distance=True, granularity=["year","month","week","hour","minute","second"])+ " old")
# print()

#---------------------------------------------------------------------------------------
# #How Long since/ How long till    Shifting showcase
# import arrow
# import random
# rDay = random.randint(-30,30)
# rYear = random.randint(-1,1)
# rMinute = random.randint(-600,600)
# rSeconds= random.randint(-120,120)

# now = arrow.now("US/Eastern")
# #Shifts the current data by random integers, positive integers shift foward and negative shift back
# nowS=now.shift(days=rDay,years=rYear , minutes=rMinute, seconds= rSeconds)

# print("The Current date is "+ now.format("dddd, MMMM Do YYYY")+". Current Time is "+ now.format( "hh:mm:ss A ZZZ"))
# print()
# print("Shifting Dates!")
# print(nowS.humanize(now,granularity=["year","month","week","hour","minute","second"]))
# print()
# #prints out the Shifted Dates
# print("The shifted date is "+ nowS.format("dddd, MMMM Do YYYY")+". Shifted Time is "+ nowS.format( "hh:mm:ss A ZZZ"))
