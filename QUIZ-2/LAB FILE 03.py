#Print the longest word in the file:
x=''
f=open('hello.txt')
f=f.read()
f=f.split()
for i in f:
    if len(i)>len(x):
        x=i
print(x)