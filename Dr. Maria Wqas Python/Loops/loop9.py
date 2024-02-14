# Write a Python program to display the sum of the series [ 9 + 99 + 999 + 9999 ...].
# Expected Test Run:
# Input the number or terms: 5
# Series: 9 99 999 9999 99999
# Sum: 111105
n=int(input('enter the number of terms:'))
sum=0
print('series',end=':')
for i in range(1,n+1):
    print(str(9)*i,end=' ')
    sum+=(10**i)-1
print()
print(f'sum:{sum}')