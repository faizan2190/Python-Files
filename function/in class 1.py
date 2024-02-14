# Write a function to count and return negative values in a list. The list is passed as argument to the function.
def neg_val(l):
    neg_list=[]
    count=0
    for i in l:
        if i < 0:
            count+=1
            neg_list.append(i)
    return neg_list,count
lst=[1,-2,-4,9]
x=neg_val(lst)
print(x[0])
print(x[1])