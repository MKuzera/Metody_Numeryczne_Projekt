# f- funkcje
# f_pochodna - pochodne funkcji
# epsilon - granica np 10e-8 do ktorej liczy
# n - ilosc iteracji

import math


def funckja_1(x):
    return x ** 2 - 2


def funkcja_1_pochodna(x):
    return 2 * x


def funckja_2(x):
    return x ** 3 + x ** 2 - 3 * x - 3


def funkcja_2_pochodna(x):
    return 3 * x * x + 2 * x - 3


def funckja_3(x):
    return math.sin(x * x) - x * x


def funkcja_3_pochodna(x):
    return 2 * x * (math.cos(x * x) - 1)


def funckja_4(x):
    return math.sin(x * x) - x * x + (1 / 2)


def funkcja_4_pochodna(x):
    return 2 * x * (math.cos(x * x) - 1)


# funckja oblicza wartosc podchodnej w punkcie
def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h


def newton(f, Df, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Brak wyniku')
            return None
        xn = xn - fxn / Dfxn
    print('Maks iteracji')
    return None


def newton_z_numerycznie_podchodna(f, x0, epsilon, max_iter):
    # modyfikacja funkcji newton w ktorej zamiast korzytac z gotowej funkcji pochodnej
    # wyliczam wartosci numerycznie podchonej w punkcie

    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            return xn
        Dfxn = derivative(f, xn)
        if Dfxn == 0:
            print('Brak wyniku')
            return None
        xn = xn - fxn / Dfxn
    print('Maks iteracji')
    return None


def siecznych(f, a, b, N):
    if f(a) * f(b) >= 0:
        return None
    a_n = a
    b_n = b
    for n in range(1, N + 1):
        m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            return m_n
        else:
            return None
    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))


def siecznych_wszytskie(f, a, b, N, krok):
    punkt = a
    tab = []
    while (punkt < b):

        npkt = siecznych(f, punkt, b, N)
        if npkt == None:
            pass
        else:
            nnpkt = round(npkt, 6)
            if nnpkt not in tab:
                tab.append(nnpkt)
        punkt = punkt + krok
    return tab


""" Kod z zajec
    print("Fukcja  siecznych_wszytskie zwraca tablice z wszytskimi miejscami zerowymi z zakresu")
    print("Dla funkcji: x^3 + x^2 -3x -3")
    print(siecznych_wszytskie(funckja_2, -5, 5, 100, 1))
    print("\n")

    print("Newton Funkcja  x^3 + x^2 -3x -3")
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, -1,
                                                                newton(funckja_2, funkcja_2_pochodna, -1, 1e-8, 10)))
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, -1.5,
                                                                newton(funckja_2, funkcja_2_pochodna, -1.5, 1e-8, 10)))
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, 1.5,
                                                                newton(funckja_2, funkcja_2_pochodna, 1.5, 1e-8, 10)))
    print("\nNewton ale numerycznie obliczane pochodne  Funkcja x^2 - 2")
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, -1,
                                                                newton_z_numerycznie_podchodna(funckja_2, -1, 1e-8,
                                                                                               10)))
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, -1.5,
                                                                newton_z_numerycznie_podchodna(funckja_2, -1.5, 1e-8,
                                                                                               10)))
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, 1.5,
                                                                newton_z_numerycznie_podchodna(funckja_2, 1.5, 1e-8,
                                                                                               10)))
    print("\nSieczncyh: Funkcja x^3 + x^2 -3x -3")
    print("Przedzial <{} , {}> , iteracji {} Wynik: {}".format(-2, -1.5, 10, siecznych(funckja_2, -2, -1.5, 10)))
    print("Przedzial <{} , {}> , iteracji {} Wynik: {}".format(1, 2, 10, siecznych(funckja_2, 1, 2, 10)))
    print("Przedzial <{} , {}> , iteracji {} Wynik: {}".format(1, 2, 10, siecznych(funckja_2, -0.8, -1.2, 10)))

    print("Newton Funkcja  sin(x^2) - x^2")
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, 0,
                                                                newton(funckja_3, funkcja_3_pochodna, -1, 1e-8, 10)))
    print("\nNewton ale numerycznie obliczane pochodne  Funkcja x^2 - 2")
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, 0,
                                                                newton_z_numerycznie_podchodna(funckja_3, -1, 1e-8,
                                                                                               10)))
    print("\nSieczncyh: Funkcja sin(x^2) - x^2")
    print("Przedzial <{} , {}> , iteracji {} Wynik: {}".format(-0.5, 0.5, 10, siecznych(funckja_3, -0.5, 0.5, 10)))

    print("Brak miejsca zerowego")

    print("\nNewton sin(x^2) - x^2 + 1/2")
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, -1,
                                                                newton(funckja_4, funkcja_4_pochodna, -1, 1e-8, 10)))
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, 1,
                                                                newton(funckja_4, funkcja_4_pochodna, 1, 1e-8, 10)))

    print("\nNewton ale numerycznie obliczane pochodne  Funkcja x^2 - 2")
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, -1,
                                                                newton_z_numerycznie_podchodna(funckja_4, -1, 1e-8,
                                                                                               10)))
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, 1,
                                                                newton_z_numerycznie_podchodna(funckja_4, 1, 1e-8, 10)))

    print("\nSieczncyh: sin(x^2) - x^2 + 1/2")
    print("Przedzial <{} , {}> , iteracji {} Wynik: {}".format(-1.5, -1, 10, siecznych(funckja_4, -1.5, -1, 10)))
    print("Przedzial <{} , {}> , iteracji {} Wynik: {}".format(1, 1.5, 10, siecznych(funckja_4, 1, 1.5, 10)))

    print("Newton Funkcja x^2 - 2")
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, -1,
                                                                newton(funckja_1, funkcja_1_pochodna, -1, 1e-8, 10)))
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, 1,
                                                                newton(funckja_1, funkcja_1_pochodna, 1, 1e-8, 10)))

    print("\nNewton ale numerycznie obliczane pochodne  Funkcja x^2 - 2")
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, -1,
                                                                newton_z_numerycznie_podchodna(funckja_1, -1, 1e-8,
                                                                                               10)))
    print('Iteracji {} ,  wartość startowa {} Wynik: {}'.format(10, 1,
                                                                newton_z_numerycznie_podchodna(funckja_1, 1, 1e-8, 10)))

    print("\nSieczncyh: Funkcja x^2 - 2")
    print("Przedzial <{} , {}> , iteracji {} Wynik: {}".format(1, 2, 10, siecznych(funckja_1, 1, 2, 10)))
    print("Przedzial <{} , {}> , iteracji {} Wynik: {}".format(-2, 1, 10, siecznych(funckja_1, -2, -1, 10)))


"""





