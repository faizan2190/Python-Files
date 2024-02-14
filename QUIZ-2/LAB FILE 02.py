#Develop a script that print the word of file by comma separate:
f=open('hello.txt','r')
f=f.read()
f=f.split()
print(f)
for i in f:
    print(i,end=',')
