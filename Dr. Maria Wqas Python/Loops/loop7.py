# Write a Python program to display the n terms of harmonic series and their sum.
# Harmonic series: 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms
# Expected Test Run:
# Input the number of terms : 5
# Series: 1/1 + 1/2 + 1/3 + 1/4 + 1/5
# Sum: 2.283334
num=int(input('enter a number for harmonic series:'))
total=0
for i in range(1,num+1):
    if i!=(num):
        print(f' 1/{i} +',end=' ')
        total+=1/i
    else:
        print(f' 1/{i}')
total+=1/num
print(total)
