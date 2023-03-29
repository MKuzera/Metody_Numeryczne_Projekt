from datetime import datetime

def pobierz_dane_A():
    fileH = open("Zajecia_3_Interpolacja_Postacia_Naturalna/H.txt", "r")
    line1 = fileH.readline()
    H = line1.split()
    H_a_list = []
    for each in H:
        H_a_list.append(each[3:])
    line2 = fileH.readline()
    H_x_list = line2.split()
    H_x_list.pop(0)
    return H_a_list

def pobierz_dane_X():
    fileH = open("Zajecia_3_Interpolacja_Postacia_Naturalna/H.txt", "r")
    line1 = fileH.readline()
    H = line1.split()
    H_a_list = []
    for each in H:
        H_a_list.append(each[3:])
    line2 = fileH.readline()
    H_x_list = line2.split()
    H_x_list.pop(0)
    return H_x_list

def Naturlna():
    H_a_list = pobierz_dane_A()
    H_x_list = pobierz_dane_X()
    print("Podaj X")
    x = float(input())

    print("Ile wezlow")
    K = float(input())

    start = datetime.now()
    suma = float(0)
    for i in range(0, int(K)):
        if (i == 0):
            suma = float(H_a_list[0])
        else:
            suma = suma + float(H_a_list[i]) * x * pow(x, int(K) - 1)
    print(suma)
    end = datetime.now()
    print("Elapsed", (end - start).total_seconds() * 10 ** 6, "µs")


def wyswietl_dane(A,X):
    print(A)
    print(X)