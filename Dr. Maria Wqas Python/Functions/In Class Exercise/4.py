# Write a function to input a list of integers from the user. The function receives an empty list from user.
def func(l):
    val=input('Enter values separated by space')
    val=val.split()
    val=[int(i) for i in val]
    # l.extend(val)
    l+=val
    return l
l=[]
print(func(l))