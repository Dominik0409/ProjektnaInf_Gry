import pygame
import numpy as np
from warcaby_kolory import kolory

win_szer, win_dl = 1200, 800
szach_szer, szach_dl = 800, 800

wiersze = kolumny = 8
pole_rozmiar = szach_szer//wiersze

class Szachownica():

    def __init__(self):
        self.szachownica_uklad = np.zeros((8,8)) # Ten atrybut tworzy macierz o wymiarach 8x8 reprezentująca szachownicę; wszystkie zera reprezentują brak krązka na danym polu na szachownicy
        self.liczba_czerwonych = 12
        self.liczba_bialych = 12
        self.kolejka = kolory["czerwony"] # Gra zaczyna się od gracza czerwonego
        self.rozstawienie(win)

    def draw(self, win):
        '''Funkcja służąca do narysowania typowej planszy do warcab'''
        
        win.fill(kolory["czarny"])
        for w in range(wiersze):
            for k in range(w%2, wiersze, 2):
                pygame.draw.rect(win, kolory["czerwony"], (pole_rozmiar*w,pole_rozmiar*k,pole_rozmiar,pole_rozmiar))

    def rozstawienie(self, win):
        '''Jest to funkcja, która aktualizuje macierz repezentującą szachownicę'''
        
        # Dla wierszy od 0 do 2 (w bibliotece pygame początek układu współrzędnych ekranu jest zawsze w lewym górnym rogu) elementy macierzy będą równe 1
        # Dla wierszy od 5 do 7 elementy macierzy będą równe 2
        
        for w in range(wiersze):
            for k in range(kolumny):
                if w < 3:
                    if k % 2 == (w + 1) % 2: # Ten warunek pozwala na rozmieszczenie krążków "zygzakowo"
                        self.szachownica_uklad[w,k] = 1
                elif w > 4:
                    if k % 2 == (w + 1) % 2:
                        self.szachownica_uklad[w,k] = 2

    def rozstawienie_rysuj(self, win):
        ''' Funkcja, za pomocą której program rysuje obiekty klasy Krazek() na wyznaczonych polach planszowych'''
        
        for w in range(wiersze):
            for k in range(kolumny):
                if self.szachownica_uklad[w,k] == 1: # Dla elementów macierzy reprezentującej szachownicę równych 1, program rysuje białe krążki
                    krazek_bialy = Krazek(w, k, kolory["bialy"])
                    krazek_bialy.draw(win)
                elif self.szachownica_uklad[w,k] == 2: # Dla elementów macierzy reprezentującej szachownicę równych 2, program rysuje czerwone krążki
                    krazek_czerwony = Krazek(w, k, kolory["czerwony"])
                    krazek_czerwony.draw(win)

    def ruch_krazek(self, krazek, wiersz, kolumna):
        '''Kiedy krążek się porusza, pozycje w macierzy reprezntującej szachownicę zamieniając się miejscami'''
        
        self.szachownica_uklad[krazek.wiersz, krazek.kolumna], self.szachownica_uklad[wiersz,kolumna] = self.szachownica_uklad[wiersz,kolumna], self.szachownica_uklad[krazek.wiersz, krazek.kolumna]
        krazek.ruch(wiersz,kolumna)

    def get_krazek(self, wiersz, kolumna):
        '''Funkcja pozwalająca na zwrócenie obiektu klasy Krazek()'''
        
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
        self.pozycja() # W każdym przypadku zmiany pozycji danego krążka, ta funkcja jest wywoływana

    def pozycja(self):
        '''Funkcja wspomagająca obliczenie pozycji danego krążka w układzie kartezjańskim'''
        
        self.x = win_szer/2 + self.kolumna*pole_rozmiar
        self.y = win_dl/2 * self.wiersz*pole_rozmiar

    def draw(self, win):
        '''Funkcja rysująca krążek o danych współrzędnych i kolorze'''
        
        promien = pole_rozmiar/3
        pygame.draw.circle(win, self.kolor, (self.x, self.y), promien)
        
    def ruch(self, wiersz, kolumna):
        '''Ta funkcja jest wywoływana, kiedy dany krążek się porusza po planszy'''
        
        self.wiersz = wiersz
        self.kolumna = kolumna
        self.pozycja()
