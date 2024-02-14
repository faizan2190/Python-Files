# Write a function Pytha that, given the lengths of the two sides of a right triangle adjacent to the right angle,
# computes the length of the hypotenuse of the triangle.
def pytha(a,b):
    c=((a**2)+(b**2))**0.5
    return c
print(pytha(3,4))