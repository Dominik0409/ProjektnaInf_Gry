import pygame
from gra import bialy, czerwony, czarny, zolty, zielony, Szachownica
from warcaby_gra import Gra


class Menu():

    def __init__(self):
        self.szerokosc = 400
        self.dlugosc = 800

    def rysuj_tlo(self, win):
        boazeria = pygame.image.load("boazeria.jpg")
        pygame.transform.scale(boazeria, (self.szerokosc, self.dlugosc))
        win.blit(boazeria, (self.dlugosc, 0))

    def zawartosc(self, win):
        '''Funkcja, która tworzy zawartość menu'''

        gra = Gra(win)
        szachownica = Szachownica()

        # Tekst powitalny
        pygame.font.init()
        czcionka_wstep = pygame.font.SysFont("Algerian", 36)
        wstep = czcionka_wstep.render("Zapraszam do gry!", False, zolty)
        win.blit(wstep, (820, 50))

        # Informacje o kolejce
        czcionka_kolejka = pygame.font.SysFont("Times New Roman", 24)
        kolejka = czcionka_kolejka.render("Aktualna kolejka: ", False, bialy)
        win.blit(kolejka, (820, 150))
        pygame.draw.rect(win, czarny, (1030, 145, 45, 45))
        pygame.draw.rect(win, gra.kolejka, (1030, 145, 40, 40))

        # Informacje o liczbie pozostąłych krążków
        czcionka_lkrazek = pygame.font.SysFont("Times New Roman", 18)
        krazek_b = czcionka_lkrazek.render(f"Liczba pozostałych białych krążków:", False, zielony)
        krazek_c = czcionka_lkrazek.render(f"Liczba pozostałych czerwonych krążków:", False, zielony)
        lkrazek_b = czcionka_lkrazek.render(f"{szachownica.liczba_bialych}", False, bialy)
        lkrazek_c = czcionka_lkrazek.render(f"{szachownica.liczba_czerwonych}", False, czerwony)
        win.blit(krazek_b, (820, 250))
        win.blit(krazek_c, (820, 300))
        win.blit(lkrazek_b, (1150, 250))
        win.blit(lkrazek_c, (1150, 300))



