import numpy as np
def divided_diff(x, y):
    n = len(x)
    F = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        F[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])

    return F[0]

def newton_interpolation(x, y, z):

    n = len(x)
    F = divided_diff(x, y)
    p = F[n-1]
    for k in range(1, n):
        p = F[n-1-k] + (z - x[n-1-k])*p

    return p

if __name__ == '__main__':
    pass


def pobierz_dane_X():
    fileN = open("Zajecia_3_Newton/N.txt", "r")
    line1 = fileN.readline()
    line2 = fileN.readline()
    X = line1.split()
    F = line2.split()
    X.pop(0)
    F.pop(0)
    print(X)
    print(F)
    return X

def pobierz_dane_F():
    fileN = open("Zajecia_3_Newton/N.txt", "r")
    line1 = fileN.readline()
    line2 = fileN.readline()
    X = line1.split()
    F = line2.split()
    X.pop(0)
    F.pop(0)
    print(X)
    print(F)
    return F

def Newton():
    X = pobierz_dane_X()
    F = pobierz_dane_F()

    print("Podaj X")
    N = float(input())
    X2 = X.copy()
    F2 = F.copy()
    X = []
    F = []
    for each in X2:
        X.append(float(each))
    for each in F2:
        F.append(float(each))

    X3 = np.array(X)
    F3 = np.array(F)

    #  Z = np.linspace(-7,8,100)
    #    fig, ax = plt.subplots()
    #    ax.plot(Z,newton_interpolation(X3,F3,Z))
    #    ax.scatter(X3,F3)
    #    plt.show()


    print("Wsp: ")
    print(divided_diff(X3, F3))
    print("Wartosc: ")
    print(newton_interpolation(X3, F3, N))
