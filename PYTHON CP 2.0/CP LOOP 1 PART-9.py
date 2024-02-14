##Write a Python program to display the sum of the series [ 9 + 99 + 999 + 9999 ...].
##Expected Test Run:
##Input the number or terms: 5
##Series: 9 99 999 9999 99999
##Sum: 111105
terms=int(input('ENTER THE NUMBER OF TERMS:'))
Sum=0
for i in range(1,terms+1):
    print(str(9)*i,end=' ')
    Sum+=((10**i)-1)
print()
print(Sum)

    
