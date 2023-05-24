import numpy as np
from matplotlib import pyplot as plt
#f - funkcja f z rownania
#x0-wartosc poczatkowa
#t0-czas poczatkowy
#tk-czas koncowy
#h-krok czasowy
# x[i-1] -> yn
# t[i-1] -> xn

alfa = 10**-12
beta = 0
def funckja_2(t,y):
  return -alfa*(y*y*y*y - beta)
def f(t,y):
  return y

def Euler(f, x0, t0, tk, h):
  t = np.arange(t0, tk, h)
  N = len(t)
  if hasattr(x0, "__len__"):
    x = np.zeros((N, len(x0)))
  else:
    x = np.zeros(N)
  x[0] = np.array(x0)
  i = 1
  while (i < N):
    x[i] = np.array(x[i - 1] + h * f(t[i - 1], x[i - 1]))
    i += 1
  return t, x
def Heun(f, x0, t0, tk, h):
    t = np.arange(t0, tk, h)
    N = len(t)
    if hasattr(x0, "__len__"):
      x = np.zeros((N, len(x0)))
    else:
      x = np.zeros(N)
    x[0] = np.array(x0)
    i = 1
    while (i < N):
      k1 = f(t[i - 1], x[i - 1])
      k2 = f(t[i - 1] + h * 0.5, x[i - 1] + 0.5 * h * k1)
      x[i] = np.array(x[i - 1] + h * 0.5 * (k1 + k2))
      i += 1
    return t, x

def Pkt_srod(f, x0, t0, tk, h):
  t = np.arange(t0, tk, h)
  N = len(t)
  if hasattr(x0, "__len__"):
    x = np.zeros((N, len(x0)))
  else:
    x = np.zeros(N)
  x[0] = np.array(x0)
  i = 1
  while (i < N):
    x[i] = np.array(x[i-1] + h * f(t[i-1] + h*0.5, x[i-1] + h *0.5*f(t[i-1], x[i-1])   ))
    i += 1
  return t, x

def RK4(f, x0, t0, tk, h):
  t = np.arange(t0, tk, h)
  N = len(t)
  if hasattr(x0, "__len__"):
    x = np.zeros((N, len(x0)))
  else:
    x = np.zeros(N)
  x[0] = np.array(x0)
  i = 1
  while (i < N):
    k1 = h * f(t[i - 1], x[i - 1])
    k2 = h * f(t[i - 1] + h * 0.5, x[i - 1] + 0.5 * k1)
    k3 = h * f(t[i - 1] + h * 0.5, x[i - 1] + 0.5 * k2)
    k4 = h * f(t[i - 1] + h, x[i - 1] + k3)
    x[i] = np.array(x[i - 1] + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6)
    i += 1
  return t, x


# Kod z zajec:


# if __name__ == '__main__':
#
#   petla = True
#   krok = 1
#   wartosc_start = 1200.0
#   czas = 300
#
#   while petla:
#     print("""1 - Metoda Eulera
# 2 - Metoda Heuna
# 3 - Metoda metoda punktu środkowego
# 4 - Metoda metoda Rungego-Kutty czwartego rzędu
# Inny wybor - wyjście z programu
# Wybor: """)
#
#     wejscie = input()
#
#     if wejscie == '1':
#       t, x = Euler(funckja_2, [wartosc_start, 0], 0.0, czas, krok)
#
#     elif wejscie == '2':
#       t, x = Heun(funckja_2, [wartosc_start, 0], 0.0, czas, krok)
#
#     elif wejscie == '3':
#       t, x = Pkt_srod(funckja_2, [wartosc_start, 0], 0.0, czas, krok)
#
#     elif wejscie == '4':
#       t, x = RK4(funckja_2, [wartosc_start, 0], 0.0, czas, krok)
#
#     else:
#       petla = False
#       break
#
#     print("Zapisać nowe wyniki do txt? Nadpisuje poprzedni rekord. [y/n]")
#     wejscie_zapis = input()
#
#     if wejscie_zapis == 'y':
#       if wejscie == '1':
#         file = open("euler.txt", "w")
#       elif wejscie == '2':
#         file = open("heun.txt", "w")
#       elif wejscie == '3':
#         file = open("pktsrod.txt", "w")
#       elif wejscie == '4':
#         file = open("rk4.txt", "w")
#
#     plt.plot(t, x[:, 0])
#     s = str(x[-1])
#     print(
#       "d/dt T = -alfa(T^4 - beta)  \nDla t = 300 wynik : {} \nprawidlowy wynik : 877,754... wedlug wolframa ".format(
#         s[1:8]))
#
#     print("Po zamknieciu wykresu wyswietla sie tabelarycznie wyniki")
#     plt.show()
#     i = 0
#     print("Krok(t) / Wartosc(temp)")
#     for each in x[:, 0]:
#       i = i + krok
#       print("{} {}".format(i, each))
#       if wejscie_zapis == 'y':
#         file.write("{} {}\n".format(i, each))
#
#     if wejscie_zapis == 'y':
#       file.close()
#
#
#
#
#
#
#
