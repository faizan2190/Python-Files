# Read this file ‘myfile.txt’ and print the following information about it:
#  Total number of characters in the file
#  Total number of words in the file
#  Total number of lines in the files
#  Total number of alphabets in the file
file=open('myfile.txt')
#total no of charecters:
text=file.read()
print(len(text))
#total no of words:
words=text.split()
print(len(words))
#total no of lines:
lines=file.seek(0)
lines=file.readlines()
print(len(lines))
#total no of alphabets:
count=0
for i in text:
    if i.isalpha():
        count+=1
print(count)
file.close()