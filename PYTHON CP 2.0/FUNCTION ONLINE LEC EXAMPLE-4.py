#Accessing the value of tuple
def circle(r):
    area=3.14*r**2
    cir=3.14*r
    return area,cir
result=circle(5)
print(result[0],result[1])