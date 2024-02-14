# Write a function to input a list of integers from the user. The function receives an empty list from user.
def lst_input(lst):
    values=input('enter integers separated by space:')
    values=values.split()
    lst+=[int(i) for i in values]
l=[]
lst_input(l)
print(l)