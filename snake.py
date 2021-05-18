import random
import pygame
from pygame.locals import *

rozmiar = 25
W, H = 1000, 1000

class Jablko():
    def __init__(self, parent_screen):
        self.jablko = pygame.image.load("zasoby\grafika\jablko.png").convert()
        self.parent_screen = parent_screen
        self.x = rozmiar * 4
        self.y = rozmiar * 4

    def rysuj(self):
        self.parent_screen.blit(self.jablko, (self.x, self.y))

    def move(self):
        self.x = random.randint(0,(W/rozmiar)-1) * rozmiar
        self.y = random.randint(0,(H/rozmiar)-1) * rozmiar

class Banan():
    def __init__(self, parent_screen):
        self.banan = pygame.image.load('b.png').convert()
        self.parent_screen = parent_screen
        self.x = rozmiar * 15
        self.y = rozmiar * 15

    def rysuj(self):
        self.parent_screen.blit(self.banan, (self.x, self.y))

    def move(self):
        self.x = random.randint(0,(W/rozmiar)-1) * rozmiar
        self.y = random.randint(0,(H/rozmiar)-1) * rozmiar




class Snake():
    def __init__(self, parent_screen, dlugosc):
        self.dlugosc = dlugosc
        self.parent_screen = parent_screen
        self.klocek = pygame.image.load("zasoby\grafika\snakeskin3.png").convert()
        self.x = [rozmiar]*dlugosc
        self.y = [rozmiar]*dlugosc
        self.kierunek = 'dol'

    def rysuj(self):
        for i in range(self.dlugosc):
            self.parent_screen.blit(self.klocek, (self.x[i], self.y[i]))

    def pow_rozmiar(self):
        self.dlugosc += 1
        self.x.append(-25)
        self.y.append(-25)

    def ruch_lewo(self):
        self.kierunek = 'lewo'

    def ruch_prawo(self):
        self.kierunek = 'prawo'

    def ruch_gora(self):
        self.kierunek = 'gora'

    def ruch_dol(self):
        self.kierunek = 'dol'

    def ruch(self):

        for i in range(self.dlugosc-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.kierunek == 'gora':
            self.y[0] -= 25
        if self.kierunek == 'dol':
            self.y[0] += 25
        if self.kierunek == 'lewo':
            self.x[0] -= 25
        if self.kierunek == 'prawo':
            self.x[0] += 25

        self.rysuj()


class Game():
    def __init__(self, gra):
        self.gra = gra
        self.FPS = 15
        pygame.init()
        pygame.mixer.init()
        self.snake = Snake(self.gra.window, 5)
        self.snake.rysuj()
        self.jablko = Jablko(self.gra.window)
        self.jablko.rysuj()
        self.banan = Banan(self.gra.window)
        self.banan.rysuj()

    def Kolizja(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + rozmiar:
            if y1 >= y2 and y1 < y2 + rozmiar:
                return True

        return False

    def dzwiek(self, sound):
        sound = pygame.mixer.Sound(f"zasoby\muzyka\{sound}.mp3")
        pygame.mixer.Sound.play(sound)
        
    def render_bg(self):
        bg = pygame.image.load("bg3.jpg")
        self.gra.window.blit(bg, (0,0))

    def play(self):
        self.render_bg()
        self.snake.ruch()
        self.jablko.rysuj()
        self.banan.rysuj()
        self.Wynik()
        self.Predkosc()

        if self.Kolizja(self.snake.x[0],self.snake.y[0],self.jablko.x,self.jablko.y):
            self.dzwiek("am")
            self.snake.pow_rozmiar()
            self.jablko.move()
            
        if self.Kolizja(self.snake.x[0],self.snake.y[0],self.banan.x,self.banan.y):
            self.dzwiek("am")
            for i in range (0,3):
                self.snake.pow_rozmiar()
            self.banan.move()
            self.FPS += 1
       
        for i in range(3,self.snake.dlugosc):
            if self.Kolizja(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                self.dzwiek("stuk")
                raise "Game over"
        
        if not (0 <= self.snake.x[0] <= W and 0 <= self.snake.y[0] <= H):
            self.dzwiek("stuk")
            raise "Game over"

    def Wynik(self):
        self.gra.draw_text(f"Wynik {self.snake.dlugosc-5}", 30, 650, 10, self.gra.WHITE)
        pygame.display.flip()
        
    def Predkosc(self):
        self.gra.draw_text(f"Predkosc {self.FPS}", 30, 650, 50, self.gra.WHITE)
        pygame.display.flip()

    def gameover(self):
        self.gra.window.blit(pygame.image.load("bg4.jpg"), (0,0))
        self.gra.draw_text(f"Koniec gry         Wynik {self.snake.dlugosc}", 30, 200, self.gra.DIS_H/2, self.gra.WHITE)
        self.gra.draw_text(f"Aby zagrac jeszcze raz kliknij Enter",  30, 20, self.gra.DIS_H/2 + 50, self.gra.WHITE)
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.gra.window, 5)
        self.jablko = Jablko(self.gra.window)
        self.banan = Banan(self.gra.window)
        self.FPS = 15


    def run(self):
        
        clock = pygame.time.Clock()
        running = True
        pause = False

        while running:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        self.gra.snake_playing = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_UP and self.snake.kierunek != 'dol':
                            self.snake.ruch_gora()
                        if event.key == K_DOWN and self.snake.kierunek != 'gora':
                            self.snake.ruch_dol()
                        if event.key == K_LEFT and self.snake.kierunek != 'prawo':
                            self.snake.ruch_lewo()
                        if event.key == K_RIGHT and self.snake.kierunek != 'lewo':
                            self.snake.ruch_prawo()

                elif event.type == QUIT:
                    running = False
                    self.gra.snake_playing = False
            try:
                if not pause:
                    self.play()
            except Exception:
                self.gameover()
                pause = True
                self.reset()



# if __name__ == "__main__":
#     game = Game()
#     game.run()
