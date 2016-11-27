#This is the quiz for section 2 Project


#1 = browser, 2 = http, 3 = server, 4 = html
easy = 'Clients access the web using a web ___1___ on a personal computer of some sort. The client makes an ___2___ request to a server, where a particular website is hosted. The ___3___ sends back the requested file(s) and displays the page using ___4___.'

#1 = Google, 2 = dev, 3 = option, 4 = css
medium = '___1___ Chrome has a cool function/section that allows you to see the parts of a webpage (html, ___4___ and javascript). To access this function you can find the ___2___ tools option in the top right corner menu area, or command ___3___ i on a mac. Here you can select an element to inspect and check out the html and ___4___ for that element. You can also see the tree branch like structure by clicking on the arrows next to the specified tags.'

#1 = Python, 2 = computer, 3 = algorithms, 4 Guido
hard = '___1___ is a backend language which allows you to write out solutions on how a ___2___ can solve problems. These solutions are also known as ___3___. ___1___ got its name from its creator ___4___ van Rossum, who named it after the BBC series "Monty ___1___" '

easyChoice = ['browser', 'http', 'server', 'html']

mediumChoice = ['Google', 'dev', 'option', 'css']

hardChoice = ['Python', 'computer', 'algorithms', 'Guido']

missingWords = ['___1___', '___2___', '___3___', '___4___']

finish ='You have completed the quiz! Congratulations!'

def quiz(level, choices, count):
	
	print level
	if count < len(missingWords):
		answer = raw_input('What should be in spot ' + missingWords[count] +'?' ' ')
		filler(answer, count, level, choices)
		

	else:	#print updateSentence
		return finish
	

def chooseLevel(level): #function lets user choose a level of easy, medium or hard
	count = 0
	if level == 'easy':
		return quiz(easy, easyChoice, count)
	if level == 'medium':
		return quiz(medium, mediumChoice, count)
	if level == 'hard':
		return quiz(hard, hardChoice, count)
	else:
		print 'Please enter a valid choice of: easy, medium or hard. Please use all lowercase.'

def filler(answer, count, update, choices): #updates the selected paragraph with the correct answers
	#update = update.split()
	if answer == choices[count]:
		print 'Correct!'
		count += 1
		quiz(update, choices, count)
	else:
		print 'Your answer was incorrect, please try again.'
		#update = ' '.join(update)
		quiz(update, choices, count)

	

userInput = raw_input('What level do you want? easy, medium or hard:' ' ')
chooseLevel(userInput)



	
		




