#input 5 integer values from user and place them in a list:
l=[]
value=input('enter five values separated by spaces:')
value=value.split()
value=[int(i) for i in value]
#l+=value
for i in value:
    l.append(i)
print(l)