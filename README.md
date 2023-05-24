# Metody_Numeryczne_Projekt
Projekt zawiera zadania związane z metodami numerycznymi ich implementacjach w jezyku Python.
# Dokumentacja
Projekt podzielony jest na sekcje związane z zajęciami.  
**Zajecia 1 Organizacyjne**  
**Zajecia 2 Interpolacja Lagrange’a**  
Funkcja: Interpolacja_Lagrange() oblicza wartość wielomianu interpolacyjnego w punkcie wpisanym z klawiatury dla danych z pliku txt.  
**Zajecia 3 Interpolacja Newtona**  
Funkcja: Naturalna() oblicza wartości wielomianu zadanego w postaci naturalnej dla wartości 𝑥wczytanej z pliku.  
Funkcja: Horner() oblicza wartości wielomianu według schematu Hornera dla wartości x wczytanej z pliku .  
Funkcja: Newton() Oblicza wartości współczynników 𝑎𝑖 wielomianu w postaci Newtona na podstawie danych z pliku.      
**Zajecia 4 Rozwiązywanie układu równań liniowych – metoda eliminacji Gaussa**    
Funkcja: gaussElim(a,b) oblicza rozwiązania układów liniowych metodą eliminacji Gaussa, pobiera dane z pliku.  
Funkcja: gauss_2(a,b) oblicza rozwiązania układów liniowych metodą eliminacji Gaussa z pivotingiem, pobiera dane z pliku.   
**Zajecia 5 Rozwiązywanie układu równań liniowych – metoda LU**    
Funkcja: Metoda_LU() oblicza rozwiązania układów liniowych metodą LU, pobiera dane z pliku.  
**Zajecia 6 Całkowanie numeryczne - cz.1 (kwadratury Simpsona oraz Trapezów)**  
Funkcja: simpsonQuadrature(leftLimit, rightLimit, dx, fun) oblicza kwadrature za pomocą wzoru Simpsona (dx to skok)  
Funkcja: met_trapv2(f, a, b, n): oblicza kwadrature za pomocą wzoru trapezów (a,b to zakres, n to ilość skoków)  
**Zajecia 7 Całkowanie numeryczne - cz.2 (kwadratury 2-3-4 wezłowe)**   
Funkcja: dwuwezlowe(fun,a,b): Oblicza całke z przedziału a,b za pomocą dwuwęzłowej kwadratury.  
Funkcja: trzywezlowe(fun,a,b): Oblicza całke z przedziału a,b za pomocą trzywęzłowej kwadratury.  
Funkcja: czterowezlowe(fun,a,b): Oblicza całke z przedziału a,b za pomocą czterowęzłowej kwadratury.  
**Zajecia 8 Aproksymacja**  
Funkcja: aproxymacja(lewa , prawa , functions_of_funkcja , ilosc_jednomainow) lewa,prawa zakres , functions_of_funkcja tablica funkcji (przykład) gdzie tab[0] = sinx tab[1] = sinx* x tab[2] = sinx*x^2  , ilosc_jednomainow określa ilość jednomianów użytych w programie.  
**Zajecia 9 i 10  Rozwiązywanie równań różniczkowych**  
Funkcja: Euler(f, x0, t0, tk, h) oblicza numerycznie równanie różniczkowe pierwszego rzędu z warunkiem początkowym metoda Eulera.  
Funkcja: Heun(f, x0, t0, tk, h) oblicza numerycznie równanie różniczkowe pierwszego rzędu z warunkiem początkowym metoda Heuna.  
Funkcja: Pkt_srod(f, x0, t0, tk, h) oblicza numerycznie równanie różniczkowe pierwszego rzędu z warunkiem początkowym metoda Punktu środkowego.  
Funkcja: RK4(f, x0, t0, tk, h) oblicza numerycznie równanie różniczkowe pierwszego rzędu z warunkiem początkowym metoda Rungego-Kutty czwartego rzędu.  
f - funkcja , x0 - wartość początkowa , t0 - czas początkowy , tk - czas końcowy , h- krok czasowy.   
**Zajecia 11 Rozwiązywanie równań nieliniowych - cz.1**   
Funkcja: newton(f, Df, x0, epsilon, max_iter) oblicza miejsce zerowe za pomocą metody newtona: f - funkcja , Df - pochodna funkcji, x0 - przybliżony punkt, epsilon - maks przyblizenie wyniku, max_iter - maksymalna ilość iteracji.  
Funkcja: newton_z_numerycznie_podchodna(f, x0, epsilon, max_iter)  jest to ta sama funkcja co wyżej lecz nie przyjmuje już gotowej pochodnej a numerycznie liczy pochodna  
Funkcja: siecznych(f, a, b, N) oblicza miejsce zerowe z przedziału a,b , N - ilosc iteracji  
Funkcja: siecznych_wszytskie(f, a, b, N, krok) oblicza wszytskie miejsca zerowe z przedziału a,b , krok określa wielkość kroku pomiędzy wywołaniem funkcji siecznych()  
**Zajecia 12 Rozwiązywanie równań nieliniowych - cz.2**    
Funkcja: bisekcja(f, a, b, tol) oblicza miejsce zerowe za pomocą metody bisekcji z przdziału a,b , tol - krok  
Funkcja: bisekcja_looped(f, a, b, tol, dokladnosc) oblicza wszytskie miejsca zerowe za pomocą metody bisekcji z przdziału a,b , tol - krok  
Funkcja: regulaFalsi(a, b, f, e) oblicza miejsce zerowe za pomocą metody fałszywej linii (regula Falsi) z przdziału a,b , e- krok  
Funkcja: regulaFalsi_looped(a,b,f,dokladnosc,krok) oblicza wszystkie miejsca zerowe za pomocą metody fałszywej linii (regula Falsi) z przdziału a,b , e- krok  
