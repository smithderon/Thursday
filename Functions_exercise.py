#1
# name = input ("What's your name?")
# def greeting(x):
#     return print(f"Hello,{x}!")

# greeting(name)

#2

# import matplotlib.pyplot as plot 

# def f(x): 
#      return x + 1

# xs = list(range(-3, 4)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

#3

# import matplotlib.pyplot as plot 

# def f(x):
#     return x * x
# xs = list(range(-100, 100, 1)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

#4

# import matplotlib.pyplot as plot 

# def f(x):
#     if x % 2 == 0:
#         return 1
#     if x % 2 == 1 or x % 2 == -1:
#         return -1

# xs = list(range(-5, 5)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.bar(xs, ys) 
# plot.show()

#5

# import matplotlib.pyplot as plot 
# from math import sin

# def f(x):
#     return sin(x)

# xs = list(range(-5, 5)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

#6

# import matplotlib.pyplot as plot 
# from math import sin
# from numpy import arange
# def f(x):
#     return sin(x)

# xs = arange(-5, 6, 0.1)
# ys = []

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

#7

# import matplotlib.pyplot as plot 
# def f(x):
#     x = (1.8 * x) + 32
#     return x


# xs = range( - 5, 20, 2)
# ys = []

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

#8

# def game():
#     so = str(input("Wanna play a game? (Y/N)"))
#     if so == "Y" or so == "y":
#         return True
#     if so == "N" or so == "n":
#         return False

# print(game())

#9

def game():
    so = str(input("Wanna play a game? (Y/N)"))
    while so == so:
        if so == "Y" or so == "y":
            return True
        if so == "N" or so == "n":
            return False
        else:
            print ("Sorry, that's an invalid answer.")
            return game()

print(game())