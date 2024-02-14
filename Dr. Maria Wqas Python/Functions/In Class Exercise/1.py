# Write a function to count and return negative values in a list. The list is passed as argument to the function.
def neg_count(lst):
    neg_lst=[]
    count=0
    for i in lst:
        if i < 0:
            count+=1
            neg_lst.append(i)

    return count,neg_lst
print(neg_count([1,2,-4,-3,-5,2,3,-6]))