import math
import numpy as np
import time

def funcja_1(x):
    return 4*x + math.sin(x) - math.exp(x)
def funckja_2(x):
    return 3*x*x*x*x - 6*x*x + x + 2
def funckja_3(x):
    return x*x - 3*x*math.sin(x) + (3*math.sin(x))*(3*math.sin(x))

def liczba_miejsc_po_przecinku(liczba): # funkcja pomocnicza
    czesc_calkowita, czesc_dziesietna = str(liczba).split('.')
    if len(czesc_dziesietna) > 0:
        return len(czesc_dziesietna)
    else:
        return 0

def bisekcja(f, a, b, tol):
    # funkcja zwraca 1 natrafione miejsce zerowe
    # f - funkcja przyjmowana
    # a - poczatek zakresu
    # b - koniec zakresu
    # tol - krok
    if np.sign(f(a)) == np.sign(f(b)):
        return None
    m = (a + b) / 2
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisekcja(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return bisekcja(f, a, m, tol)

    return None

def bisekcja_looped(f, a, b, tol, dokladnosc):
    # funkcja zwraca wszystkie miejsca zerowe z zakresu
    # dokladnosc - (int) ilosc miejsc po przecinku uwzgledniana przy wyniku
    c = a
    tab = []
    while c < b-tol:
        d = c+ tol*1000
        zmienna = bisekcja(f, c, d, tol)
        if zmienna is not None:
            zmienna = round(zmienna, dokladnosc)
            if zmienna not in tab:
                tab.append(zmienna)
        c += tol

    return tab

def regulaFalsi(a, b, f, e):
    # funkcja zwraca 1 natrafione miejsce zerowe
    # a - poczatek przedzialu
    # b - koniec przedzialu
    # f - funkcja
    # e - dokladnosc

    if f(a) * f(b) > 0.0:
        return None
    else:

        step = 1
        condition = True
        while condition:
            x2 = a - (b - a) * f(a) / (f(b) - f(a))
            if f(a) * f(x2) < 0:
                b = x2
            else:
                a = x2

            step = step + 1
            condition = abs(f(x2)) > e

        return x2

def regulaFalsi_looped(a,b,f,dokladnosc,krok):
    # zwraca tabele z wszytskimi miejscami zerowymi z przedzialu
    # krok - krok pomiedzy iteracjami
    c = a
    tab = []
    while c < b-krok:
        d = c+ krok*100
        zmienna = regulaFalsi(c,d,f,dokladnosc)
        if zmienna is not None:
            zmienna = round(zmienna, liczba_miejsc_po_przecinku(dokladnosc))
            if zmienna not in tab:
                tab.append(zmienna)
        c += krok

    return tab



""" Kod z zajec:
   print("Bisekcja")
   print("Funckja 1")
   start = time.time()
   print(bisekcja_looped(funcja_1,0,3,0.00001,4))
   koniec = time.time()
   print("Czas: {}".format(koniec-start))
   start = time.time()
   print("Funckja 2")
   print(bisekcja_looped(funckja_2, -2, 2, 0.00001, 4))
   koniec = time.time()
   print("Czas: {}".format(koniec-start))
   start = time.time()
   print("Funckja 3")
   print(bisekcja_looped(funckja_3, 0, 1,0.00001, 4))
   koniec = time.time()
   print("Czas: {}".format(koniec-start))
   start = time.time()
   print("\nRefula Falsi")
   print("Funckja 1")
   print(regulaFalsi_looped(0,3,funcja_1,0.0001,0.00001))
   koniec = time.time()
   print("Czas: {}".format(koniec-start))
   start = time.time()
   print("Funckja 2")
   print(regulaFalsi_looped(-2, 2, funckja_2, 0.0001, 0.00001))
   koniec = time.time()
   print("Czas: {}".format(koniec-start))
   start = time.time()
   print("Funckja 3")
   print(regulaFalsi_looped(0, 1, funckja_3, 0.0001, 0.00001))
   koniec = time.time()
   print("Czas: {}".format(koniec-start))
   start = time.time()


"""

