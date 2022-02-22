# import os
# print(os.name)


# import os
# fd = "file"

# # popen() is similar to open()
# file = open(fd, 'w')
# file.write("Hello")
# file.close()
# file = open(fd, 'r')
# text = file.read()
# print(text)

# # popen() provides a pipe/gateway and accesses the file directly
# file = os.popen(fd, 'w')
# file.write("Hello")
# File not closed, shown in next function.



# import os
# os.remove("file1") #removing the file.

import os

result = os.path.exists("f_1") #giving the name of the file as a parameter.
print(result)


import os
size = os.path.getsize("f_1")

print(f"Size of the file is {size} bytes.")