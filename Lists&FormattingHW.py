import math
from math import *
list = [pi]
for i in range(2,6):
    a = math.pow(pi,i)
    list.append(a)
for a in list:
    print('%.15f' % (a), end='')


print('')
symbol = '.' * 16
print('.' * 16, end='')
print('%33s' % symbol, end='')
print('%33s' % symbol)

for b in list:
    print('   %-14.8s' % b, end='')
print()
for c in range(1,6):
    d=0
    d = c*pi
    print('   %-14.8s' % d, end='')