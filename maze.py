#josh is nor girlbossing 
#Maze

import pygame, sys
pygame.init()

fps = 60
fpsClock = pygame.time.Clock()
X_resolution = 1000
Y_resolution = 800
speed = 10

screen = pygame.display.set_mode((X_resolution, Y_resolution))
pygame.display.set_caption("Da Maze")

key_input = pygame.key.get_pressed()

def display_text(scale, print, x, y):
    text = pygame.font.Font(None, scale).render(print, True, (255,255,255))
    screen.blit(text, ((x - text.get_width()//2), y - text.get_height()//2))
    return text

def display_menu():
    screen.fill((25,25,25))
    display_text(150, "Da Maze", (X_resolution//2), (Y_resolution//4))
    i = display_text(75, "Play", (X_resolution//2), (Y_resolution//2))
    rect_play = i.get_rect()
    rect_play.center = ((X_resolution//2), (Y_resolution//2))
    i = display_text(75, "Exit", (X_resolution//2), (Y_resolution//1.5))
    rect_exit = i.get_rect()
    rect_exit.center = ((X_resolution//2), (Y_resolution//1.5))
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_play.collidepoint(event.pos):
                    play()
                    break
                if rect_exit.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                
class wall(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,wallColor):
        super().__init__()

def collision(object1, object2):
    return object1.colliderect(object2)


def play():
    screen.fill((25,25,25))
    ball = pygame.sprite.Sprite
    while True:
        movex = (key_input[pygame.K_LEFT] * -speed) + (key_input[pygame.K_RIGHT] * speed)
        movey = (key_input[pygame.K_UP] * -speed) + (key_input[pygame.K_DOWN] * speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if collision(ball):
                ball.x -= movex
                ball.y -= movey
                movex, movey = 0
        ball.x += movex
        ball.y += movey        
        pygame.display.update() 
        fpsClock.tick(fps)

display_menu()

pygame.quit()
quit()