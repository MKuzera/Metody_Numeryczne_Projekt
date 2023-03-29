import numpy as np
# w Funckjach zmienic funkcje
# 1 metoda -> na numpy
# 2 metoda -> na zwyklych operacjach
#funkcja do quadra
# f11 do met_trap2

#Aktualnie liczy:
Co_liczy=  "f(x) = x^2 * cos^3(x)"


def quadrature_trapez(leftLimit, rightLimit, dx, fun):
    print("Funkcja: {} w zakresie od {} do {} w skoku {}".format(Co_liczy,leftLimit,rightLimit,dx))
    x = np.arange(leftLimit, rightLimit, dx)
    result = 0
    y = fun(x)
    return 0.5 * dx * ((y[0] + y[-1]) + 2 * np.sum(y[1:-1]))
def funkcja():
    f = lambda x: x**2 * (np.cos(x)**3)
    return f

    # print(quadrature_trapez(2, 6, 0.0000001, f)) # 3 argument to skok


# Druga metoda , n -> dokladnosc (ilosc trapezow)
def met_trapv2(f, a, b, n):
   x = np.array([0])
   h = (b - a) / n
   x = [a + i * (b - a) / n for i in range(n + 1)]

   wynik = (f(a) + f(b)) / 2
   for i in range(1, n):
      wynik += f(x[i])

   return wynik * h

def f11(x):
   return (x**2)*(np.cos(x)**3)

