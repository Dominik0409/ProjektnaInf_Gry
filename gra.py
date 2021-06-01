import pygame


win_szer, win_dl = 800, 800
boazeria = pygame.image.load("boazeria.jpg")

czarny = (0,0,0)
czerwony = (255,0,0)
bialy = (255,255,255)
wiersze = kolumny = 8
pole_rozmiar = win_szer//wiersze

class Szachownica():

    def __init__(self):
        self.szachownica = []
        self.liczba_czerwonych = 12
        self.liczba_bialych = 12

    def draw(self, win):
        win.fill(czarny)
        for w in range(wiersze):
            for k in range(w%2, wiersze, 2):
                pygame.draw.rect(win, czerwony, (pole_rozmiar*w,pole_rozmiar*k,pole_rozmiar,pole_rozmiar))

    def rozstawienie(self, win):
        for w in range(wiersze):
            for k in range(kolumny):
                if k % 2 == (w+1)%2:
                    if w < 3:
                        krazek_czerwony = Krazek(w, k, czerwony)
                        krazek_czerwony.draw(win)
                    elif w > 4:
                        krazek_bialy = Krazek(w, k, bialy)
                        krazek_bialy.draw(win)


class Krazek():

    def __init__(self, wiersz, kolumna, kolor):
        self.kolor = kolor
        self.wiersz = wiersz
        self.kolumna = kolumna
        self.x = 0
        self.y = 0
        self.pozycja()

    def pozycja(self):
        self.x = win_szer/2 + self.kolumna*pole_rozmiar
        self.y = win_dl/2 * self.wiersz*pole_rozmiar

    def draw(self, win):
        promien = pole_rozmiar/3
        pygame.draw.circle(win, self.kolor, (self.x, self.y), promien)



