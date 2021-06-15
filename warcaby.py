import pygame
from gra1 import pole_rozmiar, wiersze, kolumny
from warcaby_gra import Gra


win_szer, win_dl = 1200, 800
szach_szer, szach_dl = 800, 800
win = pygame.display.set_mode((win_szer,win_dl))


def klik(pozycja):
    x, y = pozycja
    wiersz = y//pole_rozmiar
    kolumna = x//pole_rozmiar
    return wiersz, kolumna

def main():

    run = True
    gra = Gra(win)

    while run:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pozycja = pygame.mouse.get_pos()
                wiersz, kolumna = klik(pozycja)
                try:
                    gra.select(wiersz, kolumna)
                except IndexError:
                    pass
                if (pozycja[0] > 900 and pozycja[0] < 1115) and (pozycja[1] > 735 and pozycja[1] < 770):
                    run = False

        gra.update()

