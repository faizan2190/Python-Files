# Read this file ‘myfile.txt’ and print the following information about it:
#  Total number of characters in the file
#  Total number of words in the file
#  Total number of lines in the files
#  Total number of alphabets in the file
f=open('file.txt')
f=f.read()
#total no of charecters:
print(len(f))
#total no of words:
words=f.split()
print(len(words))
#total no of lines
lines=f.split('\n')
print(len(lines))
#total no of alphabet:
count=0
for i in f:
    if i.isalpha():
        count+=1
print(count)