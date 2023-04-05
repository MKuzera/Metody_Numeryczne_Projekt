import math
import numpy as np
import funkcje_do_zadan as funkcje_do_zadania

def aproxymacja(lewa , prawa , functions_of_funkcja , ilosc_jednomainow):# 1 - 1 | 2 - x | 3 - x^2 ...
  functions = funkcje_do_zadania.functions_x_pow
  # functions - tablica[i] z funkcjami pow(x,i)
  # functions_of_funckja - tablica[i] z funkcjami funkcji * pow(x,i)

  a = []
  b = []
  c = []

  for i in range(0,int(ilosc_jednomainow)):
    for j in range(0,int(ilosc_jednomainow + 1)):
      if j != ilosc_jednomainow:
        b.append(funkcje_do_zadania.simpsonQuadrature(lewa,prawa,0.001, functions[i+j]))

      else:
        c.append(funkcje_do_zadania.simpsonQuadrature(lewa,prawa,0.001,functions_of_funkcja[i]))
    a.append(b)
    b = []

  return [a,c]




if __name__ == '__main__':

  functions_of_funkcja_simus_x = funkcje_do_zadania.functions_of_sinus # przypisuje ktora tablice dac
  g = aproxymacja(0,math.pi/2 ,functions_of_funkcja_simus_x,3)
  a = g[0]
  b = g[1]

  arr = np.array(a)
  arr2 = np.array(b)
  wynik= funkcje_do_zadania.gauss_2(arr,arr2)
  print("Dla funkcji sin(x) z przedzialu <{},{}> : 'a0 , a1 , a2' {} ".format(0,math.pi/2,wynik))

  functions_of_funkcja_ex = funkcje_do_zadania.functions_of_ex# przypisuje ktora tablice dac
  g = aproxymacja(-1,1 ,functions_of_funkcja_ex,5)
  a = g[0]
  b = g[1]
  print('A')
  for each in a:
    print(each)
  print('B')
  print(b)
  arr = np.array(a)
  arr2 = np.array(b)
  wynik= funkcje_do_zadania.gauss_2(arr,arr2)
  print("Dla funkcji e^x * sin(x/2) - x^3 z przedzialu <{},{}> : 'a0 , a1 , a2 , a3 , a4' {} ".format(-1,1,wynik))