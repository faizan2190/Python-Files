#Modifying example-1 to return area of circle too.
def circle(r):
    '''return the circumference of a circle'''
    return 3.14*r,3.14*r**2
print(circle.__doc__)
print(circle(5))
x=7
print(circle(x))
print(circle(3))
r=3
print(circle(r))