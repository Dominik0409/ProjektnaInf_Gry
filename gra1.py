import pygame
import numpy as np
from warcaby_kolory import kolory

win_szer, win_dl = 1200, 800
szach_szer, szach_dl = 800, 800
win = pygame.display.set_mode((win_szer,win_dl))

wiersze = kolumny = 8
pole_rozmiar = szach_szer//wiersze

class Szachownica():

    def __init__(self):
        self.szachownica_uklad = np.zeros((8,8))
        self.liczba_czerwonych = 12
        self.liczba_bialych = 12
        self.kolejka = kolory["czerwony"]

    def draw(self, win):
        win.fill(kolory["czarny"], (0, 0, szach_dl, szach_szer))
        for w in range(wiersze):
            for k in range(w%2, wiersze, 2):
                pygame.draw.rect(win, kolory["bordowy"], (pole_rozmiar*w,pole_rozmiar*k,pole_rozmiar,pole_rozmiar))

    def rozstawienie(self, win):
        for w in range(wiersze):
            for k in range(kolumny):
                if w < 3:
                    if k%2 == (w+1)%2:
                        self.szachownica_uklad[w,k] = 1
                elif w > 4:
                    if k % 2 == (w + 1) % 2:
                        self.szachownica_uklad[w,k] = 2

    def rozstawienie_rysuj(self, win):
        self.draw(win)
        for w in range(wiersze):
            for k in range(kolumny):
                if self.szachownica_uklad[w,k] == 1:
                    krazek_bialy = Krazek(w, k, kolory["biały"])
                    krazek_bialy.draw(win)
                elif self.szachownica_uklad[w,k] == 2:
                    krazek_czerwony = Krazek(w, k, kolory["czerwony"])
                    krazek_czerwony.draw(win)

    def ruch_krazek(self, krazek, wiersz, kolumna):
        self.szachownica_uklad[krazek.wiersz, krazek.kolumna], self.szachownica_uklad[wiersz,kolumna] = self.szachownica_uklad[wiersz,kolumna], self.szachownica_uklad[krazek.wiersz, krazek.kolumna]
        krazek.ruch(wiersz,kolumna)

    def get_krazek(self, wiersz, kolumna):
        if self.szachownica_uklad[wiersz,kolumna] == 1:
            kolor = kolory["biały"]
            return Krazek(wiersz, kolumna, kolor)
        elif self.szachownica_uklad[wiersz,kolumna] == 2:
            kolor = kolory["czerwony"]
            return Krazek(wiersz, kolumna, kolor)



class Krazek():

    def __init__(self, wiersz, kolumna, kolor):
        self.kolor = kolor
        self.wiersz = wiersz
        self.kolumna = kolumna
        self.x = 0
        self.y = 0
        self.pozycja()

    def pozycja(self):
        self.x = (pole_rozmiar//2) + self.kolumna*pole_rozmiar
        self.y = (pole_rozmiar//2) + self.wiersz*pole_rozmiar

    def draw(self, win):
        promien = pole_rozmiar/3
        pygame.draw.circle(win, self.kolor, (self.x, self.y), promien)

    def ruch(self, wiersz, kolumna):
        self.wiersz = wiersz
        self.kolumna = kolumna
        self.pozycja()

    def __repr__(self):
        return str((self.wiersz, self.kolumna, self.kolor))

