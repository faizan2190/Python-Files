def avg(*args):
    total=0
    for i in args:
        total+=i
    return total/len(args)
#args=(8,9,10)
print(avg(8,9))