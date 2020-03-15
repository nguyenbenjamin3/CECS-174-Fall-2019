import math
from math import *


def afact(x):
    a = 1
    for i in range(1, x + 1):
        a = a * i
    return a


def power(x , y):
    k = 1
    for i in range(y):
        k *= x
    return k


def acos(x):
    k = 0
    for i in range(12):
        k += (((-1) ** i) * (x ** (2 * i))) / (afact(2 * i))
    return k


def asin(x):
    k = 0
    for i in range(12):
        k += (((-1) ** i) * (x ** (2 * i + 1)))/ (afact(2 * i + 1))
    return k


user_input = input('Do you want the sin or cos?\n')
angle = int(input('What angle do you want?\n'))
angle = (angle / 180) * pi

theirssin = math.sin(angle)
theirscos = math.cos(angle)

if user_input.strip() == 'cos':
    lol = acos(angle)
    print('%.16f Theirs %.16f' % (lol, theirscos))
if user_input.strip() == 'sin':
    lol = asin(angle)
    print('%.16f Theirs %.16f' % (lol, theirssin))
