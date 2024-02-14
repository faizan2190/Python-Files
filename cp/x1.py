# Read this file ‘myfile.txt’ and print the following information about it:
#  Total number of characters in the file
#  Total number of words in the file
#  Total number of lines in the files
#  Total number of alphabets in the file
file=open('x.txt')
#total no of charecters
content=file.read()
print(len(content))
#total no of words:
words=content.split()
print(len(words))
#total no of lines:
lines=content.split('\n')
print(len(lines))
#totsl no of alphabets:
count=0
for i in content:
    if i.isalpha():
        count+=1
print(count)