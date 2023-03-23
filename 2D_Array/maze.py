#josh is nor girlbossing 
#Maze

import pygame
pygame.init()

X_resolution = 1000
Y_resolution = 800
screen = pygame.display.set_mode((X_resolution, Y_resolution))
pygame.display.set_caption("Da Maze")

def display_text(scale, print, x, y):
    text = pygame.font.Font(None, scale).render(print, True, (255,255,255))
    screen.blit(text, (x, y))
    return text

def display_menu():
    screen.fill((25,25,25))
    text = display_text(200, "Da Maze", (X_resolution//2 - .get_width()//2), (Y_resolution//3))
    text = display_text(100, "Play", (X_resolution//2 - .get_width()//2), (Y_resolution//2))
    rect_play = text.get_rect()
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_play.collidepoint(event.pos):
                    play()
                    break
                
def play():
    pass

display_menu()

pygame.quit()
quit()