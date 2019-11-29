import pygame

walkRight = [pygame.image.load('images/warrior_f9.png'),
             pygame.image.load('images/warrior_f10.png'),
             pygame.image.load('images/warrior_f11.png'),
             pygame.image.load('images/warrior_f12.png'),
             pygame.image.load('images/warrior_f9.png'),
             pygame.image.load('images/warrior_f10.png'),
             pygame.image.load('images/warrior_f11.png'),
             pygame.image.load('images/warrior_f12.png'),
             pygame.image.load('images/warrior_f9.png')]
walkLeft = [pygame.image.load('images/WL1.png'),
            pygame.image.load('images/WL1.png'),
            pygame.image.load('images/WL2.png'),
            pygame.image.load('images/WL3.png'),
            pygame.image.load('images/WL4.png'),
            pygame.image.load('images/WL1.png'),
            pygame.image.load('images/WL2.png'),
            pygame.image.load('images/WL3.png'),
            pygame.image.load('images/WL4.png')]

walkLeft = [pygame.image.load('images/WL1.png'),
            pygame.image.load('images/WL1.png'),
            pygame.image.load('images/WL2.png'),
            pygame.image.load('images/WL3.png'),
            pygame.image.load('images/WL4.png'),
            pygame.image.load('images/WL1.png'),
            pygame.image.load('images/WL2.png'),
            pygame.image.load('images/WL3.png'),
            pygame.image.load('images/WL4.png')]

attack_a = [pygame.image.load('images/warrior_f5.png'),
            pygame.image.load('images/warrior_f6.png'),
            pygame.image.load('images/warrior_f7.png'),
            pygame.image.load('images/warrior_f8.png'),
            pygame.image.load('images/warrior_f5.png'),
            pygame.image.load('images/warrior_f6.png'),
            pygame.image.load('images/warrior_f7.png'),
            pygame.image.load('images/warrior_f8.png'),
            pygame.image.load('images/warrior_f8.png')]

static_a = [pygame.image.load('images/warrior_mode1.png'),
            pygame.image.load('images/warrior_mode2.png'),
            pygame.image.load('images/warrior_mode3.png'),
            pygame.image.load('images/warrior_mode4.png'),
            pygame.image.load('images/warrior_mode1.png'),
            pygame.image.load('images/warrior_mode2.png'),
            pygame.image.load('images/warrior_mode3.png'),
            pygame.image.load('images/warrior_mode4.png'),
            pygame.image.load('images/warrior_mode4.png')]

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.attack = False
        self.static = False
        self.staticCount = 0
        self.walkCount = 0
        self.attackCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.attackCount + 1 >= 27:
            self.attackCount = 0
        if self.staticCount + 1 >= 27:
            self.staticCount = 0
        if self.attack:
            win.blit(attack_a[self.attackCount//3], (self.x,self.y))
            self.attackCount += 1
        if self.static:
            win.blit(static_a[self.staticCount//3], (self.x,self.y))
            self.staticCount += 1
        if not(self.standing):

            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.static:
                print("static")
            elif self.attack == False:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self,win):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 356
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
