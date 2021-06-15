''' Ten plik służy do optymalizacji kodu '''

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

    def update(self):
        self.szachownica.rozstawienie_rysuj(self.win)
        pygame.display.update()

    def select(self, wiersz, kolumna):
        '''Wywołanie tej funkcji spowoduje zmianę atrybutu self.selected na True, jeśli użytkownik kliknie na obszar zawierający obiekt klasy Krazek()'''
        
        krazek = self.szachownica.get_krazek(wiersz, kolumna)
        if self.selected: # Jeżeli użytkownik po wybraniu krążka wybierze pole, wtedy można przesunąć krążek na wybrane pole
            wynik = self.ruch(wiersz,kolumna)
            if not wynik: # Kiedy wykonanie ruchu jest niemożliwe, program pozwala użytkownikowi wybrać pole jeszcze raz
                self.selected = None
                self.select(wiersz,kolumna)

        if krazek != None and krazek.kolor == self.szachownica.kolejka: # Warunek określający stan, w którym użytkownikwybierze krążek o kolorze obobwiązującej kolejki
            self.selected = krazek
            pygame.draw.circle(self.win, kolory["szary"], (krazek.x, krazek.y), 20)
            return True

        return False

    def ruch(self, wiersz, kolumna):
        '''Funkcja umożliwiająca ruch krążków po planszy'''
        
        krazek = self.szachownica.get_krazek(wiersz, kolumna)
        if self.selected and krazek == None: # Jeżeli jakis krążek jest wybrany (self.selected = True) oraz wybrane pole do przemiezszczenia się jest puste, wtedy wywołuje się funkcja przemiszczająca krążek, zdefiniowana w klasie Szachownica()
            self.szachownica.ruch_krazek(self.selected, wiersz, kolumna)
            self.szachownica.rozstawienie_rysuj(self.win)
            self.zmiana_kolejki()
        else:
            return False

        return True

    def zbij(self, wiersz, kolumna):
            if self.szachownica.szachownica_uklad[wiersz, kolumna] == 1:
                self.szachownica.szachownica_uklad[wiersz, kolumna] == 2
            else:
                self.szachownica.szachownica_uklad[wiersz, kolumna] == 1

    def zmiana_kolejki(self):
        '''Po wykonaniu ruchu przez krążek konkretnego koloru, możliwe jest wybieranie krążków koloru przeciwnego'''
        
        if self.szachownica.kolejka == kolory["czerwony"]:
            self.szachownica.kolejka = kolory["biały"]
        else:
            self.szachownica.kolejka = kolory["czerwony"]
        pygame.draw.rect(self.win, self.szachownica.kolejka, (1030, 245, 40, 40)) # Prostokąt w części zawierającej menu pozwala określić, czyja jest kolejka
