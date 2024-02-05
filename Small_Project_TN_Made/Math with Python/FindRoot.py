from numpy import *

import time

def f():
    return lambda x: sin(x)
def g():
    return lambda x: sin(x) - 0.5

starting_x = 0
y_intersect = 0.5
n = 6


def find_root0(function, starting_x, y_intersect):
    x0 = starting_x
    dx = 0.001
    epsilon = 0.01
##################
    k = 0
    x = 0
    while abs(function(x) - y_intersect) > epsilon:
        x = x0 + k * dx
        k += 1

    return x, function(x)
def find_root1(function, starting_x, y_intersect, n):
    dx = 10
    epsilon = 100
    #############
    x = 0
    #############
    for i in range(1, n + 1):
        dx = dx / 10 ** i
        epsilon = epsilon / 10 ** i
        k = 0

        try:
            while abs(function(x) - y_intersect) > epsilon:
                x = starting_x + k * dx
                k += 1
        except KeyboardInterrupt:
            print(x)

        starting_x = x
    #############
    return x, function(x)
def find_root2(function, a, b, precision):
    # epsilon = 10**-4
    if function(a) * function(b) >= 0:
        raise ValueError("The fx values at 'a' and 'b' must have opposite signs.")

    while abs(b - a) > precision:
        c = (a + b) / 2
        if function(c) == 0:
            return round(c, 16)
        elif function(c) * function(a) < 0:
            b = c
        else:
            a = c
    x = round((a + b) / 2, 16)

    return x, function(x)


start = time.time()
x0, y_at_x0 = find_root0(f(), starting_x, y_intersect)
end = time.time()
print('x_root multi=', x0)
print('f(x_root) multi=', y_at_x0)
print('Time of find_root0 = ', end - start)
print('---')

start = time.time()
x2, y_at_x2 = find_root2(g(), 0, 1, 1e-9)
end = time.time()
print('x_root multi=', x2)
print('f(x_root) multi=', y_at_x2)
print('Time of find_root2 = ', end - start)
print('---')
'''
start = time.time()
xc, y_at_xc = find_root1(f(), x0, y_intersect, n)
end = time.time()
print('x_root com =', xc)
print('f(x_root) com =', y_at_xc)
print('Time = ', end - start)
print('---')
'''

start = time.time()
x1, y_at_x1 = find_root1(f(), starting_x, y_intersect, n)
end = time.time()
print('x_root =', x1)
print('f(x_root) =', y_at_x1)
print('Time of find_root1 = ', end - start)


