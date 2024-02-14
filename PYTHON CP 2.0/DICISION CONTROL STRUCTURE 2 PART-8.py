##Write a Python program to check whether the triangle is equilateral, isosceles or scalene triangle. In equilateral
##triangle all three sides are equal, in isosceles triangle any two sides are equal, and in scalene triangle none of the three are equal
angle1=int(input('ENTER AN ANGLE'))
angle2=int(input('ENTER AN ANGLE'))
angle3=int(input('ENTER AN ANGLE'))
if angle1+angle2+angle3==180:
    if angle1==angle2 and angle2==angle3 and angle1==angle3:
        print('equilatrial triangle')
    elif angle1==angle2 or angle1==angle3 or angle2==angle3:
        print('isosceles triangle')
    else:
        print('scales triangle')
else:
    print('triangle is not valid')
