# file = open('my_file.txt')  # opens the file, 'my_file' as 'file'
# content = file.read()  # read() method returns the content of the file
# print(content)
# file.close()   # as you open anything, don't forget to close it, for better performance of your computer

# # we indeed, forget closing stuff, so most developers prefer opening files in below manner:
# with open('my_file.txt') as file:
#     content = file.read()
#     print(content)
# # file closes automatically using above keywords 'with' and 'as'.

# with open('my_file.txt', mode='w') as file:  # mode is 'r' (read) by default
#     file.write('New text.')  # erases previous data, and writes up whatever you put in parenthesis

# # append:
# with open('my_file.txt', mode='a') as file:
#     file.write('\nNew text.')  # appends data to the file

# # if you open a file in 'w'(write mode) that doesn't exist, the file gets created automatically
# with open('my_other_file.txt', mode='w') as file:
#     file.write('New text.')


# # file paths:

# absolute file path
# file path is given relative to the root (C drive in most cases)
# ex: absolute file path of current file: "C:/Users/User/PycharmProjects/pythonProject/py_zipped/week4/files.py"

# relative file path
# file path is given relative to current working directory
# ex: relative file path of current file (relative to current working directory(week4)): "files.py"
# we can get hold of current working directory by "./"
# ex: relative file path of my_file.txt: (since it is in same hierarchical level of files.py) 'my_file.txt'
#                                         or can also be written as './my_file.txt'
# "../" is used to go a level up from the present working directory

# note: in mac, forward slash '/' is used to separate directories in file paths
#       in windows, backward slash '\' is used to separate directories in file paths
# but in python, be it mac or windows, we can use forward slash '/'

