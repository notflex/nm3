import numpy as np
import matplotlib.pyplot as plt
from sympy import integrate
from sympy import *
from sympy.abc import x

a = 1.0
b = 2.0

def get_func(x):
    return x * np.log(x)

def get_pervoobrazn(x):
    return x ** 2.0 (2.0 * np.log(x) - 1.0) / 4.0

def get_rectangle(n):
    sum = 0.0
    step = (b-a) / n
    y = a + step / 2
    for i in range(1, n+1):
        sum += get_func(y)
        y += step
    return sum * step

def get_trapetion(n):
    sum = 0.0
    step = (b-a) / (n-1)
    for i in range(n-1):
        sum += get_func(a + i * step) + get_func(a + (i + 1) * step)

    return sum * step / 2.0

def get_simpson(n):
    step = (b - a) / (n - 1)
    sum = 0.0
    for i in range(n - 1):
        sum += get_func(a + i * step) + 4 * get_func(a + i * step + step / 2) + get_func(a + (i + 1) * step)
    return sum * step / 6.0


if __name__=='__main__':
    var('x')
    func = x * ln(x)
    true_v = integrate(func, (x, a, b)).evalf()

    rect = []
    trap = []
    simp = []

    n = 11
    axis_x = list()
    for i in range(1, 9):
        axis_x.append((b-a) / (n-1))
        rect.append(abs(get_rectangle(n) - true_v))
        trap.append(abs(get_trapetion(n) - true_v))
        simp.append(abs(get_simpson(n) - true_v))
        n*=2

    plt.loglog(axis_x, rect, label='Rectangle')
    plt.loglog(axis_x, trap, label='trap')
    plt.loglog(axis_x, simp, label='simp')
    plt.legend()
    plt.grid()
    plt.show()