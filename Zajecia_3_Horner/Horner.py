from datetime import datetime

def pobierz_dane_A():
    fileH = open("Zajecia_3_Horner/H.txt", "r")
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
    fileH = open("Zajecia_3_Horner/H.txt", "r")
    line1 = fileH.readline()
    H = line1.split()
    H_a_list = []
    for each in H:
        H_a_list.append(each[3:])
    line2 = fileH.readline()
    H_x_list = line2.split()
    H_x_list.pop(0)
    return H_x_list

def Horner():
    H_a_list = pobierz_dane_A()
    H_x_list = pobierz_dane_X()
    print("Podaj X")
    x = float(input())

    print("Ile wezlow")
    K = int(input())
    start = datetime.now()
    suma = float(0)
    for i in range(K, 0, -1):
        if (i == K):
            suma = float(H_a_list[i])
        else:
            suma = float(H_a_list[i]) + x * suma

    print(suma)
    end = datetime.now()
    print("Elapsed", (end - start).total_seconds() * 10 ** 6, "µs")