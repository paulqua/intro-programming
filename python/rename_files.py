import os

def renameFiles():
	file_list = os.listdir("/Users/paulqua/Desktop/prank")
	print file_list
	saved_path = os.getcwd()
	os.chdir("/Users/paulqua/Desktop/prank")
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
renameFiles()