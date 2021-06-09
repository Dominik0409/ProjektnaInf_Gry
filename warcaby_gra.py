import pygame
from gra import Szachownica, Krazek

win_szer, win_dl = 800, 800
win = pygame.display.set_mode((win_szer,win_dl))

czarny = (0,0,0)
czerwony = (255,0,0)
bialy = (255,255,255)
wiersze = kolumny = 8
pole_rozmiar = win_szer//wiersze


class Gra():

    def __init__(self, win):
        self.win = win
        self.szachownica = Szachownica()
        self.selected = None
        self.kolejka = czerwony

   # def select(self, wiersz, kolumna):
       # if self.selected:
