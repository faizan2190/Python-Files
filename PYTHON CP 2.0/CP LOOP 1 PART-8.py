##Write a Python program to display the first n terms of Fibonacci series. In Fibonacci series, first two terms are 0 and 1
##respectively, after that every term is the sum of the last two terms.
##Fibonacci series: 0 1 2 3 5 8 13 .....
##Expected Test Run:
##Input number of terms to display: 10
##Here is the Fibonacci series upto to 10 terms:
##0 1 1 2 3 5 8 13 21 34
a=0
b=1


limit=int(input('ENTER THE LIMIT:'))
print(0,1)
for i in range(0,limit+1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    ###kuch error hay isme logical
    
