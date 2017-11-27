import pygame
import math

def main():

    run()

def run():
    
    
    screenWidth = 1200
    screenHeight = 600
    gameTitle = "Snowball Fight"
    white = (255,255,255)
    black = (0, 0, 0)
    close = False
    fps = 30


    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption(gameTitle)
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    ballImg = pygame.image.load('snowball.png')
    shadowImg = pygame.image.load('shadow.png')
    x = 600
    y = 300
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
    
    player = man()
    player.rect.x = 600
    player.rect.y = 300
    all_sprites_list.add(player)
    enemy = man()
    enemy.rect.x = 700
    enemy.rect.y = 300
    all_sprites_list.add(enemy)

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
    

    while close == False:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                close = True;
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if lineAngleStop == False:
                        lineAngleStop = True
                    elif lineSizeStop == False:
                        lineSizeStop = True
                    elif lineDoneStop == False:
                        lineDoneStop = True
                        initialHSpeed = lineSize*-math.cos(heightAngle)/2
                        ball = snowball()
                        ballX = 625
                        ballY = 315
                        all_sprites_list.add(ball)
        clock.tick(fps)
        screen.fill(white)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        
        if lineDoneStop == False:
            if lineAngleStop == False:
                
                if lineClock >= lineAngleTime * angleBoundary / (2*math.pi):
                    angleDirection = -1
                if lineClock <= -lineAngleTime * angleBoundary / (2*math.pi):
                    angleDirection = 1
                    
                
                lineClock += angleDirection/(fps*lineAngleTime)

            angle = lineClock*2*math.pi/lineAngleTime + math.pi/2
            
            if (lineAngleStop == True) & (lineSizeStop == False):
                if lineSize < minimumSize:
                    sizeDirection = 1
                if lineSize > maximumSize:
                    sizeDirection = -1
                lineSize += sizeDirection*(maximumSize-minimumSize)/(fps*lineSizeTime)

            if (lineAngleStop == True) & (lineSizeStop == True):
                if heightLineClock >= lineHeightTime * heightBoundary / (2*math.pi):
                    heightDirection = -1
                if heightLineClock <= -heightDirection/(fps*lineAngleTime):
                    heightDirection= 1
                
                heightLineClock += heightDirection/(fps*lineAngleTime)
                heightAngle = heightLineClock*2*math.pi/lineHeightTime + angle
                yAngleLine = lineSize * math.cos(heightAngle)
                xAngleLine = lineSize * math.sin(heightAngle)
                pygame.draw.line(screen, black, (x+25, y+15), (xAngleLine + x + 25, yAngleLine + y + 15), 1)
            yLine = lineSize * math.cos(angle)
            xLine = lineSize * math.sin(angle)
            pygame.draw.line(screen, black, (x+25, y+15), (xLine + x + 25, yLine + y + 15), 3)
            #LINE PROCESSS
            #
            #
        else:
            if (height > 0):
                timer += 1/fps
                height += initialHSpeed - gravity*timer
                ballX += lineSize*math.sin(angle)*timer/100
                ballY += lineSize*math.cos(angle)*timer/100
                font = pygame.font.Font('freesansbold.ttf', 20)
                screen.blit(font.render(str(ballX), True, (0,0,0)), (0,0))
                screen.blit(shadowImg,(ball.rect.x+height*0.01,+ball.rect.y+height*0.005))
                ball.rect.x = ballX
                ball.rect.y = ballY
            elif ball.collides(enemy):
                pygame.quit()
        
        pygame.display.update()
        
    pygame.quit()

    


class snowball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 0
        self.y = 0
        self.image = pygame.image.load('snowball.png')
        self.rect = self.image.get_rect()
    def collides(self, sprite):
        return self.rect.colliderect(sprite.rect)


    
class man(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = 0
        self.y = 0
        self.image = pygame.image.load('man.png')
        self.rect = self.image.get_rect()
        
main()
