# Write code to input three angles of a triangle and check if the triangle is valid or not.
total=0
for i in range(3):
    angle=int(input('Enter an angle '))
    total+=angle
if total==180:
    print('Triangle is valid')
else:
    print('Triangle is not valid')

