#Write a function to count negative values in a list.
def neg(list):
    count=0
    for i in list:
        if i<0:
            count+=1
    return count
list=[3,2,-33,4,-60,0,1,-92]
negative_count=neg(list)
print(negative_count)
