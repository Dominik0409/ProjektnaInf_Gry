import pygame

class Menu():
    def __init__(self, gra):
        self.gra = gra
        self.mid_w, self.mid_h = self.gra.DIS_W/2, self.gra.DIS_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -40
        
    def draw_cursor(self):
        self.gra.draw_text('*', 40, self.cursor_rect.x, self.cursor_rect.y, self.gra.PURPLE)
        
    def blit_screen(self):
        self.gra.window.blit(self.gra.display, (0,0))
        pygame.display.update()
        self.gra.reset_keys()
#klasa menu glownego        
class MainMenu(Menu):
    def __init__(self,gra):
        Menu.__init__(self, gra)
        self.state = "Snake"
        self.snakex, self.snakey = 150, 200
        self.kikx, self.kiky = self.snakex, self.snakey + 40
        self.warcabyx, self.warcabyy = self.snakex, self.snakey + 80
        self.kimx, self.kimy = self.snakex, self.snakey + 120
        self.exitx, self.exity = self.snakex, self.snakey + 160
        self.cursor_rect.midtop = (self.snakex + self.offset, self.snakey)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.gra.check_events()
            self.check_input()
            bg = pygame.image.load('bg1.jpg').convert()
            self.gra.display.blit(bg, (0,0))
            self.gra.draw_text('Wybierz gre', 70, 40, 100, self.gra.PURPLE)
            self.gra.draw_text('Snake', 40, self.snakex,self.snakey, self.gra.PURPLE)
            self.gra.draw_text('Kolko i krzyzyk', 40, self.kikx,self.kiky, self.gra.PURPLE)
            self.gra.draw_text('Warcaby', 40, self.warcabyx,self.warcabyy, self.gra.PURPLE)
            self.gra.draw_text('Kot i mysz', 40, self.kimx,self.kimy, self.gra.PURPLE)
            self.gra.draw_text('Wyjscie', 40, self.exitx,self.exity, self.gra.PURPLE)
            self.draw_cursor()
            self.blit_screen()
# ruch kursora po menu            
    def move_cursor(self):
        if self.gra.DOWN_KEY:
            if self.state == 'Snake':
                self.cursor_rect.midtop= (self.kikx + self.offset, self. kiky)
                self.state = 'Kolko i krzyzyk'
            elif self.state == 'Kolko i krzyzyk':
                self.cursor_rect.midtop= (self.warcabyx + self.offset, self. warcabyy)
                self.state = 'Warcaby'
            elif self.state == 'Warcaby':
                self.cursor_rect.midtop= (self.kimx + self.offset, self. kimy)
                self.state = 'Kot i mysz'
            elif self.state == 'Kot i mysz':
                self.cursor_rect.midtop= (self.exitx + self.offset, self. exity)
                self.state = 'Wyjscie'
            elif self.state == 'Wyjscie':
                self.cursor_rect.midtop= (self.snakex + self.offset, self. snakey)
                self.state = 'Snake'
        
        elif self.gra.UP_KEY:
            if self.state == 'Snake':
                self.cursor_rect.midtop= (self.exitx + self.offset, self. exity)
                self.state = 'Wyjscie'
            elif self.state == 'Kolko i krzyzyk':
                self.cursor_rect.midtop= (self.snakex + self.offset, self. snakey)
                self.state = 'Snake'
            elif self.state == 'Warcaby':
                self.cursor_rect.midtop= (self.kikx + self.offset, self. kiky)
                self.state = 'Kolko i krzyzyk'
            elif self.state == 'Kot i mysz':
                self.cursor_rect.midtop= (self.warcabyx + self.offset, self. warcabyy)
                self.state = 'Warcaby'
            elif self.state == 'Wyjscie':
                self.cursor_rect.midtop= (self.kimx + self.offset, self. kimy)
                self.state = 'Kot i mysz'
# wcisniecie klawisza enter powoduje wybranie gry             
    def check_input(self):
        self.move_cursor()
        if self.gra.START_KEY:
            if self.state == 'Snake':
                self.gra.snake_playing = True
            elif self.state == 'Kolko i krzyzyk':
                self.gra.kik_playing = True
            elif self.state == 'Warcaby':
                self.gra.curr_menu = self.gra.tworcy
            elif self.state == 'Kot i mysz':
                self.gra.kim_playing = True
            elif self.state == 'Wyjscie':
                pygame.quit()
            self.run_display = False

class Tworcy(Menu):
    def __init__(self,gra):
        Menu.__init__(self, gra)
        self.t1x, self.t1y = 50, 200
        self.t2x, self.t2y = self.t1x, self.t1y + 40
        self.t3x, self.t3y = self.t1x, self.t1y + 80
        self.t4x, self.t4y = self.t1x, self.t1y + 120
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.gra.check_events()
            self.check_input()
            bg = pygame.image.load('bg1.jpg').convert()
            self.gra.display.blit(bg, (0,0))
            self.gra.draw_text('Dominik Buchholz', 40, self.t1x, self.t1y, self.gra.PURPLE)
            self.gra.draw_text('Piotr Gieraltowski', 40, self.t2x,self.t2y, self.gra.PURPLE)
            self.gra.draw_text('Julia Urbanek', 40, self.t3x,self.t3y, self.gra.PURPLE)
            self.gra.draw_text('Andrzej Palski', 40, self.t4x,self.t4y, self.gra.PURPLE)
            self.blit_screen()
 
    def check_input(self):
        if self.gra.START_KEY:
            self.gra.curr_menu = self.gra.mainmenu
            self.run_display = False
        
        