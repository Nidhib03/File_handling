# Deleting Directory or Files using Python
# Python program to explain os.remove() method
import os

file = 'file.txt'	
location = "/home/rao/Documents/pyPro"
path = os.path.join(location, file)

os.remove(path)



# # Or

# # Python program to explain os.rmdir() method
import os
	
directory = "fileh"
parent = "/home/rao/Documents/pyPro/v_env"
path = os.path.join(parent, directory)

os.rmdir(path)
