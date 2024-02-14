# Write a function to input a list of integers from the user. The function returns the list to the caller.
def enter_list():
    lst=[]
    val=input('enter values separated by spaces:')
    val=val.split()
    val=[int(i) for i in val]
    for i in val:
        lst.append(i)
    return lst
print(enter_list())
