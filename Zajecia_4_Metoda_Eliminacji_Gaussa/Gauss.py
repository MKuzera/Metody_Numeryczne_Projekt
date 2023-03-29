import numpy as np
from numpy import array, zeros, fabs, linalg
# GaussElim -> funkcja gotowa do uzytku
# Gaus_zajec -> funkcja obliczajaca dane z zajec
# gauss_2 -> gaus z pivotem (dziala)
def gauss_2(a,b):

    n = len(b)
    x = zeros(n, float)
    for k in range(n - 1):
        if fabs(a[k, k]) < 1.0e-12:

            for i in range(k + 1, n):
                if fabs(a[i, k]) > fabs(a[k, k]):
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break

        for i in range(k + 1, n):
            if a[i, k] == 0: continue

            factor = a[k, k] / a[i, k]
            for j in range(k, n):
                a[i, j] = a[k, j] - a[i, j] * factor
            b[i] = b[k] - b[i] * factor

    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_ax = 0

        for j in range(i + 1, n):
            sum_ax += a[i, j] * x[j]

        x[i] = (b[i] - sum_ax) / a[i, i]

    return x




def gaussElim(a ,b): # z zajec

    n = len(b)
    for k in range(0 , n -1):
        for i in range( k +1 ,n):
            if a[i ,k] != 0.0:
                lam = a [i ,k ] /a[k ,k]
                a[i , k +1:n] = a[i , k +1:n] - lam*a[k , k +1:n]
                b[i] = b[i] - lam*b[k]
    for k in range( n -1 ,-1 ,-1):
        b[k] = (b[k] - np.dot(a[k , k +1:n] ,b[ k +1:n]) ) /a[k ,k]

    return b

def Gauss_zajec():
    print("\n\n1 - A , 2 - B , 3 - C , 4 - exit")
    wejscie = input()

    if (wejscie == "1"):
        file = open("Zajecia_4_Metoda_Eliminacji_Gaussa/A.txt", "r")
    elif (wejscie == "2"):
        file = open("Zajecia_4_Metoda_Eliminacji_Gaussa/B.txt", "r")
    elif (wejscie == "3"):
        file = open("Zajecia_4_Metoda_Eliminacji_Gaussa/C.txt", "r")
    else:
        return 0

    A = []
    new = []
    for each in file:
        K = each.split()
        for each2 in K:
            new.append(float(each2))
            print(float(each2))
        A.append(new)
        new = []
    A.pop(1)

    print(A)

    a = np.array([np.array(A[1], float), np.array(A[2], float), np.array(A[3], float), np.array(A[4], float),
                  np.array(A[5], float)])
    b = np.array(np.array(A[0], float))

    aOrig = a.copy()
    bOrig = b.copy()
    x = gaussElim(a, b)
    print(aOrig)
    print("x =\n", bOrig)
    print("\n [a]{x} - b =\n", np.dot(aOrig, x) - bOrig)