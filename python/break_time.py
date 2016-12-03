import time 
import webbrowser

count = 0
breaks = 3
while count < breaks:
	time.sleep(10)
	webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
	count += 1