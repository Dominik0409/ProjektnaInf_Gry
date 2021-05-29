# -*- coding: utf-8 -*-
"""
Gra kot i mysz
Nie pozwól myszy zostać złapaną!
Wykorzystano bibliotekę pygame.

@author: Asus
"""

import pygame
import random
import time

pygame.init()

#wymiary okna 
wys_okno = 600
szer_okno = 800

#zdefiniowane kolory 
czarny = (0, 0, 0)
zielony = (0, 255, 0)
biały = (255, 255, 255)

szer_kot = 227
wys_kot = 150

#ustawienia wyswietlacza
okno_monitor = pygame.display.set_mode((szer_okno, wys_okno))
pygame.display.set_caption('Uratuj mysz!')

#sledzenie czasu
clock = pygame.time.Clock()

#zaladowanie zdjec
png_mysz = pygame.image.load('mouse.png')
png_kot = pygame.image.load('cat.png')
png_boom = pygame.image.load('boom.png') 

#rodzaj czcionki
over_font = pygame.font.SysFont("comicsans", 60)
