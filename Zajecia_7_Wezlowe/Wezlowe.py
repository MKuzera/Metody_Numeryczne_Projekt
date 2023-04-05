import math
def funkcja(x):
   return (5*(x**3)) - (12*(x**2)) - (x) + 3

def funkcja2(x):
   return x*x*math.sin(x)*math.sin(x)*math.sin(x)

def funkcja3(x):
   return (math.exp(x**2))*(1-x)

def dwuwezlowe(fun,a,b):
   wezel1 = -(1/math.sqrt(3))
   waga1 = 1
   wezel2 = (1/math.sqrt(3))
   waga2 = 1
   return ((b - a) / 2) * (waga1*fun(((b - a) / 2) * (wezel1) + ((b + a) / 2)) + waga2*fun(((b - a) / 2) * (wezel2) + ((b + a) / 2)))


def trzywezlowe(fun,a,b):
   wezel1 = 0
   waga1 = 8/9
   wezel2 = -math.sqrt(3/5)
   waga2 = 5/9
   wezel3 = math.sqrt(3/5)
   waga3 = 5/9
   return ((b - a) / 2) * (waga1*fun(((b - a) / 2) * (wezel1) + ((b + a) / 2)) + waga2*fun(((b - a) / 2) * (wezel2) + ((b + a) / 2)) + waga3*fun(((b - a) / 2) * (wezel3) + ((b + a) / 2)))

def czterowezlowe(fun,a,b):
   wezel1 = -math.sqrt(3/7 - (2/7 * math.sqrt(6/5)))
   waga1 = (18+math.sqrt(30))/36
   wezel2 = math.sqrt(3/7 - (2/7 * math.sqrt(6/5)))
   waga2 = (18+math.sqrt(30))/36
   wezel3 = -math.sqrt(3/7 + (2/7 * math.sqrt(6/5)))
   waga3 = (18-math.sqrt(30))/36
   wezel4 = math.sqrt(3/7 + (2/7 * math.sqrt(6/5)))
   waga4 = (18-math.sqrt(30))/36
   return ((b - a) / 2) * ( waga1*fun(((b - a) / 2) * (wezel1) + ((b + a) / 2)) + waga2*fun(((b - a) / 2) * (wezel2) + ((b + a) / 2)) + waga3*fun(((b - a) / 2) * (wezel3) + ((b + a) / 2)) + waga4*fun(((b - a) / 2) * (wezel4) + ((b + a) / 2)))

""" kod z zajec do maina
 print("5x^3 - 12x^2 -x + 3 w przedziale -2.0 do 3.0")
   print("Prawidłowa odp. -46.25")
   print("Dwuwezlowe: {} ".format(dwuwezlowe(funkcja,-2,3)))
   print("Trzywezlowe: {}".format(trzywezlowe(funkcja,-2,3)))
   print("Czterowezlowe: {}.".format(czterowezlowe(funkcja,-2,3)))


   print("\nx^2 * sin^3 (x) od 1.0 do 4.8")
   print("Prawidłowa odp. -10.9001 ")
   print("Dwuwezlowe: {} ".format(dwuwezlowe(funkcja2,1,4.8)))
   print("Trzywezlowe: {}".format(trzywezlowe(funkcja2,1,4.8)))
   print("Czterowezlowe: {}.".format(czterowezlowe(funkcja2,1,4.8)))
   print("Wraz z ilsocia wezlow przyblizenie oraz blad staja sie coraz mniejsze")


   print("\nexp(x^2)* (1-x) od -1.5 do 3.2")
   print("Prawidłowa odp. -9358.63 ")
   print("Dwuwezlowe: {} ".format(dwuwezlowe(funkcja3, -1.5, 3.2)))
   print("Trzywezlowe: {}".format(trzywezlowe(funkcja3, -1.5, 3.2)))
   print("Czterowezlowe: {}.".format(czterowezlowe(funkcja3, -1.5, 3.2)))
   print("Wartosc zbliza sie do wartosci oczekiwanej.\n")

   print("Dla 1. rownania wsyztskie 3 metody daja idealny wynik")
   print("Dla 2. rownania trzecia metoda juz daje wynik przybliżony")
   print("Dla 3. rownania żadna z wartosci nie odpowiada wartosci szukanej lecz wraz z iloscia wezlow")
   print("wartosc zbliza sie do oczekiwanej")
   print("Dodatkowo robiac test dla 5. wezlow wartosc juz zblizala sie do oczekiwanej lecz w celu otrzymania wartosci")
   print("oczekiwanej trzeba bedzie jeszcze zwiekszyc ilosc wezlow")
"""