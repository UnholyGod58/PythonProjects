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
    screen.blit(text, ((x - text.get_width()//2), y - text.get_height()//2))
    return text

def display_menu():
    screen.fill((25,25,25))
    display_text(150, "Da Maze", (X_resolution//2), (Y_resolution//4))
    i = display_text(75, "Play", (X_resolution//2), (Y_resolution//2))
    rect_play = i.get_rect()
    i = display_text(75, "Exit", (X_resolution//2), (Y_resolution//1.5))
    rect_exit = i.get_rect()
    rect_exit.center = ()
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
                    print("Mark")
                    pygame.quit()
                    exit()
                
def play():
    pass

display_menu()

pygame.quit()
quit()