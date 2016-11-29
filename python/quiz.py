#This is the quiz for section 2 Project


#1 = browser, 2 = http, 3 = server, 4 = html
easy = 'Clients access the web using a web ___1___ on a personal computer of some sort. The client makes an ___2___ request to a server, where a particular website is hosted. The ___3___ sends back the requested file(s) and displays the page using ___4___ .'

#1 = Google, 2 = dev, 3 = option, 4 = css
medium = '___1___ Chrome has a cool function/section that allows you to see the parts of a webpage (html, ___4___ and javascript). To access this function you can find the ___2___ tools option in the top right corner menu area, or command ___3___ i on a mac. Here you can select an element to inspect and check out the html and ___4___ for that element. You can also see the tree branch like structure by clicking on the arrows next to the specified tags.'

#1 = Python, 2 = computer, 3 = algorithms, 4 Guido
hard = '___1___ is a backend language which allows you to write out solutions on how a ___2___ can solve problems. These solutions are also known as ___3___ . ___1___ got its name from its creator ___4___ van Rossum, who named it after the BBC series " Monty ___1___ " '

#correct answers for the easy quiz
easyChoice = ['browser', 'http', 'server', 'html']

#correct answers for the medium quiz
mediumChoice = ['Google', 'dev', 'option', 'css']

#correct answers for the hard quiz
hardChoice = ['Python', 'computer', 'algorithms', 'Guido']

#used for finding and replacing these in the quiz
missingWords = ['___1___', '___2___', '___3___', '___4___']

#printed at the end of the quiz
finish ='YOU HAVE COMPLTED THE QUIZ! CONGRATULATIONS!'

#used to keep track of how many times user has tried a specific question
errorCount = []

#used in the filler function else statement for max amount of tries per question
maxTries = 5

#function asks the questions from user, then passes info to filler function, then receives it back again just like a while loop
def quiz(level, choices, count): 
	print level
	if count < len(missingWords):
		answer = raw_input('WHAT SHOULD BE IN SPOT ' + missingWords[count] +'?' ' ')
		filler(answer, count, level, choices)
	else:	
		print finish
	
#function lets user choose a level of easy, medium or hard
def chooseLevel(level): 
	count = 0
	if level == 'easy':
		print 'YOU HAVE CHOSEN EASY!'
		return quiz(easy, easyChoice, count)
	elif level == 'medium':
		print 'YOU HAVE CHOSEN EASY!'
		return quiz(medium, mediumChoice, count)
	elif level == 'hard':
		print 'YOU HAVE CHOSEN EASY!'
		return quiz(hard, hardChoice, count)
	else:
		print 'Please enter a valid choice of: easy, medium or hard. Please use all lowercase.'

#counts how many times the user has tried to answer the question and got it wrong
def error(count): 
	ecount = 0
	errorCount.append(count)
	for index in errorCount:
		if index == count:
			ecount +=1
	return ecount

#updates the selected paragraph with the correct answers if correct. Else, prints out incorrect statement and counts down tries
def filler(answer, count, update, choices): 
	finalList = []
	if answer == choices[count]:
		print 'CORRECT!'
		update = update.split()
		for word in update:
			if word == missingWords[count]:
				finalList.append(choices[count])
			else:
				finalList.append(word)
		update = ' '.join(finalList)
		count += 1
		quiz(update, choices, count)
	else:
		print 'YOUR ANSWER WAS INCORRECT, PLEASE TRY AGAIN.'
		error_count = error(count)
		if error_count < maxTries:
			print 'YOU HAVE', maxTries - error_count, 'TRIES LEFT.'
			quiz(update, choices, count)
		else:
			print 'You have used up all your chances. Game Over!'


userInput = raw_input('What level do you want? easy, medium or hard:' ' ')
chooseLevel(userInput)



	
		




