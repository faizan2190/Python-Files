# Write a function that finds average of the numbers passed to it. The input to the function should be variable length
# argument.
def ave(*args):
    total=0
    for i in args:
        total+=i
    average=total/len(args)
    return average
print(ave(1,2,3,4,5,6))
