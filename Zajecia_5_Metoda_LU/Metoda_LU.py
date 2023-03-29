import numpy as np
from numpy import array, zeros, fabs, linalg
import Zajecia_4_Metoda_Eliminacji_Gaussa.Gauss as gauss

def RozkladDoolittle(macierz):
    n = len(macierz)
    gorna = [[0] * n for x in range(n)]
    dolna = [[0] * n for x in range(n)]
    for i in range(n):
        for k in range(i, n):
            suma = sum([dolna[i][j] * gorna[j][k] for j in range(i)])
            gorna[i][k] = macierz[i][k] - suma
        for k in range(i, n):
            if i == k:
                dolna[i][i] = 1
                continue
            suma = sum([dolna[k][j] * gorna[j][i] for j in range(i)])
            dolna[k][i] = (macierz[k][i] - suma) / gorna[i][i]
    return gorna, dolna

def WypiszTablice(macierz):
  n = len(macierz)
  for i in range(n):
    print('\t'.join([str(x) for x in macierz[i]]))

def multimatrix(X,Y):
    result = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    for r in result:
        print(r)
    return result

def pobierz_dane_A():
    file = open("Zajecia_5_Metoda_LU/LU.txt", "r")
    b = []
    a = []
    line = file.readline().split()
    for each in line:
        b.append(float(each))
    line2 = []
    for each in file:
        line = each.split()
        for k in line:
            line2.append(float(k))
        a.append(line2)
        line2 = []
    return a

def pobierz_dane_B():
    file = open("Zajecia_5_Metoda_LU/LU.txt", "r")
    b = []
    a = []
    line = file.readline().split()
    for each in line:
        b.append(float(each))
    line2 = []
    for each in file:
        line = each.split()
        for k in line:
            line2.append(float(k))
        a.append(line2)
        line2 = []
    return b

def wyswietl_A_B(a,b):
    print("----------------------- B:")
    print(b)
    print("----------------------- A:")
    print(a)
def Metoda_LU():
    a = pobierz_dane_A()
    b = pobierz_dane_B()
    n = 5
    gorna, dolna = RozkladDoolittle(a)
    print("Górna U:")
    WypiszTablice(gorna)
    print("Dolna U:")
    WypiszTablice(dolna)
    print("----------------------- U * L:")
    result = multimatrix(dolna,gorna)


    A = np.array([np.array(a[0], float), np.array(a[1], float), np.array(a[2], float), np.array(a[3], float),
                  np.array(a[4], float)])
    B = np.array(np.array(b, float))

    aOrig = a.copy()
    bOrig = b.copy()

    C = np.array([np.array(dolna[0], float), np.array(dolna[1], float), np.array(dolna[2], float), np.array(dolna[3], float),np.array(dolna[4], float)])
    z = gauss.gauss_2(C,B)
    print("----------------------- z:")
    print(z)

    gorna_conv = np.array(
        [np.array(gorna[0], float), np.array(gorna[1], float), np.array(gorna[2], float), np.array(gorna[3], float),
         np.array(gorna[4], float)])

    x = gauss.gauss_2(gorna_conv,z)
    print("----------------------- x:")
    print(x)




