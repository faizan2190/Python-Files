f=open('val.txt')
value=f.read()
value=value.split()
total=0
for i in value:
    total+=int(i)
print(total/len(value))
print(value)