import pygame
import math

def swapTurn(currentTurn):
    if(currentTurn==0):
        currentTurn=1
    elif(currentTurn==1):
        currentTurn=0
    return currentTurn


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


class bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'bullet'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
    def collides(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def rotate(self, angle, x, y):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()


class gun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'gun'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('gun.png')
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
    def revive(self):
        self.image = pygame.image.load('man.png')
        self.isDead = False
        
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


class againButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'againbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('againButton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('againButtonOver.png')
    def unhighlight(self):
        self.image = pygame.image.load('againButton.png')


class menuButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'menubtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('menuButton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('menuButtonOver.png')
    def unhighlight(self):
        self.image = pygame.image.load('menuButton.png')



   
#class powerButton(pygame.sprite.Sprite):
    #def __init__(self):
    #    pygame.sprite.Sprite.__init__(self)
   #     self.id = 'Pwrbtn'
    #    self.x = 0
   #     self.y = 0
   #     self.image = pygame.image.load('powerup.png')
    #    self.rect = self.image.get_rect()
  #  def draw(self, screen):
     #   screen.blit(self.image, self.rect)
  #  def highlight(self):
  #      self.image = pygame.image.load('powerover.png')
 #  def unhighlight(self):
   #     self.image = pygame.image.load('powerup.png')


class extraButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'Extbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('extra.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('extraover.png')
    def unhighlight(self):
        self.image = pygame.image.load('extra.png')


class chillButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'Chillbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('chill.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('chillover.png')
    def unhighlight(self):
        self.image = pygame.image.load('chill.png')

class gunButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'Gunbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('gunbutton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('gunbuttonover.png')
    def unhighlight(self):
        self.image = pygame.image.load('gunbutton.png')

    
def mainMenu():
    
    leaveMenu = False
    playButton = button()
    playButton.rect.x = 600
    playButton.rect.y = 300
    isInButton = False
    while (leaveMenu == False):
        for event in pygame.event.get():
            if event.type == firstOver:
                pygame.mixer.music.load('loopsong.ogg')
                pygame.mixer.music.play(-1)
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
    


def gameOver():

    pygame.mixer.music.stop()
    
    leaveMenu = False
    againBut = againButton()
    againBut.rect.x = 400
    againBut.rect.y = 300
    menuBut = menuButton()
    menuBut.rect.x = 800
    menuBut.rect.y = 300
    isInButton = False
    isInMenu = False
    while (leaveMenu == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clicked = pygame.mouse.get_pressed()
        screen.fill(white);
        font = pygame.font.Font('freesansbold.ttf', 100)
        screen.blit(font.render(str("GAME OVER"), True, (0,0,0)), (0,0))
        mouse = pygame.mouse.get_pos()
        if againBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                leaveMenu=True
                firstOver = pygame.USEREVENT + 1
                snowFall = pygame.mixer.Sound("snowfall.wav")
                snowThrow = pygame.mixer.Sound("throw.wav")
                pygame.mixer.music.set_endevent(firstOver)
                pygame.mixer.music.load('firstsong.ogg')
                pygame.mixer.music.set_volume(0.15)
                pygame.mixer.music.play()
            if(not isInButton): 
               againBut.highlight()
               isInButton = True
        if not(againBut.rect.collidepoint(mouse)):
            if(isInButton):    
               againBut.unhighlight()
               isInButton = False

        if menuBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                firstOver = pygame.USEREVENT + 1
                snowFall = pygame.mixer.Sound("snowfall.wav")
                snowThrow = pygame.mixer.Sound("throw.wav")
                pygame.mixer.music.set_endevent(firstOver)
                pygame.mixer.music.load('firstsong.ogg')
                pygame.mixer.music.set_volume(0.15)
                pygame.mixer.music.play()
                mainMenu()
                leaveMenu = True
                
            if(not isInMenu): 
               menuBut.highlight()
               isInMenu = True
        if not(menuBut.rect.collidepoint(mouse)):
            if(isInMenu):    
               menuBut.unhighlight()
               isInMenu = False
            
        againBut.draw(screen)
        menuBut.draw(screen)
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


##SOUND STUFF

gunActivationSound = pygame.mixer.Sound("gunactivated.wav")
gunShot = pygame.mixer.Sound("gunshot.wav")
gameEnd = pygame.mixer.Sound("gameend.wav")
snowFall = pygame.mixer.Sound("snowfall.wav")
ballBounce = pygame.mixer.Sound("ballbounce.wav")
bulletBounce = pygame.mixer.Sound("bulletbounce.wav")
snowThrow = pygame.mixer.Sound("throw.wav")
presentSound = pygame.mixer.Sound("present.wav")

firstOver = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(firstOver)
pygame.mixer.music.load('firstsong.ogg')
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play()
###

shadowImg = pygame.image.load('shadow.png')
clock = pygame.time.Clock()
pygame.display.set_caption(gameTitle)
screen = pygame.display.set_mode((screenWidth, screenHeight))


lineAngleTimeStd = 2
lineHeightTimeStd = 2
lineSizeTimeStd = 1

scrollFps = 10
giftSpeed = 50
lineSize = 50
lineAngleTime = lineAngleTimeStd
#lineAngleTime is in seconds
lineHeightTime = lineHeightTimeStd
#lineHeightTime is in seconds
lineSizeTime = lineSizeTimeStd
#lineSizeTime is in seconds, for 1 up or down
angleBoundary = math.pi/4
heightBoundary = math.pi/3
minimumSize = 15
maximumSize = 50
#Changeable stuff

    
all_sprites_list = pygame.sprite.Group()
snowList = pygame.sprite.Group()
fabricList = pygame.sprite.Group()
powerList = pygame.sprite.Group()
chillList = pygame.sprite.Group()
gunButList = pygame.sprite.Group()
bullList = pygame.sprite.Group()
gunList = pygame.sprite.Group()

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


extraBtn = extraButton()
extraBtn.rect.x = 90
extraBtn.rect.y = 500
powerList.add(extraBtn)

chillBtn = chillButton()
chillBtn.rect.x = 180
chillBtn.rect.y = 500
chillList.add(chillBtn)

gunBtn = gunButton()
gunBtn.rect.x = 270
gunBtn.rect.y = 500
gunButList.add(gunBtn)

bull = bullet()
bull.rect.x = 0
bull.rect.y = 0
bullList.add(bull)


gunObj = gun()
gunObj.rect.x = 0
gunObj.rect.y = 0
gunList.add(gunObj)



extraUp = [False, False]
extraInButton = False
extraActivated = [False, False]
chillUp = [False, False]
chillInButton = False
chillActivated = [False, False]
gunUp = [True, False]
gunInButton = False
gunActivated = [False, False]


playerDied = False
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
bouncedUp = False
bouncedDown = False
bounce = 1
selectedPlayer = 0
currentTurn = 0
#0 for first player's turn, 1 for second player
currentDirection = 1
playerChosen = False
ball = snowball()
snowList.add(ball)
posY = 0
isInButton = False
gameEnded = False

player[3].kill()
player[4].kill()

mainMenu()

while close == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == firstOver:
            pygame.mixer.music.load('loopsong.ogg')
            pygame.mixer.music.play(-1)
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
                        pygame.mixer.Sound.play(snowThrow)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(not extraBtn.rect.collidepoint(mouse)):
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
                        pygame.mixer.Sound.play(snowThrow)

    clicked = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    if(chillActivated[currentTurn]):
        lineAngleTime = 4
        lineHeightTime = 4
        lineSizeTime = 2
        chillActivated[currentTurn] = False
    
    
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
    
            if gunActivated[currentTurn]:
                gunObj.rect.x = player[selectedPlayer+currentTurn*3].rect.x
                gunObj.rect.y = player[selectedPlayer+currentTurn*3].rect.y+10
                gunList.update()
                gunList.draw(screen)
            
            if lineAngleStop == False:
                    
                if lineClock >= lineAngleTime * angleBoundary / (2*math.pi):
                    angleDirection = -1
                if lineClock <= -lineAngleTime * angleBoundary / (2*math.pi):
                    angleDirection = 1
                        
                    
                lineClock += angleDirection/(fps*lineAngleTime)

            angle = lineClock*2*math.pi/lineAngleTime + math.pi/2
            if currentDirection == -1:
                angle += math.pi
            if (lineAngleStop == True) and (gunActivated[currentTurn]):
                lineSizeStop = True
                lineDoneStop = True
                ballX = player[selectedPlayer+currentTurn*3].rect.x+25
                ballY = player[selectedPlayer+currentTurn*3].rect.y+15
                bull.rotate(math.degrees(angle-math.pi/2), ballX, ballY)
                pygame.mixer.Sound.play(gunShot)
                
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
            if(not gunActivated[currentTurn]):
                if (height > 0):
                    timer += 1/fps
                    height += initialHSpeed - gravity*timer
                    ballX += lineSize*math.sin(angle)*fps/1000
                    ballY += bounce*lineSize*math.cos(angle)*fps/1000
                    screen.blit(shadowImg,(ball.rect.x+height*0.01,+ball.rect.y+height*0.005))
                    ball.rect.x = ballX
                    ball.rect.y = ballY
                if (ball.rect.y > screenHeight-ball.rect.height):
                    if bouncedDown == False:
                        bounce *= -1
                        bouncedDown = True
                        bouncedUp = False
                        pygame.mixer.Sound.play(ballBounce)
                if (ball.rect.y<0):
                    if bouncedUp == False:
                        bounce *= -1
                        bouncedUp = True
                        bouncedDown = False
                        pygame.mixer.Sound.play(ballBounce)
                   
                if(height <= 0):
                    pygame.mixer.Sound.play(snowFall)
                    currentTurn = swapTurn(currentTurn)
                    currentDirection *= -1
                    for i in range(0,3):
                        if (ball.collides(gifts[i])):
                            pygame.mixer.Sound.play(presentSound)
                            if(extraUp[swapTurn(currentTurn)]):
                                chillUp[swapTurn(currentTurn)] = True
                            extraUp[swapTurn(currentTurn)] = True
                            gunUp[swapTurn(currentTurn)] = True
                        if (ball.collides(player[i+currentTurn*3])) and (not player[i+currentTurn*3].isDead):
                            player[i+currentTurn*3].kill()
                            if(player[currentTurn*3].isDead) and (player[1+currentTurn*3].isDead) and (player[2+currentTurn*3].isDead):
                                #RESET GAME
                                pygame.mixer.Sound.play(gameEnd)
                                gameOver()
                                for i in range(0,6):
                                    if(player[i].isDead):
                                        player[i].revive()
                                extraUp = [False, False]
                                extraInButton = False
                                extraActivated = [False, False]
                                chillUp = [False, False]
                                chillInButton = False
                                chillActivated = [False, False]
                                gunUp = [False, False]
                                gunInButton = False
                                gunActivated = [False, False]
                                currentTurn = 0
                                currentDirection = 1
                                ###


                                    
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
                    bouncedUp = False
                    bouncedDown = False
                    bounce = 1
                    lineSize = 50
                    playerChosen = False
                    lineAngleTime = lineAngleTimeStd
                    lineHeightTime = lineHeightTimeStd
                    lineSizeTime = lineSizeTimeStd
                    #
                    #RESET VARIABLES

                snowList.update()
                snowList.draw(screen)

            else:
                ballX += lineSize*math.sin(angle)*fps/400
                ballY += bounce*lineSize*math.cos(angle)*fps/400
                bull.rect.x = ballX
                bull.rect.y = ballY
                
                if (bull.rect.y > screenHeight-bull.rect.height):
                    if bouncedDown == False:
                        pygame.mixer.Sound.play(bulletBounce)
                        bounce *= -1
                        bouncedDown = True
                        bouncedUp = False
                        bull.reset()
                        bull.rotate(bounce*math.degrees(angle-math.pi/2), ballX, ballY)
                if (bull.rect.y<0):
                    if bouncedUp == False:
                        pygame.mixer.Sound.play(bulletBounce)
                        bounce *= -1
                        bouncedUp = True
                        bouncedDown = False
                        bull.reset()
                        bull.rotate(bounce*math.degrees(angle-math.pi/2), ballX, ballY)

                for i in range(0,3):
                        if (bull.collides(player[i+swapTurn(currentTurn)*3])) and (not player[i+swapTurn(currentTurn)*3].isDead):
                            player[i+swapTurn(currentTurn)*3].kill()
                            playerDied = True
                        if(player[swapTurn(currentTurn)*3].isDead) and (player[1+swapTurn(currentTurn)*3].isDead) and (player[2+swapTurn(currentTurn)*3].isDead):
                            print("hi")
                            pygame.mixer.Sound.play(gameEnd)
                            gameOver()
                            #RESET GAME
                            for i in range(0,6):
                                if(player[i].isDead):
                                    player[i].revive()
                            extraUp = [False, False]
                            extraInButton = False
                            extraActivated = [False, False]
                            chillUp = [False, False]
                            chillInButton = False
                            chillActivated = [False, False]
                            gunUp = [False, False]
                            gunInButton = False
                            gunActivated = [False, False]
                            currentTurn = 0
                            currentDirection = 1
                            gameEnded = True
                            ###
                            
                            
                
                
            
                if (bull.rect.x+bull.rect.width>=screenWidth) or (bull.rect.x <= 0) or (playerDied):
                    gunActivated[currentTurn] = False
                    currentTurn = swapTurn(currentTurn)
                    currentDirection *= -1
                    #RESET VARIABLES
                    #
                    playerDied = False
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
                    bouncedUp = False
                    bouncedDown = False
                    bounce = 1
                    lineSize = 50
                    playerChosen = False
                    lineAngleTime = lineAngleTimeStd
                    lineHeightTime = lineHeightTimeStd
                    lineSizeTime = lineSizeTimeStd
                    bull.reset()
                    if(gameEnded):
                        currentTurn = 0
                        currentDirection = 1
                        gameEnded = False
                    #
                    #RESET VARIABLES
                  
                gunList.update()
                gunList.draw(screen)    
                bullList.update()
                bullList.draw(screen)
                

                

                    
            if(extraActivated[swapTurn(currentTurn)]):
                currentTurn = swapTurn(currentTurn)
                currentDirection *= -1
                extraActivated[currentTurn] = False



        
                    


    
    if (extraUp[currentTurn] and (not playerChosen)):
        powerList.update()
        powerList.draw(screen)
        if extraBtn.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                extraActivated[currentTurn] = True
                extraUp[currentTurn] = False
            if(not extraInButton): 
                extraBtn.highlight()
                extraInButton = True
        if not(extraBtn.rect.collidepoint(mouse)):
            if(extraInButton):    
                extraBtn.unhighlight()
                extraInButton = False    

    if (chillUp[currentTurn] and (not playerChosen)):
        chillList.update()
        chillList.draw(screen)
        if chillBtn.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                chillActivated[currentTurn] = True
                chillUp[currentTurn] = False
            if(not chillInButton): 
                chillBtn.highlight()
                chillInButton = True
        if not(chillBtn.rect.collidepoint(mouse)):
            if(chillInButton):    
                chillBtn.unhighlight()
                chillInButton = False


    if (gunUp[currentTurn] and (not playerChosen)):
        gunButList.update()
        gunButList.draw(screen)
        if gunBtn.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                pygame.mixer.Sound.play(gunActivationSound)
                gunActivated[currentTurn] = True
                gunUp[currentTurn] = False
            if(not gunInButton): 
                gunBtn.highlight()
                gunInButton = True
        if not(gunBtn.rect.collidepoint(mouse)):
            if(gunInButton):    
                gunBtn.unhighlight()
                gunInButton = False


            
    font = pygame.font.Font('freesansbold.ttf', 20)
    if playerChosen == False:
        screen.blit(font.render(str("Select Player"), True, (0,0,0)), (0,0))
 
    pygame.display.update()
        
pygame.quit()

    






