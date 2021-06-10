''' Ten plik służy optymalizacji kodu '''

import pygame
from gra1 import Szachownica, Krazek
from warcaby_minimenu import Menu

class Gra():
    '''Klasa została stworzona jako moduł sterujący warcabami'''
    
    def __init__(self, win):
        self.win = win
        self.szachownica = Szachownica()
        self.menu = Menu()
        self.selected = None
        self.kolejka = czerwony
    
    def init_menu(self):
        self.menu.rysuj_tlo(self.win)
        self.menu.zawartosc(self.win)
        self.menu.przycisk(self.win)

    def init_szachownica(self):
        self.szachownica.draw(self.win)
        self.szachownica.rozstawienie(self.win)
        self.szachownica.rozstawienie_rysuj(self.win)

