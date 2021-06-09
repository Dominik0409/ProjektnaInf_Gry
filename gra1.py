import pygame
import numpy as np
from warcaby_kolory import kolory

win_szer, win_dl = 1200, 800
szach_szer, szach_dl = 800, 800

wiersze = kolumny = 8
pole_rozmiar = szach_szer//wiersze

class Szachownica():

    def __init__(self):
        self.szachownica = np.zeros((8,8))
        self.liczba_czerwonych = 12
        self.liczba_bialych = 12
        self.rozstawienie(win)

    def draw(self, win):
        win.fill(czarny)
        for w in range(wiersze):
            for k in range(w%2, wiersze, 2):
                pygame.draw.rect(win, czerwony, (pole_rozmiar*w,pole_rozmiar*k,pole_rozmiar,pole_rozmiar))

    def rozstawienie(self, win):
        for w in range(wiersze):
            for k in range(kolumny):
                if w < 3:
                    if k%2 == (w+1)%2:
                        self.szachownica[w,k] = 1
                elif w > 4:
                    if k % 2 == (w + 1) % 2:
                        self.szachownica[w,k] = 2

    def rozstawienie_rysuj(self, win):
        for w in range(wiersze):
            for k in range(kolumny):
                if self.szachownica[w,k] == 1:
                    krazek_bialy = Krazek(w, k, bialy)
                    krazek_bialy.draw(win)
                elif self.szachownica[w,k] == 2:
                    krazek_czerwony = Krazek(w, k, czerwony)
                    krazek_czerwony.draw(win)

    def ruch_krazek(self, krazek, wiersz, kolumna):
        print(self.szachownica)
        self.szachownica[krazek.wiersz, krazek.kolumna], self.szachownica[wiersz,kolumna] = self.szachownica[wiersz,kolumna], self.szachownica[krazek.wiersz, krazek.kolumna]
        krazek.ruch(wiersz,kolumna)
        pass

    def get_krazek(self, wiersz, kolumna):
        return self.szachownica[wiersz,kolumna]

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
        
    def ruch(self, wiersz, kolumna):
        self.wiersz = wiersz
        self.kolumna = kolumna
        self.pozycja()
