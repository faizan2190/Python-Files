file=open('data.txt','r')
content=file.read()
total=0
count=0
for i in content:
    if i.isdigit():
        total+=int(i)
        count+=1
print(total/count)