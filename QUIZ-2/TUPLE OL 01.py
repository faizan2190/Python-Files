#Find the minimum value from a predefine tuple having five value using for loop:
tu=6,2,3,-65,4,5
min_val=tu[0]
for i in tu:
    if i < min_val:
        min_val=i
print(min_val)
