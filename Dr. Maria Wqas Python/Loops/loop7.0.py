# Write a program that requests a positive four-digit integer from the user and prints its digits. You are not allowed to
# use the string data type operations to do this task. Your program should simply read the input as an integer and
# process it as an integer, using standard arithmetic operations (+, *, -, /, %, etc).
# Test Data:
# Enter n: 1234
# Expected Output:
# 1
# 2
# 3
# 4


# num=int(input('Enter the four digit number:'))
# tc=str(num)
# for i in tc:
#     print(i)

print(1234//1000)
print((1234%1000)//100)
print((1234%100)//10)
