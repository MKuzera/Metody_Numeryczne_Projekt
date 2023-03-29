class punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pobierz_dane():
    file = open("Zajecia_2_Interpolacja_Lagrange/6.txt", "r")

    line = file.readline()
    X = line.split()
    line = file.readline()
    Y = line.split()
    f = []

    for i in range(len(X)):
        if(i==0):
            continue
        g = punkt(float(X[i]),float(Y[i]))
        f.append(g)
    return f
def wyswietl_dane(f):
    for each in f:
        print(each.x)
        print(each.y)
        print("\n")



def Interpolacja_Lagrange():
    f = pobierz_dane()
    wyswietl_dane(f)
    print("Podaj ")
    xi = float(input())
    n = len(f)
    wynik = 0.0
    for i in range(n):
        k = f[i].y
        for j in range(n):
            if j != i:
                k = k * (xi - f[j].x) / (f[i].x - f[j].x)
        wynik += k
    print("Wynik: ")
    print(xi)
    print(wynik)