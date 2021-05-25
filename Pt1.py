# -*- coding: utf-8 -*-
"""
Gra kółko i krzyżyk

Na wyswietlonej planszy zaznacz symol kółka lub krzyżyka.
Osoba, która jako pierwsza postawi swoje 3 symbole w jednej linii
(tj poziomo, pionowo lub po przekątnej) wygrywa grę.

Do uruchomienia potrzebna biblioteka pygame
"""

import pygame
pygame.init()

#otwarcie okna
win = pygame.display.set_mode((550,550))

#oznaczenie tablicy, rzędy/kolumny
board = [[0,0,0],[0,0,0],[0,0,0]]