def horner_2(wspA, x):
   suma = float(0)
   K = len(wspA) - 1
   for i in range(K, -1, -1):
      if (i == K):
         suma = float(wspA[i])
      else:
         suma = float(wspA[i]) + x * suma

   return suma


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


def simpson_quadrature_z_danymi():
   file = open("Zajecia_6_Kwadratura_Simpson/kwadratury_gr_3.txt", "r")
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
   print("""a = {} , b = {} , N = {}
      Ai = {}""".format(a, b, N, Ai))



