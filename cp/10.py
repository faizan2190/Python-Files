# Write code that accepts two parameters, a list of numbers and a number x. The code should print, in order, all the
# elements in the list that are at least as large as the number x.
l=[]
value=input('enter values separated by spaces:')
value=value.split()
value=[int(i) for i in value]
num=int(input('enter the comperision number:'))
for i in value:
    if i>num:
        l.append(i)
print(l)
