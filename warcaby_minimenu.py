import pygame
from gra1 import Szachownica
from warcaby_kolory import kolory

class Menu():

    def __init__(self):
        self.szerokosc = 400
        self.dlugosc = 800

    def rysuj_tlo(self, win):
        boazeria = pygame.image.load("boazeria.jpg")
        siding = pygame.image.load("siding.jpg")

        pygame.transform.scale(boazeria, (self.szerokosc, self.dlugosc))
        win.blit(boazeria, (self.dlugosc, 0))

        win.blit(siding, (self.dlugosc, 700))

    def zawartosc(self, win):
        '''Funkcja, która tworzy zawartość menu'''

        szachownica = Szachownica()

        # Tekst powitalny
        pygame.font.init()
        czcionka_wstep = pygame.font.SysFont("Algerian", 36)
        wstep = czcionka_wstep.render("Zapraszam do gry!", False, kolory["żółty"])
        win.blit(wstep, (820, 50))

        # Informacje o kolejce
        czcionka_kolejka = pygame.font.SysFont("Times New Roman", 24)
        kolejka = czcionka_kolejka.render("Aktualna kolejka: ", False, kolory["biały"])
        win.blit(kolejka, (820, 250))
        pygame.draw.rect(win, kolory["czarny"], (1030, 245, 45, 45))
        pygame.draw.rect(win, szachownica.kolejka, (1030, 245, 40, 40))

        # Informacje o liczbie pozostąłych krążków
        czcionka_lkrazek = pygame.font.SysFont("Times New Roman", 18)
        krazek_b = czcionka_lkrazek.render(f"Liczba pozostałych białych krążków:", False, kolory["zielony"])
        krazek_c = czcionka_lkrazek.render(f"Liczba pozostałych czerwonych krążków:", False, kolory["zielony"])
        lkrazek_b = czcionka_lkrazek.render(f"{szachownica.liczba_bialych}", False, kolory["biały"])
        lkrazek_c = czcionka_lkrazek.render(f"{szachownica.liczba_czerwonych}", False, kolory["czerwony"])
        win.blit(krazek_b, (820, 375))
        win.blit(krazek_c, (820, 425))
        win.blit(lkrazek_b, (1150, 375))
        win.blit(lkrazek_c, (1150, 425))

    def przycisk(self, win):
        pygame.font.init()

        przycisk_x = 900
        przycisk_y = 735
        przycisk_dl = 35
        przycisk_szer = 215

        pygame.draw.rect(win, kolory["szary"], (przycisk_x, przycisk_y, przycisk_szer, przycisk_dl))
        czcionka_przycisk = pygame.font.SysFont("Arial", 14)
        tekst_przycisk = czcionka_przycisk.render("Jeżeli chcesz zakończyć grę, kliknij tutaj!", False, kolory["czarny"])
        win.blit(tekst_przycisk, (przycisk_x , przycisk_y + (przycisk_dl)//4))


