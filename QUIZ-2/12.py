# Read this file ‘myfile.txt’ and print the following information about it:
#  Total number of characters in the file
#  Total number of words in the file
#  Total number of lines in the files
#  Total number of alphabets in the file
f=open('new.txt','r')
#total no of charecters:
char=f.read()
print(len(char))
#total no of words:
word=char.split()
print(len(word))
#total no of lines:
lines=char.split('\n')
print(len(lines))
#total no of alphabets:
count=0
for i in char:
    if i.isalpha():
        count+=1
print(count)
f.close()