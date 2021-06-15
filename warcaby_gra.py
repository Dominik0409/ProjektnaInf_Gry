import pygame
from gra1 import Szachownica, Krazek
from warcaby_minimenu import Menu
from warcaby_kolory import kolory

class Gra():

    def __init__(self, win):
        self.win = win
        self.szachownica = Szachownica()
        self.menu = Menu()
        self.selected = None
        self.init_szachownica()
        self.init_menu()

    def init_menu(self):
        self.menu.rysuj_tlo(self.win)
        self.menu.zawartosc(self.win)
        self.menu.przycisk(self.win)

    def init_szachownica(self):
        self.szachownica.draw(self.win)
        self.szachownica.rozstawienie(self.win)
        self.szachownica.rozstawienie_rysuj(self.win)

    def update(self):
        self.szachownica.rozstawienie_rysuj(self.win)
        pygame.display.update()

    def select(self, wiersz, kolumna):
        krazek = self.szachownica.get_krazek(wiersz, kolumna)
        if self.selected:
            wynik = self.ruch(wiersz,kolumna)
            if not wynik:
                self.selected = None
                self.select(wiersz,kolumna)

        if krazek != None and krazek.kolor == self.szachownica.kolejka:
            self.selected = krazek
            return True

        return False

    def ruch(self, wiersz, kolumna):
        krazek = self.szachownica.get_krazek(wiersz, kolumna)
        if self.selected and krazek == None:
                self.szachownica.ruch_krazek(self.selected, wiersz, kolumna)
                self.zmiana_kolejki()
        else:
            return False
        return True

    def zmiana_kolejki(self):
        if self.szachownica.kolejka == kolory["czerwony"]:
            self.szachownica.kolejka = kolory["biały"]
        else:
            self.szachownica.kolejka = kolory["czerwony"]
        pygame.draw.rect(self.win, self.szachownica.kolejka, (1030, 245, 40, 40))
