# def bananas():
#         print('No way, no how.')
# def groceries():
#     print("milk")
#     print("eggs")
#     print("sugar")
#     print("blah")
#     bananas()

# groceries()

# def blend(power, minutes):
#     print (power * minutes)

# for i in range(0, 10):
#     p = i * 3
#     n = i * 6
#     blend(p,n)

# def addtwo(value):
#     print(value + 2)

# addtwo(9997)
# from math import sqrt

# def quadratic(a, b, c):
#     x1 = -b / (2*a)
#     x2 = sqrt(b**2 - 4*a*c) / (2*a)
#     return (x1 + x2), (x1 - x2)

# call = quadratic(a = 2, b = 4, c = 7)
# print(call)

# def F2C(nDegreesF):
#     nDegreesC = (nDegreesF - 32) * (5.0 / 9.0)
#     return nDegreesC
# def C2F(nDegreesC):
#     nDegreesF = (1.8 * nDegreesC) + 32
#     return nDegreesF

# print(C2F(int(input("It's pretty cold outside, huh? How cold is it?"))))

# rectL = input("Length of our rectangle?")
# rectH = input("Height of your rectangle?")

# def area(rectL, rectH):
#     return rectL * rectH

# area()

# from turtle import *
# up()
# forward(50)
# left(90)
# forward(50)
# left(90)
# down()
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# mainloop()

from turtle import *
for i in range(5):
    forward(100)
    right(144)
mainloop()