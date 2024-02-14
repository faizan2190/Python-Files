def out_circle(r1):
    area=2*3.14*r1
    def in_circle():
        r2=float(input('enter the radius of in cicle:'))
        print('circumference=',2*3.14*r2)
    in_circle()
    print('area=',area)
r1=float(input('enter the radius of out circle:'))
out_circle(r1)
