"# ProjektnaInf_Gry" 
Projekt polega na stworzeniu aplikacji w której użytkownik może zagrać w kilka prostych gier. Każdy z członków grupy miał za zadanie wybrać ulubioną grę i odtworzyć jej działanie za pomocą kodu języka programowania python, a następnie wspólnie stworzyć menu główne aplikacji. Jako główne narzędzie zdecydowaliśmy się wybrać bibliotekę pygame, która została stworzona z przeznaczeniem do tworzenia gier komputerowych. Zawiera ona takie metody, które pozwalają na wyświetlanie grafik, odtwarzanie dźwięków, śledzenie czasu czy obsługę myszki i klawiatury.

Opis poszczególnych plików:

1. main.py - jest to plik za pomocą którego inicializujemy aplikację
2. gra.py - to tutaj znajdują się funkcję odpowiadające za status aplikacji oraz to w jaką grę obecnie gramy
3. menu.py - tutaj znajdują się klasy odpowiadające za wyświetlanie i działanie menu głównego
4. snake.py - tutaj zanjduje się kod gry snake
5. escape.py - tutaj znajduje się kod gry kot i mysz
6. Pt1.py - tutaj znajduje się kod gry kółko i krzyżyk
7. pliki png - są to tekstury wykorzystywane przy wyświetlaniu obrazu
8. pliki mp3 - pliki audio wykorzystywane jako efekty dźwiękowe

Opis Menu:
Proste menu główne po którym użytkownik porusza się za pomocą strzałek na klawiaturze. Została wykorzystana darmowa czcionka 8-bit. Do wyboru są 4 gry oraz opcja wyjścia.

Opis gry snake:
Gra w której użytkownik za pomocą strzałek steruje tytułowym wężem. Za zadanie ma zdobyć jak najwięcej punktów. Punkty zdobywa się zjadając czerwone i żółte klocki. Czerwone dają jeden punkt, natomiast żółte trzy, ale zwiększają także prędkość węża, co czyni gre trudniejszą. Gra kończy się w momencie udeżenia w samego siebie. Po przegranej gracz widzi ilość uzyskanych punktów oraz ma możliwość ponownej gry.

Opis gry kółko i krzyżyk:
Znana gra w kółko i krzyżyk. Dwóch graczy ma za zadanie ułożenie odpowiednio kółka lub krzyżyka w lini po trzy. Jeśli nikomu się nie uda gra kończy się remisem. Po naciśnięciu spacji gra się resetuje, a gracze dostają ponowną sznsę.

Opis gry kot i mysz:
Gracz ma za zadanie nie dopuścić aby kot zjadł mysz. Sterowanie odbywa się za pomocą klawiszy prawo lewo. Kot pojawia się w odstępach czasu w losowym położeniu na ekranie. Po przegranej gra resetuje się automatycznie.
