#Scrabble HW Assignment            Michael S.        Comp 3320
def letterScore(letter):
	if letter in 'abcdefghijklmnopqrstuvwxyz':
		if letter in 'aeilnorstu':
			return 1
		if letter in 'dg':
			return 2	
		if letter in 'bcmp':
			return 3	
		if letter in 'fhvwy':
			return 4	
		if letter in 'k':
			return 5	
		if letter in 'jx':
			return 8
		if letter in 'qz':
			return 10
	else :
		return 0	
def wordScore(string):
	string = string.lower()
	totalScore = 0
	i = 0
	for i in range(len(string)):
		totalScore = totalScore + letterScore(string[i])
	return totalScore	

Word = input("Input a Word: ")
score = wordScore(Word)
print("The Word Score is: ",score)
