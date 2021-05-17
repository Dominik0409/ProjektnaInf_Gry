import pygame

class Menu():
    def __init__(self, gra):
        self.gra = gra
        self.mid_w, self.mid_h = self.gra.DIS_W/2, self.gra.DIS_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100
        
    def draw_cursor(self):
        self.gra.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y, self.gra.WHITE)
        
    def blit_screen(self):
        self.gra.window.blit(self.gra.display, (0,0))
        pygame.display.update()
        self.gra.reset_keys()
        
class MainMenu(Menu):
    def __init__(self,gra):
        Menu.__init__(self, gra)
        self.state = "Snake"
        self.snakex, self.snakey = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.snakex + self.offset, self.snakey)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.gra.check_events()
            self.check_input()
            self.gra.display.fill(self.gra.BLACK)
            self.gra.draw_text('Main Menu', 20, self.gra.DIS_W/2, self.gra.DIS_H/2 -20, self.gra.WHITE)
            self.gra.draw_text('Snake', 20, self.snakex,self.snakey, self.gra.WHITE)
            self.gra.draw_text('Options', 20, self.optionsx,self.optionsy, self.gra.WHITE)
            self.gra.draw_text('Credits', 20, self.creditsx,self.creditsy, self.gra.WHITE)
            self.draw_cursor()
            self.blit_screen()
            
    def move_cursor(self):
        if self.gra.DOWN_KEY:
            if self.state == 'Snake':
                self.cursor_rect.midtop= (self.optionsx + self.offset, self. optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop= (self.creditsx + self.offset, self. creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop= (self.snakex + self.offset, self. snakey)
                self.state = 'Snake'
        
        elif self.gra.UP_KEY:
            if self.state == 'Snake':
                self.cursor_rect.midtop= (self.creditsx + self.offset, self. creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop= (self.snakex + self.offset, self. snakey)
                self.state = 'Snake'
            elif self.state == 'Credits':
                self.cursor_rect.midtop= (self.optionsx + self.offset, self. optionsy)
                self.state = 'Options'
                
    def check_input(self):
        self.move_cursor()
        if self.gra.START_KEY:
            if self.state == 'Snake':
                self.gra.snake_playing = True
            elif self.state == 'Options':
                pass
            elif self.state == 'Credits':
                pass
            self.run_display = False
        
        