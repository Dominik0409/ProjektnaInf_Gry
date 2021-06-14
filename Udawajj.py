# -*- coding: utf-8 -*-
"""
Proba generalna
probowałem przykryć tekst tekstem, ale nadal jakas poswiata zostaje
cos remis nie dziala ani countem ani inaczej
@author: giera
"""

import pygame
import time

#init biblioteki
pygame.init()


#Okno potrzebne do wyswietlenia gry
width = 600
height = 600

win = pygame.display.set_mode((width,height))

#wyswietlanie tekstu kto wygral
def kolko():
    font = font = pygame.font.SysFont(None, 40)
    text_surface = font.render('Wygrywa Team Kółko', True, (0, 0, 255))
    win.blit(text_surface, (width/4, height/2))
    pygame.display.update()
    #tylko to też nie zachowuje się jak 1 sekunda tylko dziesięć (sprawdzone)
    time.sleep(1)
    text_surface = font.render('Wygrywa Team Kółko', True, (135, 206, 250))
    win.blit(text_surface, (width/4, height/2))
    pygame.display.update()
    #win_check()
    
def krzyzyk():
    font = font = pygame.font.SysFont(None, 40)
    text_surface = font.render('Wygrywa Team Krzyżyk', True, (0, 0, 255))
    win.blit(text_surface, (width/4, height/2))
    pygame.display.update()
    time.sleep(1)
    text_surface = font.render('Wygrywa Team Krzyżyk', True, (135, 206, 250))
    win.blit(text_surface, (width/4, height/2))
    pygame.display.update()
    #win_check()
    
def remis():
    font = font = pygame.font.SysFont(None, 40)
    text_surface = font.render('Remis', True, (0, 0, 255))
    win.blit(text_surface, (width/2.5, height/2))
    pygame.display.update()
    time.sleep(1)
    text_surface = font.render('Remis', True, (135, 206, 250))
    win.blit(text_surface, (width/2.5, height/2))
    pygame.display.update()
    
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
   #?????????????????????
    else:
        return True
    
    
    # if count == 9:
    #     remis()
    
    
#Main
#potrzebne do podtrzymania pętli

