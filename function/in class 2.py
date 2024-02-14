# Write code that inputs a list and a value. If the value is present in the list it returns the index of its first occurrence,
# otherwise returns a None. In the main program use this return value to print appropriate messages. Do not call any
# method of object list.
def index(lst,value):
    for i in range(len(lst)):
        if lst[i]==value:
            return i
x=index([1,2,3,4,5],3)
print(x)
