# Write a function called index that inputs a list and a value. If the value is present in the list it returns the indices of
# all its occurences in the form a tuple. If the value is not there, it returns an empty tuple. In the program use this return
# value to print appropriate messages. Do not call any method of object list.
def index(l,val):
    tu=()

    for i in range(len(l)):
        if l[i]==val:
            tu+=(i,)
            return tu
print(index([1,2,3,4,5,4,4],4))

