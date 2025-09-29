from math import *
x = float (input("Введите x: "))
y = float (input("Введите y: "))
z = float (input("Введите z: "))
if z < -1 or z > 1:
    print("Error: asin(z) is undefined for |z| > 1")
else:
    sqr = 10*(((x**(1/3)))+pow(x,y+2))
    if sqr < 0:
        print("Error: sqrt of negative number")
    else:
        b = sqrt(sqr) * (pow(asin(z),2) - fabs(x-y))
        print("b =", b)
