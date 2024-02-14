# Write code that accepts two parameters, a list of numbers and a number x. The code should print, in order, all the
# elements in the list that are at least as large as the number x.
def unknown(l,n):
    lst=[]
    for i in l:
        if i > n:
            lst.append(i)
    return lst
print(unknown([1,2,3,4,5,6,7],4))
