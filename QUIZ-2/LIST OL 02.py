#Find maximum value from a predefined list of 5 values using for loop.
l=[1,2,3,4,5,55,6]
large_val=l[0]
for i in l:
    if i > large_val:
        large_val=i
print(large_val)