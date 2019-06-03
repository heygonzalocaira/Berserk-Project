import pygame 

pygame.init() 

win  = pygame.display.set_mode((500,500))

pygame.display.set_caption("Berserk Game Prototype")

pos_x = 50 
pos_y = 350
width = 40
height = 60
vel = 25
isJump = False
jumpCount = 10

gameBool = True

while gameBool:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameBool = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pos_x > vel:  #prevent it from leaving the screen
        pos_x -= vel
    if key[pygame.K_RIGHT] and x < 500 - width -vel: #prevent it from leaving the screen
        pos_x += vel
    if not isJump:
        if key[pygame.K_UP] and y > vel:
            pos_y -= vel
        if key[pygame.K_DOWN] and y <500 - height -vel:
            pos_y += vel
        if key[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg =1
            if jumpCount < 0:
                neg = -1
            pos_y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    win.fill((0,0,0))
    pygame.draw.rect(win,(255, 0, 0),(pos_x,pos_y,width,height))
    pygame.display.update()

pygame.quit
 