import numpy as np
from matplotlib import pyplot as plt

#f - funkcja f z rownania
#x0-wartosc poczatkowa
#t0-czas poczatkowy
#tk-czas koncowy
#h-krok czasowy

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

if __name__ == '__main__':


  # zakomnetowana czesc jest dla funkcji y' = y
  # # y' = y
  # # y(0) = 1
  #
  # t, x = Euler(f, [1.0,0], 0.0, 4, 0.0001)
  # print(" y' = y , Dla t = 4 wynik : {}  , e^4 = 54.59...".format(x[-1]))
  #
  # print("Aby przejsc do kolejnego wykresu nalezy aktualny zamknac")
  # plt.plot(t, x[:, 0])
  # plt.show()
  # #print("Ilosc krokow okresla czas wykonywania oblcizen , przy bardzo malymn kroku moze zajac kilka sekund")



  # y' = -alfa * (T^4 - beta)
  # y(0) = 1200


  krok = 1
  wartosc_start = 1200.0
  czas = 300
  t, x = Euler(funckja_2, [wartosc_start,0], 0.0,czas, krok)
  plt.plot(t, x[:, 0])
  s = str(x[-1])
  print("Krok : {}".format(krok))
  print("d/dt T = -alfa(T^4 - beta)  \nDla t = 300 wynik : {} \nprawidlowy wynik : 877,754... wedlug wolframa ".format(s[1:8]))
  print("Po zamknieciu wykresu wyswietla sie tabelarycznie wyniki")
  plt.show()
  i = 0
  print("Krok(t) / Wartosc(temp)")
  for each in x[:, 0]:
    i = i + krok
    print("{} {}".format(i,each))


