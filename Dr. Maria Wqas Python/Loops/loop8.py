# Write a Python program to display the first n terms of Fibonacci series. In Fibonacci series, first two terms are 0 and 1
# respectively, after that every term is the sum of the last two terms.
# Fibonacci series: 0 1 2 3 5 8 13 .....
# Expected Test Run:
# Input number of terms to display: 10
# Here is the Fibonacci series upto to 10 terms:
# 0 1 1 2 3 5 8 13 21 34
n=int(input('enter the number of terms to display...'))
a=0
b=1
for i in range(1,n+1):
    if i==1:
        print(a,end=' ')
    elif i==2:
        print(b,end=' ')
    else:
        c=a+b
        print(c,end=' ')
        a=b
        b=c
