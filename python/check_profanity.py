import urllib

def read_text():
	quotes = open("/Users/paulqua/Desktop/movie_quotes.txt")
	contents_of_file = quotes.read()
	#print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	print (output)
	if output == "true":
		print "There is Profanity in the file!"
	elif output == "false":
		print "There is no Profanity in the file!"
	else:
		print "Could not read properly!"
	connection.close()
read_text()