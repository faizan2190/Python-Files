# 2. Read this file ‘myfile.txt’ and print the following information about it:
#  Total number of characters in the file
#  Total number of words in the file
#  Total number of lines in the files
#  Total number of alphabets in the file
with open('myfile.txt','r') as file:
    count=0
    content=file.read()
    print(len(content))
    word=content.split()
    print(len(word))
    lines=content.split('\n')
    print(len(lines))
    for i in content:
        if i.isalpha():
            count+=1
    print(count)