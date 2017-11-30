import pygame
import math


class scroller(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'scroller'
        self.x = 0
        self.y = 0
        self.animationPos = 1
        self.image = pygame.image.load('scroll1.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def animate(self):
        if self.animationPos == 3:
            self.animationPos = 1
        else:
            self.animationPos += 1
        self.image = pygame.image.load('scroll' + str(self.animationPos) + '.png')    


class snowball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'sb'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('snowball.png')
        self.rect = self.image.get_rect()
    def collides(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class fabric(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'fabric'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('fabric.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class gift(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'gift'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('gift.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def updatePos(self,x,y):
        self.x = x
        self.y = y

    
class man(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'man'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('man.png')
        self.rect = self.image.get_rect()
        self.isDead = False
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def kill(self):
        self.image = pygame.image.load('dead.png')
        self.isDead = True
        
class button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'btn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('play.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('mouseplay.png')
    def unhighlight(self):
        self.image = pygame.image.load('play.png')



    
def mainMenu():

    leaveMenu = False
    playButton = button()
    playButton.rect.x = 600
    playButton.rect.y = 300
    isInButton = False
    while (leaveMenu == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clicked = pygame.mouse.get_pressed()
        screen.fill(white);
        font = pygame.font.Font('freesansbold.ttf', 100)
        screen.blit(font.render(str("SNOWBALL FIGHT"), True, (0,0,0)), (0,0))
        mouse = pygame.mouse.get_pos()
        if playButton.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                leaveMenu=True
            if(not isInButton): 
               playButton.highlight()
               isInButton = True
        if not(playButton.rect.collidepoint(mouse)):
            if(isInButton):    
               playButton.unhighlight()
               isInButton = False
            
        playButton.draw(screen)
        pygame.display.update()
        clock.tick(fps)
    


screenWidth = 1200
screenHeight = 600
gameTitle = "Snowball Fight"
white = (255,255,255)
black = (0, 0, 0)
green = (20, 200, 20)
close = False
fps = 30

pygame.init()
shadowImg = pygame.image.load('shadow.png')
clock = pygame.time.Clock()
pygame.display.set_caption(gameTitle)
screen = pygame.display.set_mode((screenWidth, screenHeight))



scrollFps = 10
giftSpeed = 50
lineSize = 50
lineAngleTime = 2
#lineAngleTime is in seconds
lineHeightTime = 2
#lineHeightTime is in seconds
lineSizeTime = 1
#lineSizeTime is in seconds, for 1 up or down
angleBoundary = math.pi/4
heightBoundary = math.pi/3
minimumSize = 15
maximumSize = 50
#Changeable stuff

    
all_sprites_list = pygame.sprite.Group()
snowList = pygame.sprite.Group()
fabricList = pygame.sprite.Group()

player = [man() for i in range(6)]
player[0].rect.x = 600
player[0].rect.y = 300
all_sprites_list.add(player[0])
player[1].rect.x = 600
player[1].rect.y = 500
all_sprites_list.add(player[1])
player[2].rect.x = 600
player[2].rect.y = 100
all_sprites_list.add(player[2])
player[3].rect.x = 900
player[3].rect.y = 300
all_sprites_list.add(player[3])
player[4].rect.x = 900
player[4].rect.y = 500
all_sprites_list.add(player[4])
player[5].rect.x = 900
player[5].rect.y = 100
all_sprites_list.add(player[5])
scroll = scroller()
scroll.rect.x = 750
scroll.rect.y = 0
all_sprites_list.add(scroll)
fabr = fabric()
fabr.rect.x = 750
fabr.rect.y = 0
fabricList.add(fabr)
gifts = [gift() for i in range(3)]
gifts[0].rect.x = 750
gifts[0].rect.y = 500
all_sprites_list.add(gifts[0])
gifts[1].rect.x = 750
gifts[1].rect.y = 300
all_sprites_list.add(gifts[1])
gifts[2].rect.x = 750
gifts[2].rect.y = 100
all_sprites_list.add(gifts[2])

scrollCounter = 0
lineClock = 0
heightLineClock = 0
angleDirection = 1
sizeDirection = -1
heightDirection = 1
yLine = 0
xLine = 50
#Starting Position
lineAngleStop = False
lineSizeStop =  False
lineDoneStop = False
heightAngle = 0
height = 0.5
gravity = 4
timer = 0
weird = False
bounce = 1
selectedPlayer = 0
currentTurn = 0
#0 for first player's turn, 1 for second player
currentDirection = 1
playerChosen = False
ball = snowball()
snowList.add(ball)
posY = 0

mainMenu()

while close == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playerChosen == True:
                    if lineAngleStop == False:
                        lineAngleStop = True
                    elif lineSizeStop == False:
                        lineSizeStop = True
                    elif lineDoneStop == False:
                        lineDoneStop = True
                        initialHSpeed = abs(lineSize*math.cos(heightAngle-angle)/2)
                        ballX = player[selectedPlayer+currentTurn*3].rect.x + 25
                        ballY = player[selectedPlayer+currentTurn*3].rect.y + 15
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playerChosen == True:
                if lineAngleStop == False:
                    lineAngleStop = True
                elif lineSizeStop == False:
                    lineSizeStop = True
                elif lineDoneStop == False:
                    lineDoneStop = True
                    initialHSpeed = abs(lineSize*math.cos(heightAngle-angle)/2)
                    ballX = player[selectedPlayer+currentTurn*3].rect.x + 25
                    ballY = player[selectedPlayer+currentTurn*3].rect.y + 15

    scrollCounter += 1
    for i in range(0,3):
        gifts[i].rect.y += giftSpeed/fps
        if gifts[i].rect.y > (600):
            gifts[i].rect.y -= screenHeight
        
    if(scrollCounter >= fps/scrollFps):
        scrollCounter = 0
        scroll.animate()       
    clock.tick(fps)
    screen.fill(white)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    fabricList.update()
    fabricList.draw(screen)
    
    if playerChosen == False:
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        for i in range(0,3):
          if player[i+currentTurn*3].rect.collidepoint(mouse):
              if(click[0] == 1) and (not player[i+currentTurn*3].isDead):
                selectedPlayer = i
                playerChosen = True
    else:      
            
        if lineDoneStop == False:
            if lineAngleStop == False:
                    
                if lineClock >= lineAngleTime * angleBoundary / (2*math.pi):
                    angleDirection = -1
                if lineClock <= -lineAngleTime * angleBoundary / (2*math.pi):
                    angleDirection = 1
                        
                    
                lineClock += angleDirection/(fps*lineAngleTime)

            angle = lineClock*2*math.pi/lineAngleTime + math.pi/2
            if currentDirection == -1:
                angle += math.pi
             
            if (lineAngleStop == True) and (lineSizeStop == False):
                if lineSize < minimumSize:
                    sizeDirection = 1
                if lineSize > maximumSize:
                    sizeDirection = -1
                lineSize += sizeDirection*(maximumSize-minimumSize)/(fps*lineSizeTime)

            if (lineAngleStop == True) and (lineSizeStop == True):
                if heightLineClock >= lineHeightTime * heightBoundary / (2*math.pi):
                    heightDirection = -1
                if heightLineClock <= -heightDirection/(fps*lineAngleTime):
                    heightDirection= 1
                    
                heightLineClock += heightDirection/(fps*lineAngleTime)
                heightAngle = heightLineClock*2*math.pi/lineHeightTime + angle
                if currentDirection == -1:
                    heightAngle -= heightBoundary
                yAngleLine = lineSize * math.cos(heightAngle)
                xAngleLine = lineSize * math.sin(heightAngle)
                pygame.draw.line(screen, black, (player[selectedPlayer+currentTurn*3].rect.x+25, player[selectedPlayer+currentTurn*3].rect.y+15), (xAngleLine + player[selectedPlayer+currentTurn*3].rect.x + 25, yAngleLine + player[selectedPlayer+currentTurn*3].rect.y + 15), 1)
            yLine = lineSize * math.cos(angle)
            xLine = lineSize * math.sin(angle)
            pygame.draw.line(screen, black, (player[selectedPlayer+currentTurn*3].rect.x+25, player[selectedPlayer+currentTurn*3].rect.y+15), (xLine + player[selectedPlayer+currentTurn*3].rect.x + 25, yLine + player[selectedPlayer+currentTurn*3].rect.y + 15), 3)
            #LINE PROCESSS
            #
            #
        else:
            if (height > 0):
                timer += 1/fps
                height += initialHSpeed - gravity*timer
                ballX += lineSize*math.sin(angle)*fps/1000
                ballY += bounce*lineSize*math.cos(angle)*fps/1000
                screen.blit(shadowImg,(ball.rect.x+height*0.01,+ball.rect.y+height*0.005))
                ball.rect.x = ballX
                ball.rect.y = ballY
            if (ball.rect.y > screenHeight-12) or (ball.rect.y<0):
                if weird == False:
                    bounce *= -1
                    print('hi')
                weird = True
            if(height <= 0):
                if(currentTurn==0):
                    currentTurn=1
                    currentDirection= -1
                elif(currentTurn==1):
                    currentTurn=0
                    currentDirection= 1
                for i in range(0,3):
                    if (ball.collides(player[i+currentTurn*3])) and (not player[i+currentTurn*3].isDead):
                        player[i+currentTurn*3].kill()
                #RESET VARIABLES
                #
                lineDoneStop=False
                lineAngleStop = False
                lineSizeStop =  False
                heightAngle = 0
                height = 0.5
                lineClock = 0
                heightLineClock = 0
                angleDirection = 1
                sizeDirection = -1
                heightDirection = 1
                yLine = 0
                xLine = 50
                timer = 0
                weird = False
                bounce = 1
                lineSize = 50
                playerChosen = False
                #
                #RESET VARIABLES
            snowList.update()
            snowList.draw(screen)
        
    font = pygame.font.Font('freesansbold.ttf', 20)
    if playerChosen == False:
        screen.blit(font.render(str("Select player"), True, (0,0,0)), (0,0))    
    pygame.display.update()
        
pygame.quit()

    






