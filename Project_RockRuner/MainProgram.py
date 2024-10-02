import pygame
import random


pygame.init()
interface = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("RockRunner")

# ....Character and Object Image .......
walkright = [pygame.image.load('run1.PNG'), pygame.image.load('run2.PNG'), pygame.image.load('run3.PNG'),
             pygame.image.load('run4.PNG'), pygame.image.load('run5.PNG')]
walkleft = [pygame.image.load('run1l.PNG'), pygame.image.load('run2l.PNG'), pygame.image.load('run3l.PNG'),
            pygame.image.load('run4l.PNG'), pygame.image.load('run5l.PNG')]
characterjump = [pygame.image.load('jump1.PNG'), pygame.image.load('jump2.PNG'), pygame.image.load('jump3.PNG'),
                 pygame.image.load('jump4.PNG')]
character = [pygame.image.load('Stand.PNG'), pygame.image.load('Stand2.PNG'), pygame.image.load('Stand3.PNG'),
             pygame.image.load('Stand4.PNG'), pygame.image.load('Stand5.PNG'), pygame.image.load('Stand6.PNG'),
             pygame.image.load('Stand7.PNG')]
Bg = pygame.image.load('Background.PNG')

# ....  Time .......
time = pygame.time.Clock()


#....Character......
class Player(object):
    def __init__(self, x, y, width, height, stand):
        self.x = x
        self.y = y
        self.vel = 5
        self.width = width
        self.height = height
        self.isJump = False
        self.jumpcount = 10
        self.Left = False
        self.Right = False
        self.walkcount = 0
        self.stand = stand


    def Keywalk(self, interface):
        if self.walkcount + 1 > 27:
            self.walkcount = 0
        if self.Left:
            interface.blit(walkleft[self.walkcount // 7], (self.x, self.y))
            self.walkcount += 1
        elif self.Right:
            interface.blit(walkright[self.walkcount // 7], (self.x, self.y))
            self.walkcount += 1
        elif self.isJump:
            interface.blit(characterjump[self.stand // 13], (self.x, self.y))
        else:
            interface.blit(character[self.stand // 19], (self.x, self.y))


#...Tree Object .........
class Tree(object):
    GoRight = pygame.image.load('Tree.PNG')

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.vel = 5
        self.width = width
        self.height = height
        self.GoCount  = 0
        self.come = 0
        self.end = 0
    def draw (self,interface):
        self.move()
        interface.blit(self.GoRight, (self.x,self.y))
    def move(self):
        if self.vel > 0:
            if self.x > self.end :
                self.x -= 3


#...Fire Object ..........
class Fire(object):
    Firecome = pygame.image.load('Fire.PNG')

    def __init__(self,x,y, width,height):
        self.x = x
        self.y = y
        self.vel = 5
        self.width = width
        self.height = height
        self.GoCount  = 0
        self.come = 0
        self.end = 0
    def draw (self,interface):
        self.move()
        interface.blit(self.Firecome, (self.x,self.y))
    def move(self):
        if self.vel > 0:
            if self.y > self.end :
                self.y += random.randrange(1,5)


#.......MainCreate and Program and Interface ..........
def MyGameWindow():
    interface.blit(Bg, (0, 0))
    char.Keywalk(interface)
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    interface.blit(text, (450, 80))
    for i in listlist :
        i.draw(interface)
        if i.x < 0 :
            listlist.remove(i)
        if char.y - 50 < i.y  and char.x + 10  > i.x and char.x < i.x + 30 :
            import GameOver
            GameOver.main()
            pygame.quit()
    for k in listlisttree :
        k.draw(interface)
        if k.x < 0 :
            listlisttree.remove(k)
        if char.y + 20 > k.y and char.x +30 > k.x and char.x < k.x + 20 :
            import GameOver
            GameOver.main()
            pygame.quit()

    pygame.display.update()

# .....MainProgram........
char = Player(100,550,80,80,10)
count = 0
countFire = 0
listlist = []
listlisttree = []
font = pygame.font.SysFont('comicsans', 30, True)
score = 0
run = True
while run  :
    time.tick(50)
    startx = random.randrange(1, 700)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and char.x > char.vel:
        char.x -= char.vel
        char.Left = True
        char.Right = False
        char.stand = 0
    elif keys[pygame.K_d] and char.x < 1000 - char.width - char.vel:
        char.x += char.vel
        char.Left = False
        char.Right = True
        char.stand = 0
    elif keys[pygame.K_ESCAPE] :
        pygame.quit()
    else:
        char.Left = False
        char.Right = False
        char.walkcount = 0
        char.stand += 1
    if not (char.isJump):
        if keys[pygame.K_SPACE]:
            char.isJump = True
            char.Left = False
            char.Right = False
            char.walkcount = 0
            char.stand = 0
    else:
        if char.jumpcount >= -10:
            neg = 1
            if char.jumpcount < 0:
                neg = -1
            char.y -= (char.jumpcount ** 2) * 0.5 * neg
            char.jumpcount -= 1
        else:
            char.isJump = False
            char.jumpcount = 10


    char.stand += 1
    if char.stand >= 50:
        char.stand = 0

    #.....Create Tree .....
    if count % 80  == 0 :
        listlisttree.append((Tree(930,550,80,80)))

    #......Create Fire.......
    if countFire % 50 == 0  :
        listlist.append(Fire(startx, 100, 80, 80))

    count += 1
    countFire += 1
    score += 1


    MyGameWindow()


pygame.quit()
