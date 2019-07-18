


import os, sys
import pygame
from pygame.locals import *

sys.path.append ("../")
import parallax

pygame.init()
screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)
pygame.display.set_caption('Parallax-test')
pygame.mouse.set_visible(0)

orientation = 'vertical'


bg = parallax.ParallaxSurface((640, 480), pygame.RLEACCEL)
bg.add('p2.png', 5)
bg.add('p3.png', 2)
bg.add('p1.png', 1)

run = True
speed = 0
t_ref = 0
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN and event.key == K_RIGHT:
            speed += 10
        if event.type == KEYUP and event.key == K_RIGHT:
            speed -= 10
        if event.type == KEYDOWN and event.key == K_LEFT:
            speed -= 10
        if event.type == KEYUP and event.key == K_LEFT:
            speed += 10
        if event.type == KEYDOWN and event.key == K_UP:
            orientation = 'vertical'
        if event.type == KEYDOWN and event.key == K_DOWN:
            orientation = 'horizontal'
        
    bg.scroll(speed, orientation)
    t = pygame.time.get_ticks()
    if (t - t_ref) > 60:
        bg.draw(screen)
        pygame.display.flip()

