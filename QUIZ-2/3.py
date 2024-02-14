# Write code that accepts two parameters, a list of numbers and a number x. The code should print, in order, all the
# elements in the list that are at least as large as the number x.
lst=input('enter an integers seperated by space:')
unknown=int(input("enter the number you want to compare with:"))
lst=lst.split()
lst=[int(i) for i in lst]
final_lst=[]
for i in lst:
    if i > unknown:
        final_lst+=[i]
print(f'The list of the numbers greater then {unknown} is: {final_lst}')
