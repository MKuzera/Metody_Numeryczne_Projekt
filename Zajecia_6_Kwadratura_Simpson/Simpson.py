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