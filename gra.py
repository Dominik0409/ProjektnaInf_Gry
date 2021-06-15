import pygame
import random
from menu import MainMenu
from menu import Tworcy
from snake import Game
import escape
import Pt1

class Gra():
    def __init__(self):
        pygame.init()
        self.FPS = 15
        self.running, self.snake_playing, self.kim_playing, self.kik_playing = True, False, False, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY= False, False, False, False, False, False
        self.DIS_W, self.DIS_H = 800, 800
        self.display = pygame.Surface((self.DIS_W,self.DIS_H))
        self.window = pygame.display.set_mode(((self.DIS_W,self.DIS_H)))
        self.font = 'zasoby\czcionki\8-BIT WONDER.TTF'
        self.BLACK, self.WHITE, self.PURPLE = (0,0,0) , (255,255,255) , (119,65,235)
        self.mainmenu = MainMenu(self)
        self.tworcy = Tworcy(self)
        self.curr_menu = self.mainmenu
        self.GraSnake = Game(self)

        
    def game_loop(self):
        if self.snake_playing:
            self.GraSnake.run()
        elif self.kim_playing:
             escape.petla()
        elif self.kik_playing:
            Pt1.petla()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY =  True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY =  True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY =  True
                    
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY= False, False, False, False, False, False
        
    def draw_text(self, text, size, x, y, color):
        font_1 = pygame.font.Font(self.font, size)
        text_surface_1 = font_1.render(text, True, self.BLACK)
        text_rect_1 = text_surface_1.get_rect()
        text_rect_1.topleft = (x+5,y+5)
        font_2 = pygame.font.Font(self.font, size)
        text_surface_2 = font_2.render(text, True, color)
        text_rect_2 = text_surface_2.get_rect()
        text_rect_2.topleft = (x,y)
        self.display.blit(text_surface_1,text_rect_1)
        self.window.blit(text_surface_1,text_rect_1)
        self.display.blit(text_surface_2,text_rect_2)
        self.window.blit(text_surface_2,text_rect_2)  
                
                
                