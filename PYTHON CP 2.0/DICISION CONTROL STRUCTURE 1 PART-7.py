##Write code to input three angles of a triangle and check if the triangle is valid or not.
angle1=int(input('ENTRE AN ANGLE:'))
angle2=int(input('ENTRE AN ANGLE:'))
angle3=int(input('ENTRE AN ANGLE:'))
if angle1+angle2+angle3==180:
    print('TRIANGLE IS VALID')
else:
    print('triangle is not valid')
