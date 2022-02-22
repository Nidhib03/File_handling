import os
print(os.name)    # posix


 # os.popen(): This method opens a pipe to or from command
fd = "file.txt"       
# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello")
# File not closed, shown in next function.

 # removing the file.
os.remove("file1")  

 # giving the name of the file as a parameter.
result = os.path.exists("f_1") 
print(result)


size = os.path.getsize("f_1")
print(f"Size of the file is {size} bytes.")
