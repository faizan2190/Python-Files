value=input('enter the values separated by spaces:')
value=value.split()
value=[int(i) for i in value]
compare_value=int(input('enter the value you want to compare with:'))
newlist=[]
for i in value:
    if i > compare_value:
        newlist.append(i)
print(newlist)