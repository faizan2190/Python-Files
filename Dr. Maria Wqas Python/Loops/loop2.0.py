# Write a Python program that allows the user to enter exactly twenty floating-point values. The program then prints the
# sum, average (arithmetic mean), maximum, and minimum of the values entered.
l=[]
for i in range(20):
    num=float(input('enter a float value'))
    l.append(num)
print(sum(l))
print(max(l))
print(min(l))
print(sum(l)/20)