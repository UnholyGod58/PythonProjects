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
                



def collision(object1, object2):
    return object1.colliderect(object2)


def play():
    screen.fill((25,25,25))
    ball = pygame.Rect(X_resolution//2, Y_resolution//2, 10,10)
    wall1 = pygame.Rect(0,0,X_resolution,10)
    wall2 = pygame.Rect(0,Y_resolution-10,X_resolution,10)
    wall3 = pygame.Rect(0,0,10,Y_resolution)
    wall4 = pygame.Rect(X_resolution-10,0,10,Y_resolution)
    pygame.draw.rect(screen, (200,0,0), ball)
    pygame.draw.rect(screen, (100,0,0), wall1)
    pygame.draw.rect(screen, (100,0,0), wall2)
    pygame.draw.rect(screen, (100,0,0), wall3)
    pygame.draw.rect(screen, (100,0,0), wall4)
    
    while True:
        movex = (key_input[pygame.K_LEFT] * -speed) + (key_input[pygame.K_RIGHT] * speed)
        movey = (key_input[pygame.K_UP] * -speed) + (key_input[pygame.K_DOWN] * speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if collision(ball, wall1):
                ball.x -= movex
                ball.y -= movey
                movex, movey = 0
        ball.x += movex
        ball.y += movey        
        pygame.draw.rect(screen, (200,0,0), ball)
        pygame.display.update() 
        fpsClock.tick(fps)
        input()

display_menu()

pygame.quit()
quit()