def petla():
    #plansza 3x3
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    run = True
    won = False
    count = 0
    draw_object = 'o'
    while run:
    
        #dla zdarzenia
        for event in pygame.event.get():
    
            #zakoncz
            if event.type == pygame.QUIT:
                run = False
    
            #spacja do wznowienia gry
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #znowu patrzymy czy miejsce zajęte czy nie
                    first_open = True
                    second_open = True
                    third_open = True
                    fourth_open = True
                    fifth_open = True
                    sixth_open = True
                    seventh_open = True
                    eighth_open = True
                    ninth_open = True
                    
                    run = True
                    won = False
                    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    count = 0
                    
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
    
            #które miejsca zajęte po kliknięciu
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
    
                #czy po wcisnieciu kursorem jest wolne
                if won != True:
                    if first.collidepoint(pos) and first_open:
                        #pierwszy ruch
                        if draw_object == 'o':
                            #kształt kółko
                            pygame.draw.circle(win, circle_color,(125,125), 60 , circle_width)
                            #tzn ze kolejny ruch musi byc przeciwnika
                            draw_object = 'x'
                            board[0][0] = 1
                           
                        else:
                            #jesli to nie kolko, to krzyzyk
                            pygame.draw.line(win, cross_color, (125 + space, 125 - space),(125 - space, 125 +space),cross_width)
                            pygame.draw.line(win, cross_color, (125 + space, 125 + space),(125 - space, 125 -space),cross_width)
                            #kolejny ruch bedzie przeciwnika
                            draw_object = 'o'
                            board[0][0] = 2
                        #przelaczymy miejsce na zajęte
                        first_open = False
                        count += 1
    
                    #pętle analogiczne do tej powyżej, sprawdzanie warunków
                    if second.collidepoint(pos) and second_open:
                        if draw_object == 'o':
                            pygame.draw.circle(win, circle_color,(300, 125), 60 , circle_width)
                            draw_object = 'x'
                            board[0][1] = 1
                        else:
                            pygame.draw.line(win, cross_color, (300 + space, 125 - space), (300 - space, 125 + space),cross_width)
                            pygame.draw.line(win, cross_color, (300 + space, 125 + space), (300 - space, 125 - space),cross_width)
                            draw_object = 'o'
                            board[0][1] = 2
                        second_open = False
                        count += 1
    
                    if third.collidepoint(pos) and third_open:
                        if draw_object == 'o':
                            pygame.draw.circle(win, circle_color,(475,125), 60 , circle_width)
                            draw_object = 'x'
                            board[0][2] = 1
                        else:
                            pygame.draw.line(win, cross_color, (475 + space, 125 - space),(475 - space, 125 + space),cross_width)
                            pygame.draw.line(win, cross_color, (475 + space, 125 + space),(475 - space, 125 - space),cross_width)
                            draw_object = 'o'
                            board[0][2] = 2
                        third_open = False
                        count += 1
                        
    
                    if fourth.collidepoint(pos) and fourth_open:
                        if draw_object == 'o':
                            pygame.draw.circle(win, circle_color, (125,300), 60 , circle_width)
                            draw_object = 'x'
                            board[1][0] = 1
                        else:
                            pygame.draw.line(win, cross_color, (125 + space, 300 - space),(125 - space, 300 + space),cross_width)
                            pygame.draw.line(win, cross_color, (125 + space, 300 + space),(125 - space, 300 - space),cross_width)
                            draw_object = 'o' 
                            board[1][0] = 2
                        fourth_open = False
                        count += 1
    
                    if fifth.collidepoint(pos) and fifth_open:
                        if draw_object == 'o':
                            pygame.draw.circle(win, circle_color,(300,300), 60 , circle_width)
                            draw_object = 'x'
                            board[1][1] = 1
                        else:
                            pygame.draw.line(win, cross_color, (300 + space, 300 - space), (300 - space, 300 + space),cross_width)
                            pygame.draw.line(win, cross_color, (300 +  space, 300 + space), (300 - space, 300 - space),cross_width)
                            draw_object = 'o'
                            board[1][1] = 2
                        fifth_open = False
                        count += 1
    
                    if sixth.collidepoint(pos) and sixth_open:
                        if draw_object == 'o':
                            pygame.draw.circle(win, circle_color,(475,300), 60 , circle_width)
                            draw_object = 'x'
                            board[1][2] = 1
                        else:
                            pygame.draw.line(win, cross_color, (475 + space, 300 - space),( 475 - space, 300 + space),cross_width)
                            pygame.draw.line(win, cross_color, (475 + space, 300 + space),( 475 - space, 300 - space),cross_width)
                            draw_object = 'o'
                            board[1][2] = 2
                        sixth_open = False
                        count += 1
    
                    if seventh.collidepoint(pos) and seventh_open:
                        if draw_object == 'o':
                            pygame.draw.circle(win, circle_color,(125,475), 60 , circle_width)
                            draw_object = 'x'
                            board[2][0] = 1
                        else:
                            pygame.draw.line(win, cross_color, (125 + space, 475 - space),( 125 - space, 475 + space),cross_width)
                            pygame.draw.line(win, cross_color, (125 + space, 475 + space),( 125 - space, 475 - space),cross_width)
                            draw_object = 'o'
                            board[2][0] = 2
                        seventh_open = False
                        count += 1
    
                    if eighth.collidepoint(pos) and eighth_open:
                        if draw_object == 'o':
                            pygame.draw.circle(win, circle_color,(300,475), 60 , circle_width)
                            draw_object = 'x'
                            board[2][1] = 1
                        else:
                            pygame.draw.line(win, cross_color, (300 + space, 475 - space),(300 - space, 475 + space),cross_width)
                            pygame.draw.line(win, cross_color, (300 + space, 475 + space),(300 - space, 475 - space),cross_width)
                            draw_object = 'o'
                            board[2][1] = 2
                        eighth_open = False
                        count += 1
    
                    if ninth.collidepoint(pos) and ninth_open:
                        if draw_object == 'o':
                            pygame.draw.circle(win, circle_color,(475,475), 60 , circle_width)
                            draw_object = 'x'
                            board[2][2] = 1
                        else:
                            pygame.draw.line(win, cross_color, (475 + space, 475 - space),(475 - space, 475 + space),cross_width)
                            pygame.draw.line(win, cross_color, (475 + space, 475 + space),(475 - space, 475 - space),cross_width)
                            draw_object = 'o'
                            board[2][2] = 2
                        ninth_open = False
                        count += 1
    
    
    #czy wygrało kółko czy krzyżyk
        if win_check(1):
            kolko()
            won = True
            
        if win_check(1) != True and count > 8:
            remis()
            won = True
        # if win_check(1):
        #      if count == 9:
        #          R = False
        #          if R == won:
        #              remis()
        #              #no bo jesli won !=true to pozostaje false
        #          won = True
                 
            #pygame.display.update()
        if win_check(2):
            krzyzyk()   
            won = True
        
        if win_check(2) != True and count > 8:
            remis()
            won = True
            
        # if won == False:
        #     remis()
            
        # if win_check(1):
        #      if count == 9:
        #          R = False
        #          if R == won:
        #              remis()
        #          won = True
        
        # #nie mogę tego wykminić, won na początku ma false wiec trzeba uwazac
        # if count == 9:
        #     R = False
        #     if R == won:
        #         remis()
        #         won = True
        #count się źle zlicza
        
           
        #odswieży ekran
        pygame.display.update()
        
    
    #zamknie pętle