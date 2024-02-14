#Write code that accepts two parameters, a list of numbers and a number x. The code should print, in order, all the
#elements in the list that are at least as large as the number x.
l=[]
num=input('enter the member of list seperated by space:')
num2=int(input('enter the comparision number'))
num=num.split()
num=[int(i) for i in num]
for i in num:
    if i>num2:
        l.append(i)
print(l)
