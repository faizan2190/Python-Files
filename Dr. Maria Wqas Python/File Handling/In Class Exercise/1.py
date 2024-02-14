# 1. Create a file named ‘myfile.txt’ containing the following text:

# First Line
# Second Line
# Third Line
# Last Line

# 2. Read this file ‘myfile.txt’ and print the following information about it:
#  Total number of characters in the file
#  Total number of words in the file
#  Total number of lines in the files
#  Total number of alphabets in the file
with open('myfile.txt','w+') as file:
    file.write('First Line\nSecond line\nthird Line\nForth Line')


