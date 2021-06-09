import pygame
from gra1 import Szachownica

win_szer, win_dl = 800, 800
win = pygame.display.set_mode((win_szer,win_dl))

def klik(pozycja):
    x, y = pozycja
    wiersz = y//pole_rozmiar
    kolumna = x//pole_rozmiar
    return wiersz, kolumna

def main():

    run = True
    szachownica = Szachownica()

    while run:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        szachownica.draw(win)
        szachownica.rozstawienie(win)
        szachownica.rozstawienie_rysuj(win)
        pygame.display.update()
    pygame.quit()

main()
