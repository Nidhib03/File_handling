
# Python program to change the current working directory
# import os
# def current_path():
# 	print("Current working directory before", os.getcwd())
# 	print()
# current_path()
# os.chdir('/home/rao/Documents/pyPro/v_env')
# print("Changed directory: ",os.getcwd())


# # Python program to explain os.mkdir() method
import os
directory = "file"
parent_dir = "/home/rao/Documents/pyPro/v_env"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

directory = "fileh"
parent_dir = "/home/rao/Documents/pyPro/v_env"

mode = 0o666
path = os.path.join(parent_dir, directory)

os.mkdir(path, mode)
print("Directory '% s' created" % directory)
