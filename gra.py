import pygame
import random
from menu import MainMenu
from snake import Game

class Gra():
    def __init__(self):
        pygame.init()
        self.FPS = 15
        self.running, self.snake_playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY= False, False, False, False, False, False
        self.DIS_W, self.DIS_H = 1000, 1000
        self.display = pygame.Surface((self.DIS_W,self.DIS_H))
        self.window = pygame.display.set_mode(((self.DIS_W,self.DIS_H)))
        self.font = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0,0,0) , (255,255,255)
        self.curr_menu = MainMenu(self)
        self.GraSnake = Game(self)
        
    def game_loop(self):
        if self.snake_playing:
            self.GraSnake.run()

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
        
    def draw_text(self, text, size, x, y,color):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
        self.window.blit(text_surface,text_rect)   
                
                
                