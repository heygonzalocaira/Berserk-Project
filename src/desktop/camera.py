import pygame, sys 
from pygame.locals import * 

pygame.init()
size = width, height = 800,600
screen = pygame.display.set_mode(size)
r = 0
bif = pygame.image.load("image/background.png") 
pygame.display.set_caption("Pygame 2D RPG !")
x,y=0,0
movex, movey=0,0
character="image/warrior.png"
player=pygame.image.load(character).convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_a:
                movex=-10
            elif event.key==K_d:
                movex=+10
            elif event.key==K_w:
                movey=-10
            elif event.key==K_s:
                movey=+10
        if event.type==KEYUP:        
            if event.key==K_a:
                movex=0
            elif event.key==K_d:
                movex=0
            elif event.key==K_w:
                movey=0
            elif event.key==K_s:
                movey=0    

        x+=movex
        y+=movey    
        
        screen.fill((r,0,0))
        screen.blit(bif,(0,0))
        screen.blit(player,(x,y))
        pygame.display.flip()