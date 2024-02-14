# Write a function to count and return negative values in a list. The list is passed as argument to the function.
def negative_count(l):
    l1=[]
    count=0
    for i in l:
        if i < 0:
            count+=1
            l1.append(i)

    return count,l1
l=[1,2,3,-4,-5,-7,3,4]
x=negative_count(l)
print(x[0])
print(x[1])