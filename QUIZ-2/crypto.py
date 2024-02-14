import fileinput

file = open ('crypto.txt','r')
file = file.read()
file = file.split()
emptylist=[]
for i in file:
    if i == 'secret':
        emplyfile.append(i)
print(emptylist)