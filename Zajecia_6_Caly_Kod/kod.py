import numpy as np
def funk(x):
   return ((4.0)*(x**0))  - ((6.0)*(x**1)) +((4.0)*(x**2)) + ((5.0)*(x**3)) -((1.0)*(x**4))
def funkcja():
   f = lambda x: x ** 2 * (np.cos(x) ** 3)
   return f
def f11(x):
   return (x**2)*(np.cos(x)**3)

def simpsonQuadrature(leftLimit, rightLimit, dx, fun):
   s = 0
   st = 0
   size = (rightLimit - leftLimit) / dx + 1
   for i in range(1, int(size)):
      x = leftLimit + i * dx
      st += fun(x - dx / 2)
      if i < size:
         s += fun(x)
   return dx / 6 * (fun(leftLimit) + fun(rightLimit) + 2 * s + 4 * st)

def met_trapv2(f, a, b, n):
   x = np.array([0])
   h = (b - a) / n
   x = [a + i * (b - a) / n for i in range(n + 1)]

   wynik = (f(a) + f(b)) / 2
   for i in range(1, n):
      wynik += f(x[i])

   return wynik * h

wspB = [4.0,-6.0,4.0,5.0,-1.0]
def horner_2(wspA,x):
   suma = float(0)
   K = len(wspA) - 1
   for i in range(K, -1, -1):
      if (i == K):
         suma = float(wspA[i])
      else:
         suma = float(wspA[i]) + x * suma

   return suma

def horner_3(x):
   suma = float(0)
   K = len(wspB) - 1
   for i in range(K, -1, -1):
      if (i == K):
         suma = float(wspB[i])
      else:
         suma = float(wspB[i]) + x * suma

   return suma

""" kod z zajec
file = open("kwadratury_gr_3.txt", "r")
   line = file.readline()
   line2 = line.split()
   N = int(line2[2])
   line = file.readline()
   line = file.readline()
   line2 = line.split()
   Ai = []
   for each in line2:
      Ai.append(float(each))
   line = file.readline()
   line2 = line.split()
   a = float(line2[1])
   b = float(line2[2])
   print("a = {} , b = {} , N = {}
        Ai = {}".format(a, b, N, Ai)) # TU zamienic " na """ """

   print("Dla x^2cos^3(x) Trapez:   Mniej dokladny")
   print(met_trapv2(f11,2,6,99))
   print("Dla x^2cos^3(x) simpson:  Bardziej dokladny")
   print(simpsonQuadrature(2,6,0.0001,f11))


   print("\n Prawidlowy wynik: 1070.9 (z wolframa) \n\nDla danych z txt Trapez: (wprowadzajac gotowa funckje) ")
   print(met_trapv2(funk, a, b, 99))
   print("Dla danych z txt simpson:  (wprowadzajac gotowa funckje) ")
   print(simpsonQuadrature(a,b,0.0001,funk))

   print("\nz Hornerem:")
   print("Dla danych z txt Trapez + horner: ")
   print(met_trapv2(horner_3, a, b, 99))
   print("Dla danych z txt simpson + horner: ")
   print(simpsonQuadrature(a,b,0.0001,horner_3))




"""




