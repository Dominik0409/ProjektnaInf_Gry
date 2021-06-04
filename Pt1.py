# -*- coding: utf-8 -*-
"""
Gra kółko i krzyżyk

Na wyswietlonej planszy zaznacz symol kółka lub krzyżyka.
Osoba, która jako pierwsza postawi swoje 3 symbole w jednej linii
(tj poziomo, pionowo lub po przekątnej) wygrywa.

Do uruchomienia potrzebna biblioteka pygame
"""

import pygame


#init biblioteki
pygame.init()


#Okno potrzebne do wyswietlenia gry
width = 600
height = 600

win = pygame.display.set_mode((width,height))
#kolory RGB
win.fill((135, 206, 250))
circle_color = (255, 255, 0)
line_color = (145, 139, 200)
rect_color = (30,144, 255) 

#parametry kształtów
circle_radius = 60
circle_width = 15
line_width = 10
space = 55
cross_width = 25
cross_color = (192, 192, 192)

#Nazwa okna
pygame.display.set_caption('Kółko i krzyżyk')

#układ gry, 3 rzędy i 3 kolumny
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#font = pygame.font.Font('freesansbold.ttf', 10)

#plansza 3x3
first = pygame.draw.rect(win, rect_color, (50,50,150,150))
second = pygame.draw.rect(win, rect_color, (225,50,150,150))
third = pygame.draw.rect(win, rect_color, (400,50,150,150))

fourth = pygame.draw.rect(win, rect_color, (50,225,150,150))
fifth = pygame.draw.rect(win, rect_color, (225,225,150,150))
sixth = pygame.draw.rect(win, rect_color, (400,225,150,150))

seventh = pygame.draw.rect(win,rect_color, (50,400,150,150))
eighth = pygame.draw.rect(win, rect_color, (225,400,150,150))
ninth = pygame.draw.rect(win, rect_color, (400,400,150,150))

#pierwszy ruch
draw_object = 'o'

#czy miejsce zajęte czy nie
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

#board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check(num):
    #dla każdej poziomej listy
    for row in board:
        #dla każdego symoblu w małej liscie
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True


    for column in range(3):
        #każdą kolumnę pionowo
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True
    
    
    for tile in range(3):
        #po przekątnej z lewej do prawej
        #0,0; 1,1; 2,2
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True
    
    
    for tile in range(3):
        #po przekątnej z prawej do lewej
        #0,2; 1,1; 2,0
        if board[tile][2-tile] == num:
            continue
        else:
            break
    else:
        return True

