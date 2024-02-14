# Write a function called count_odd to count and return odd numbers in a list. The list is passed as argument to the
# function.
def count_odd(l):
    count=0
    odd_lst=[]
    for i in l:
        if i%2!=0:
            count+=1
            odd_lst.append(i)
    return count,odd_lst
print(count_odd([1,2,3,4,5]))