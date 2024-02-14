# Write a function to input a list of integers from the user. The function receives an empty list from user.
def enter_list(l):
    value=input('enter values separated by spaces:')
    value=value.split()
    value=[int(i) for i in value]
    for i in value:
        l.append(i)
    return l

l=[]
print(enter_list(l))