import pygame
from pygame.locals import *
from warrior import player
from enemy import enemy
from game_funtions import control

pygame.init()
W, H =800,600# 1280, 720
HW, HH = W / 2, H / 2
win = pygame.display.set_mode((800,600))
stagePosX=0

pygame.display.set_caption("Berserk Game")


bg = pygame.image.load('background.png')
bgWidth, bgHeight = bg.get_rect().size
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

stageWidth = bgWidth * 2
startScrollingPosX = HW
#bulletSound = pygame.mixer.Sound('bullet.wav')
#hitSound = pygame.mixer.Sound('hit.wav')

##music = pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1)

score = 0

def redrawGameWindow():
    rel_x=stagePosX % bgWidth
    win.blit(bg, (rel_x - bgWidth, 0))
    if rel_x < W:
        win.blit(bg, (rel_x, 0))

    #win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (350, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()
    ############

##################

#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
man = player(700, 356, 64,64)
goblin = enemy(100, 356, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit(win)
                score -= 5


    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                #hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    control(man,shootLoop,bullets)
    redrawGameWindow()
    #update_screen()

pygame.quit()
