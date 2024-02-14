# Write code to find average of five non-negative integers entered by the user and print average.
total=0
for i in range(5):
    num=int(input('enter a non negative integers:'))
    total+=num
print(f'Average of a given numbers are {total/5}')