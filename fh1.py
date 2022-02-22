# basename function
import os
out = os.path.basename("/baz/foo")
print(out)


# dirname function
import os
out = os.path.dirname("/baz/foo")
print(out)

# isabs function - absolute path
import os
out = os.path.isabs("/baz/foo")
print(out)

# isdir function
import os
out = os.path.isdir("C:\\Users")
print(out)


# isfile function
import os
out = os.path.isfile("C:\\Users\foo.csv")
print(out)


# normcase function in windows
import os
out = os.path.normcase("/BAz")
print(out)


# normpath function in Unix
import os
out = os.path.normpath("foo/./bar")
print(out)


import os
cwd = os.getcwd()
print("Current working directory:", cwd)




# Get the list of all files and directories in the root directory
import os

# path = "/"
path = "/home/rao/Documents/pyPro"
dir_list = os.listdir(path)

print(f"Files and directories in {path}:")
print(len(dir_list), dir_list)
