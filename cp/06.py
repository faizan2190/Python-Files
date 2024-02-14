file=open('newfile.txt')
file=file.read()
file=file.split()
total=0
for i in file:
    total+=int(i)
print(total/len(file))