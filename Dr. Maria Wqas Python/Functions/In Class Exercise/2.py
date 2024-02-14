# Write code that inputs a list and a value. If the value is present in the list it returns the index of its first occurrence,
# otherwise returns a None. In the main program use this return value to print appropriate messages. Do not call any
# method of object list.
def index(lst,val):
    for i in range(len(lst)):
        if lst[i]==val:
            return i
print(index([1,2,3,4,5,2],8))