import math

import numpy as np
from numpy import array, zeros, fabs, linalg



# kwadratury wymaga jako argumentu funkcji (x) , w pythonie nie udalo mi sie
# pomnozyc funckje razy funkcje aby w rezultacie otrzymac funkcje
# a inne rozwiazania tez nie daja efektu
# Chwilowym wyjsciem bylo utowrzenie tablic z gotowymi funkcjami

#def funkcja_razy_x_do_potegi(fun,i):
#    if i == 0:
#        return 1
#    if i == 1:
#        return fun
#    for j in range(0,i):
#        fun = np.multiply(fun , funckja_x)
#
#    return fun

# dla innych funkcji wystraczy utowrzyc kilka gotowych funkcji wymnozonych przez x i utrozyc ich tablice.
# To jest do poprawy , na zajeciach zabraklo czasu to usprawnienia tego.

def funkcja_ex(x):
    return (math.exp(x) * math.sin(x/2)) - x*x*x

def funkcja_ex_razy_x(x):
    return ((math.exp(x) * math.sin(x/2)) - x*x*x) *x

def funkcja_ex_razy_x2(x):
    return ((math.exp(x) * math.sin(x/2)) - x*x*x) *x*x

def funkcja_ex_razy_x3(x):
    return ((math.exp(x) * math.sin(x/2)) - x*x*x) *x*x*x

def funkcja_ex_razy_x4(x):
    return ((math.exp(x) * math.sin(x/2)) - x*x*x) *x*x*x*x

def funkcja_ex_razy_x5(x):
    return ((math.exp(x) * math.sin(x/2)) - x*x*x) *x*x*x*x*x






def funckja_1(x):
  return 1
def funckja_x(x):
  return x
def funckja_x2(x):
  return x*x
def funckja_x3(x):
  return x*x*x
def funckja_x4(x):
  return x*x*x*x
def funckja_x5(x):
  return x*x*x*x*x
def funckja_x6(x):
  return x*x*x*x*x*x
def funckja_x7(x):
  return x*x*x*x*x*x*x
def funckja_x8(x):
  return x*x*x*x*x*x*x*x
def funckja_x9(x):
  return x*x*x*x*x*x*x*x*x
def funckja_x10(x):
  return x*x*x*x*x*x*x*x*x*x


def funckja_razy_1(x):
  return math.sin(x)
def funckja_razy_x(x):
  return math.sin(x)*x
def funckja_razy_x2(x):
  return math.sin(x)*x*x
def funckja_razy_x3(x):
  return math.sin(x)*x*x*x
def funckja_razy_x4(x):
  return math.sin(x)*x*x*x*x
def funckja_razy_x5(x):
  return math.sin(x)*x*x*x*x*x
def funckja_razy_x6(x):
  return math.sin(x)*x*x*x*x*x*x

functions_x_pow = [funckja_1,funckja_x,funckja_x2,funckja_x3,funckja_x4,funckja_x5,funckja_x6,funckja_x7,funckja_x8,funckja_x9,funckja_x10]
functions_of_sinus = [funckja_razy_1, funckja_razy_x, funckja_razy_x2, funckja_razy_x3,funckja_razy_x4,funckja_razy_x5,funckja_razy_x6]
functions_of_ex = [funkcja_ex,funkcja_ex_razy_x,funkcja_ex_razy_x2,funkcja_ex_razy_x3,funkcja_ex_razy_x4,funkcja_ex_razy_x5]


def gauss_2(a,b): # z zeszlych zajec

    n = len(b)
    x = zeros(n, float)
    for k in range(n - 1):
        if fabs(a[k, k]) < 1.0e-12:

            for i in range(k + 1, n):
                if fabs(a[i, k]) > fabs(a[k, k]):
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break

        for i in range(k + 1, n):
            if a[i, k] == 0: continue

            factor = a[k, k] / a[i, k]
            for j in range(k, n):
                a[i, j] = a[k, j] - a[i, j] * factor
            b[i] = b[k] - b[i] * factor

    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_ax = 0

        for j in range(i + 1, n):
            sum_ax += a[i, j] * x[j]

        x[i] = (b[i] - sum_ax) / a[i, i]

    return x

def simpsonQuadrature(leftLimit, rightLimit, dx, fun): # z zeszlych zajec , dx- skok
  s = 0
  st = 0
  size = (rightLimit - leftLimit) / dx + 1
  for i in range(1, int(size)):
    x = leftLimit + i * dx
    st += fun(x - dx / 2)
    if i < size:
      s += fun(x)

  return dx / 6 * (fun(leftLimit) + fun(rightLimit) + 2 * s + 4 * st)
