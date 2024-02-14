#Write a function to count ODD values in a list.
def odd(list):
    count=0
    for i in list:
        if i%2!=0:
            count+=1
    return count
list=[1,2,3,4,5,6,7,8,9]
odd_list=odd(list)
print(odd_list)