#QUESTION-03
length=''
f=open('values.txt')
f=f.read()
f=f.split()
for i in f:
    if len(i)>len(length):
        length=i
print(length)