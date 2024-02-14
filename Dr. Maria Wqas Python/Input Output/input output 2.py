# Take five integer values from user, find average and print it on screen.
count=0
total=0
for i in range(5):
    num=int(input('enter an integer:'))
    count+=1
    total+=num
print(f'The average of the given numbers are {total/count}')
