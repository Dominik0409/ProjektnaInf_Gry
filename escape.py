  
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

szer_mysz = 71
wys_mysz = 70

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
czcionka = pygame.font.SysFont("comicsans", 60)

#definiowanie potrzebnych funkcji

def linia(liniaX,liniaY,liniaW,liniaH, kolor):
    pygame.draw.rect(okno_monitor, kolor,[liniaX,liniaY,liniaW,liniaH])

def rekord(licz):
	font = pygame.font.SysFont(None,30)
	tekst = font.render("Score : "+str(licz), True, czarny)
	okno_monitor.blit(tekst,(0,10))

def wyswietlanie_tekst(tekst, font):
	tekst_Styl = font.render(tekst, True, zielony)
	return tekst_Styl, tekst_Styl.get_rect()

def informacja_zderzenie(tekst,size,x,y):
    font = pygame.font.Font("freesansbold.ttf",size)
    tekst_styl, tekst_prostokat = wyswietlanie_tekst(tekst, font)
    tekst_prostokat.center = (x,y)
    okno_monitor.blit(tekst_styl, tekst_prostokat)
    

def zderzenie(x,y):
    okno_monitor.blit(png_boom, (x,y))
    informacja_zderzenie("Mysz została schwytana", 64, szer_okno/2, wys_okno/2)
    
    
    pygame.display.update()
    time.sleep(2)
    petla()


def mysz(x,y):
    okno_monitor.blit(png_mysz, (x,y))

def kot(x,y):
    okno_monitor.blit(png_kot, (x,y))

def petla():
    x = (szer_okno * 0.45) 
    y = (wys_okno * 0.8) 

    x_zmiana = 0

    kot_startx = random.randrange(200,585 ) 
    kot_starty = -600
    kot_predkosc = 8
    kot_szer = 227 
    kot_wys = 150  
    licz = 0
    liniaY = 0
    liniaX = 400
    liniaW = 20
    liniaH = 450
    linia_przyspieszenie = 10
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()               
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_zmiana = -15
                if event.key == pygame.K_RIGHT:
                    x_zmiana = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_zmiana = 0
        x += x_zmiana
        okno_monitor.fill(biały)
        linia(150, 0, 20, wys_okno,czarny)
        linia(szer_okno -170, 0, 20, wys_okno, czarny)
        kot(kot_startx, kot_starty)
        mysz(x,y)
        if x > szer_okno - szer_mysz or x < 0: 
            zderzenie(x,y)
        if kot_starty > wys_okno: 
            kot_starty = 0 - kot_szer
            kot_startx = random.randrange(200,585)
        if y < kot_starty + kot_wys: 
            if x > kot_startx and x < kot_startx + kot_szer: 
                zderzenie(x-25, y- wys_mysz/2)
            if x + szer_mysz > kot_startx and x + szer_mysz < kot_startx + kot_szer:
                zderzenie(x, y-wys_mysz/2)
        rekord(licz)
        licz += 1
        kot_starty += kot_predkosc


        pygame.display.update()
        clock.tick(60)

