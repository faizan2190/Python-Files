# Write a function to input a list of integers from the user. The function returns the list to the caller.
def lst_input():
    values=input('enter integers separated by space')
    values=values.split()
    values=[int(i) for i in values]
    return values
l=lst_input()
print(l)