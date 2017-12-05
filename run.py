import pygame
import math
import random

def swapTurn(currentTurn):
    if(currentTurn==0):
        currentTurn=1
    elif(currentTurn==1):
        currentTurn=0
    return currentTurn


def randomItem(extraUpPlayer,chillUpPlayer,gunUpPlayer, potionUpPlayer):

    listOfItems = [False, False, False, False]
    listOfItems[0] = extraUpPlayer
    listOfItems[1] = chillUpPlayer
    listOfItems[2] = gunUpPlayer
    listOfItems[3] = potionUpPlayer

    currentCount = 0
    obtainedItem = 0
    possibleBonuses = 0

    for i in range(0,4):
        if(not listOfItems[i]):
            possibleBonuses+=1

    if possibleBonuses==0:
        return -1
    
    randomNumber = random.randint(1,possibleBonuses)
    
    for i in range(0,4):
        if(not listOfItems[i]):
            currentCount+=1
        if(currentCount==randomNumber):
            return i

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



class cantTouchThis(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'sb'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('cantTouch.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def hammertime(self):
        self.image = pygame.image.load('hammertime.png')

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
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def reset(self):
        self.image = pygame.image.load('gun.png')
    def swap(self):
        self.image = pygame.image.load('gun.png')
        self.image = pygame.transform.flip(self.image,True,False)
        


class powerBar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'pwbar'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('powerbar.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def rotate(self, angle, x, y):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def flip(self, y):
        self.image = pygame.transform.flip(self.image,False,True)
        self.rect.y = y
    def scale(self, width,height):
        self.image = pygame.transform.scale(self.image, (round(width), round(height)))
    def reset(self):
        self.image = pygame.image.load('powerbar.png')
        self.rect = self.image.get_rect()

class powerHolder(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'pwholder'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('powerholder.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class instructions(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'instructions'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('instructions.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'arrow'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('arrow.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def rotate(self, angle, x, y):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        self.image = pygame.image.load('arrow.png')
        self.rect = self.image.get_rect()
    def flip(self, y):
        self.image = pygame.transform.flip(self.image,False,True)
        self.rect.y = y
    def flipOther(self):
        self.image = pygame.transform.flip(self.image,False,True)
    def resetLeft(self):
        self.image = pygame.image.load('arrowleft.png')
        self.rect = self.image.get_rect()
    def rotateLeft(self, angle, x, y):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y    

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
        self.isMan = True
        self.isWoman = False
        self.isAlien = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def kill(self):
        self.image = pygame.image.load('dead.png')
        self.isDead = True
    def reviveMan(self):
        self.image = pygame.image.load('man.png')
        self.isDead = False
    def reviveWoman(self):
        self.image = pygame.image.load('woman.png')
        self.isDead = False
    def reviveAlien(self):
        self.image = pygame.image.load('alien.png')
        self.isDead = False       
    def flip(self):
        self.image = pygame.transform.flip(self.image,True,False)
    def becomeWoman(self):
        self.image = pygame.image.load('woman.png')
        self.isMan = False
        self.isWoman = True
        self.isAlien = False
    def becomeAlien(self):
        self.image = pygame.image.load('alien.png')
        self.isMan = False
        self.isAlien = True
        self.isWoman = False
    def becomeMan(self):
        self.image = pygame.image.load('man.png')
        self.isMan = True
        self.isWoman = False
        self.isAlien = False

        
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


class helpButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'help'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('helpButton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('helpButtonOver.png')
    def unhighlight(self):
        self.image = pygame.image.load('helpButton.png')


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


class backButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'backbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('backButton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('backButtonOver.png')
    def unhighlight(self):
        self.image = pygame.image.load('backButton.png')


class nextButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'nextbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('nextButton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('nextButtonOver.png')
    def unhighlight(self):
        self.image = pygame.image.load('nextButton.png')

class potionButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'potionbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('potion.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('potionOver.png')
    def unhighlight(self):
        self.image = pygame.image.load('potion.png')


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


class creditButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'crdbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('creditButton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('creditButtonOver.png')
    def unhighlight(self):
        self.image = pygame.image.load('creditButton.png')


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

class yesButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'Yesbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('yesbutton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('yesbuttonover.png')
    def unhighlight(self):
        self.image = pygame.image.load('yesbutton.png')


class manButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'manbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('manbutton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('manbuttonover.png')
    def unhighlight(self):
        self.image = pygame.image.load('manbutton.png')

class womanButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'womanbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('womanbutton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('womanbuttonover.png')
    def unhighlight(self):
        self.image = pygame.image.load('womanbutton.png')

class otherButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'otherbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('otherbutton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('otherbuttonover.png')
    def unhighlight(self):
        self.image = pygame.image.load('otherbutton.png')



class noButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'Nobtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('nobutton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('nobuttonover.png')
    def unhighlight(self):
        self.image = pygame.image.load('nobutton.png')
    def OKhighlight(self):
        self.image = pygame.image.load('okbuttonover.png')
    def OKunhighlight(self):
        self.image = pygame.image.load('okbutton.png')
    def turnOK(self):
        self.image = pygame.image.load('okbutton.png')
    def reset(self):
        self.image = pygame.image.load('nobutton.png')

        

class quitButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.id = 'quitbtn'
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('quitbutton.png')
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def highlight(self):
        self.image = pygame.image.load('quitbuttonover.png')
    def unhighlight(self):
        self.image = pygame.image.load('quitbutton.png')

def leaveScreen():

    
    leaveMenu = False
    playButton = noButton()
    playButton.reset()
    playButton.rect.x = screenWidth/2 - playButton.rect.width/2 + 100
    playButton.rect.y = 200
    isInButton = False
    credBut = yesButton()
    credBut.rect.x = screenWidth/2 - playButton.rect.width/2 - 100
    credBut.rect.y = 200
    isInCredits = False
    question = "Are you sure you want to leave?"
    firstQuestion = False
    secondQuestion = False
    thirdQuestion = False
    
    while (leaveMenu == False):

        clicked = pygame.mouse.get_pressed()
        screen.fill(grey);
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(question, 1, (0, 0, 0))
        tWidth = text.get_width()
        screen.blit(font.render(question, True, black), ((screenWidth/2)-tWidth/2,50))
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == firstOver:
                pygame.mixer.music.load('loopsong.ogg')
                pygame.mixer.music.play(-1)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if credBut.rect.collidepoint(mouse):
                    if(not firstQuestion):
                        question = "Are you really sure?"
                        firstQuestion = True
                    elif(not secondQuestion):
                        question = "Absolutely sure?"
                        secondQuestion = True
                    elif(not thirdQuestion):
                        thirdQuestion = True
                        question = "I'm sorry Dave, I'm afraid I can't do that."
                        playButton.turnOK()
                        playButton.rect.x = 550
                        playButton.rect.y = 200
                if playButton.rect.collidepoint(mouse):
                    leaveMenu=True

        if playButton.rect.collidepoint(mouse):
            if(not isInButton):
                if (not thirdQuestion):
                    playButton.highlight()
                    isInButton = True
                else:
                    playButton.OKhighlight()
                    isInButton = True
        if not(playButton.rect.collidepoint(mouse)):
            if(isInButton):
                if (not thirdQuestion):
                    playButton.unhighlight()
                    isInButton = False
                else:
                    playButton.OKunhighlight()
                    isInButton = False

                    
            if(not isInCredits): 
               credBut.highlight()
               isInCredits = True
        if not(credBut.rect.collidepoint(mouse)):
            if(isInCredits):    
               credBut.unhighlight()
               isInCredits = False

        
        playButton.draw(screen)
        if(not thirdQuestion):
            credBut.draw(screen)
        pygame.display.update()
        clock.tick(fps)

    


def mainMenu():
    
    leaveMenu = False
    playButton = button()
    playButton.rect.x = screenWidth/2 - playButton.rect.width/2
    playButton.rect.y = 250
    isInButton = False
    credBut = creditButton()
    credBut.rect.x = screenWidth/2 - playButton.rect.width/2
    credBut.rect.y = 350
    isInCredits = False
    leaveBut = quitButton()
    leaveBut.rect.x = screenWidth/2 - playButton.rect.width/2
    leaveBut.rect.y = 400
    isInLeave = False
    helpBut = helpButton()
    helpBut.rect.x = screenWidth/2 - playButton.rect.width/2
    helpBut.rect.y = 300
    isInHelp = False

    cantTouch = cantTouchThis()
    cantTouch.rect.x = random.randint(0,400)
    cantTouch.rect.y = random.randint(200,550)
    touchCount = 0
    
    while (leaveMenu == False):
        for event in pygame.event.get():
            if event.type == firstOver:
                pygame.mixer.music.load('loopsong.ogg')
                pygame.mixer.music.play(-1)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clicked = pygame.mouse.get_pressed()
        screen.fill(grey);
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render("SNOWBALL FIGHT", 1, (0, 0, 0))
        tWidth = text.get_width()
        screen.blit(font.render("SNOWBALL FIGHT", True, black), ((screenWidth/2)-tWidth/2,60))
        mouse = pygame.mouse.get_pos()

        if cantTouch.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                if(touchCount<3):
                    touchCount+=1
                    cantTouch.rect.x = random.randint(0,400)
                    cantTouch.rect.y = random.randint(200,550)
                else:
                    cantTouch.hammertime()
            
    
        
        if playButton.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                userChoice=playerSelection()
                if not(userChoice[0]==-1):
                    leaveMenu=True
            if(not isInButton): 
               playButton.highlight()
               isInButton = True
        if not(playButton.rect.collidepoint(mouse)):
            if(isInButton):    
               playButton.unhighlight()
               isInButton = False

        if credBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                creditScreen()
            if(not isInCredits): 
               credBut.highlight()
               isInCredits = True
        if not(credBut.rect.collidepoint(mouse)):
            if(isInCredits):    
               credBut.unhighlight()
               isInCredits = False


        if helpBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                instructionScreen()
            if(not isInHelp): 
               helpBut.highlight()
               isInHelp = True
        if not(helpBut.rect.collidepoint(mouse)):
            if(isInHelp):    
               helpBut.unhighlight()
               isInHelp = False

        if leaveBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                leaveScreen()
            if(not isInLeave): 
               leaveBut.highlight()
               isInLeave = True
        if not(leaveBut.rect.collidepoint(mouse)):
            if(isInLeave):    
               leaveBut.unhighlight()
               isInLeave = False

        cantTouch.draw(screen)
        playButton.draw(screen)
        credBut.draw(screen)
        helpBut.draw(screen)
        leaveBut.draw(screen)
        pygame.display.update()
        clock.tick(fps)
    return userChoice   

def creditScreen():
    leaveMenu = False
    menuBut = backButton()
    menuBut.rect.x =  screenWidth/2 - menuBut.rect.width/2
    menuBut.rect.y = 500
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
        
        screen.fill(grey)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render("Who checks the credits anyway?", 1, (0, 0, 0))
        tWidth = text.get_width()
        screen.blit(font.render(str("Who checks the credits anyway?"), True, black), ((screenWidth/2)-tWidth/2,50))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Raul sozcos()", 1, (0, 0, 0))
        tWidth = text.get_width()
        screen.blit(font.render(str("Raul sozcos()"), True, black), ((screenWidth/2)-tWidth/2,150))
        text = font.render("Formiga Ferrera", 1, (0, 0, 0))
        tWidth = text.get_width()
        screen.blit(font.render(str("Formiga Ferrera"), True, black), ((screenWidth/2)-tWidth/2,180))

        mouse = pygame.mouse.get_pos()
        if menuBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                leaveMenu=True
                
            if(not isInButton): 
               menuBut.highlight()
               isInButton = True
        if not(menuBut.rect.collidepoint(mouse)):
            if(isInButton):    
               menuBut.unhighlight()
               isInButton = False

        menuBut.draw(screen)
        pygame.display.update()
        clock.tick(fps)

def instructionScreen():
    leaveMenu = False
    menuBut = backButton()
    menuBut.rect.x = screenWidth/2 - menuBut.rect.width/2
    menuBut.rect.y = 520
    isInButton = False
    instruct = instructions()
    instruct.rect.x = 0
    instruct.rect.y = 0
    
    while (leaveMenu == False):
        for event in pygame.event.get():
            if event.type == firstOver:
                pygame.mixer.music.load('loopsong.ogg')
                pygame.mixer.music.play(-1)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clicked = pygame.mouse.get_pressed()
        
        screen.fill(white)

        mouse = pygame.mouse.get_pos()
        if menuBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                leaveMenu=True
                
            if(not isInButton): 
               menuBut.highlight()
               isInButton = True
        if not(menuBut.rect.collidepoint(mouse)):
            if(isInButton):    
               menuBut.unhighlight()
               isInButton = False

        instruct.draw(screen)
        menuBut.draw(screen)
        pygame.display.update()
        clock.tick(fps)
    
    
def gameOver(winner):

    pygame.mixer.music.stop()
    userChoice = [-1,-1]
    leaveMenu = False
    againBut = againButton()
    againBut.rect.x = screenWidth/2 - againBut.rect.width/2 - 50
    againBut.rect.y = 300
    menuBut = menuButton()
    menuBut.rect.x = screenWidth/2 - againBut.rect.width/2 + 50
    menuBut.rect.y = 300
    isInButton = False
    isInMenu = False
    while (leaveMenu == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clicked = pygame.mouse.get_pressed()
        screen.fill(grey)
        font = pygame.font.Font('freesansbold.ttf', 70)
        text = font.render("GAME OVER", 1, (0, 0, 0))
        tWidth = text.get_width()
        screen.blit(font.render(str("GAME OVER"), True, black), ((screenWidth/2)-tWidth/2,100))

        if(winner==0):
            font = pygame.font.Font('freesansbold.ttf', 40)
            text = font.render("Men are superior.", 1, (0, 0, 0))
            tWidth = text.get_width()
            screen.blit(font.render(str("Men are superior."), True, black), ((screenWidth/2)-tWidth/2,200))            
        elif(winner==1):
            font = pygame.font.Font('freesansbold.ttf', 40)
            text = font.render("Women are superior.", 1, (0, 0, 0))
            tWidth = text.get_width()
            screen.blit(font.render(str("Women are superior."), True, black), ((screenWidth/2)-tWidth/2,200))            
        elif(winner==2):
            font = pygame.font.Font('freesansbold.ttf', 40)
            text = font.render("Aliens are superior.", 1, (0, 0, 0))
            tWidth = text.get_width()
            screen.blit(font.render(str("Aliens are superior."), True, black), ((screenWidth/2)-tWidth/2,200))                  
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
                userChoice = mainMenu()
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
    return userChoice



def playerSelection():

    
    leaveMenu = False
    otherBut = otherButton()
    otherBut.rect.right = 1000
    otherBut.rect.y = 120
    manBut = manButton()
    manBut.rect.x = 200
    manBut.rect.y = 120
    womanBut = womanButton()
    womanBut.rect.x = screenWidth/2 - womanBut.rect.width/2
    womanBut.rect.y = 120
    menuBut = backButton()
    menuBut.rect.x = screenWidth/2 - menuBut.rect.width/2 - 50
    menuBut.rect.y = 500
    nextBut = nextButton()
    nextBut.rect.x = screenWidth/2 - menuBut.rect.width/2 + 50
    nextBut.rect.y = 500

    
    secotherBut = otherButton()
    secotherBut.rect.right = 1000
    secotherBut.rect.y = 320
    secmanBut = manButton()
    secmanBut.rect.x = 200
    secmanBut.rect.y = 320
    secwomanBut = womanButton()
    secwomanBut.rect.x = screenWidth/2 - womanBut.rect.width/2
    secwomanBut.rect.y = 320

    
    isInMan = [True, True]
    isInOther = [False, False]
    isInWoman = [False, False]
    isInButton = False
    isInNext = False
    userChoice = [0, 0]
    manBut.highlight()
    secmanBut.highlight()
    
    while (leaveMenu == False):
        for event in pygame.event.get():
            if event.type == firstOver:
                pygame.mixer.music.load('loopsong.ogg')
                pygame.mixer.music.play(-1)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clicked = pygame.mouse.get_pressed()
        
        screen.fill(grey)
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render("Team 1:", 1, (0, 0, 0))
        tWidth = text.get_width()
        screen.blit(font.render(str("Team 1:"), True, black), ((screenWidth/2)-tWidth/2,50))
        text = font.render("Team 2:", 1, (0, 0, 0))
        tWidth = text.get_width()
        screen.blit(font.render(str("Team 2:"), True, black), ((screenWidth/2)-tWidth/2,250))

        mouse = pygame.mouse.get_pos()

        
        if menuBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                leaveMenu=True
                userChoice[0] = -1
                return userChoice
            if(not isInButton): 
               menuBut.highlight()
               isInButton = True
        if not(menuBut.rect.collidepoint(mouse)):
            if(isInButton):    
               menuBut.unhighlight()
               isInButton = False

        if nextBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                leaveMenu=True
                return userChoice
            if(not isInNext): 
               nextBut.highlight()
               isInNext = True
        if not(nextBut.rect.collidepoint(mouse)):
            if(isInNext):    
               nextBut.unhighlight()
               isInNext = False

        if womanBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                womanBut.highlight()
                manBut.unhighlight()
                otherBut.unhighlight()
                userChoice[0] = 1
        elif manBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                userChoice[0] = 0
                manBut.highlight()
                womanBut.unhighlight()
                otherBut.unhighlight()
        elif otherBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                userChoice[0] = 2
                manBut.unhighlight()
                womanBut.unhighlight()
                otherBut.highlight()

        if secwomanBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                secwomanBut.highlight()
                secmanBut.unhighlight()
                secotherBut.unhighlight()
                userChoice[1] = 1
        elif secmanBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                userChoice[1] = 0
                secmanBut.highlight()
                secwomanBut.unhighlight()
                secotherBut.unhighlight()
        elif secotherBut.rect.collidepoint(mouse):
            if(clicked[0] == 1):
                userChoice[1] = 2
                secmanBut.unhighlight()
                secwomanBut.unhighlight()
                secotherBut.highlight()
                
        menuBut.draw(screen)
        otherBut.draw(screen)
        manBut.draw(screen)
        womanBut.draw(screen)
        secotherBut.draw(screen)
        secmanBut.draw(screen)
        secwomanBut.draw(screen)
        nextBut.draw(screen)
        pygame.display.update()
        clock.tick(fps)



screenWidth = 1200
screenHeight = 600
gameTitle = "Snowball Fight"
white = (248,243,237)
black = (54, 51, 47)
grey = (105, 102, 98)
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
heightBoundary = 8*math.pi/20
minimumSize = 15
maximumSize = 75
#Changeable stuff

    
all_sprites_list = pygame.sprite.Group()
snowList = pygame.sprite.Group()
fabricList = pygame.sprite.Group()
powerList = pygame.sprite.Group()
chillList = pygame.sprite.Group()
potionList = pygame.sprite.Group()
gunButList = pygame.sprite.Group()
bullList = pygame.sprite.Group()
gunList = pygame.sprite.Group()
arrowList = pygame.sprite.Group()
pwBarList = pygame.sprite.Group()



distanceToBorder = 100
distanceToHeight = 50

player = [man() for i in range(6)]
player[0].rect.x = distanceToBorder
player[0].rect.y = distanceToHeight
all_sprites_list.add(player[0])
player[1].rect.x = distanceToBorder
player[1].rect.y = screenHeight/2 - player[1].rect.height/2
all_sprites_list.add(player[1])
player[2].rect.x = distanceToBorder
player[2].rect.bottom = screenHeight - distanceToHeight
all_sprites_list.add(player[2])
player[3].rect.right = screenWidth-distanceToBorder
player[3].rect.y = distanceToHeight
all_sprites_list.add(player[3])
player[4].rect.right = screenWidth-distanceToBorder
player[4].rect.y = screenHeight/2 - player[1].rect.height/2
all_sprites_list.add(player[4])
player[5].rect.right = screenWidth-distanceToBorder
player[5].rect.bottom = screenHeight - distanceToHeight






all_sprites_list.add(player[5])
scroll = scroller()
scroll.rect.x = 550
scroll.rect.y = 0
all_sprites_list.add(scroll)
fabr = fabric()
fabr.rect.x = (player[3].rect.right + player[0].rect.x)/2 - fabr.rect.width/2
fabr.rect.y = 0
fabricList.add(fabr)
gifts = [gift() for i in range(3)]
gifts[0].rect.x = (player[3].rect.right + player[0].rect.x)/2 - fabr.rect.width/2
gifts[0].rect.y = 500
all_sprites_list.add(gifts[0])
gifts[1].rect.x = (player[3].rect.right + player[0].rect.x)/2 - fabr.rect.width/2
gifts[1].rect.y = 300
all_sprites_list.add(gifts[1])
gifts[2].rect.x = (player[3].rect.right + player[0].rect.x)/2 - fabr.rect.width/2
gifts[2].rect.y = 100
all_sprites_list.add(gifts[2])


extraBtn = extraButton()
extraBtn.rect.x = 200
extraBtn.rect.y = 700
powerList.add(extraBtn)

chillBtn = chillButton()
chillBtn.rect.x = 200
chillBtn.rect.y = 600
chillList.add(chillBtn)

gunBtn = gunButton()
gunBtn.rect.x = 200
gunBtn.rect.y = 500
gunButList.add(gunBtn)

potionBtn = potionButton()
potionBtn.rect.x = 200
potionBtn.rect.y = 500
potionList.add(potionBtn)


bull = bullet()
bull.rect.x = 0
bull.rect.y = 0
bullList.add(bull)


gunObj = gun()
gunObj.rect.x = 0
gunObj.rect.y = 0
gunList.add(gunObj)


powerHold = powerHolder()
powerHold.rect.x = 0
powerHold.rect.y = 0
pwBarList.add(powerHold)

power = powerBar()
power.rect.x = 0
power.rect.y = 0
pwBarList.add(power)
powerHeight = power.rect.height




arrowObj = arrow()
arrowObj.rect.x = 0
arrowObj.rect.y = 0
arrowList.add(arrowObj)
arrowHeight = arrowObj.rect.height
arrowWidth = arrowObj.rect.width


extraUp = [False, False]
extraInButton = False
extraActivated = [False, False]
chillUp = [False, False]
chillInButton = False
chillActivated = [False, False]
gunUp = [False, False]
gunInButton = False
gunActivated = [False, False]
potionUp = [False, False]
potionInButton = False
potionActivated = [False, False]


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
gravity = 8
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
angle=0
textToSay = "Select Player"
gunConstant = 0

userChoice = mainMenu()

if(userChoice[0]==1):
    player[0].becomeWoman()
    player[1].becomeWoman()
    player[2].becomeWoman()
elif(userChoice[0]==2):
    player[0].becomeAlien()
    player[1].becomeAlien()
    player[2].becomeAlien()


if(userChoice[1]==1):
    player[3].becomeWoman()
    player[4].becomeWoman()
    player[5].becomeWoman()
elif(userChoice[1]==2):
    player[3].becomeAlien()
    player[4].becomeAlien()
    player[5].becomeAlien()

player[3].flip()
player[4].flip()
player[5].flip()




while close == False:

    
    buttonUp = False
    waitingForRevive = False
    potionJustUsed = False
    
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
                        if currentTurn==1:
                            angle = -(angle + 2*math.pi/2)
                    elif lineSizeStop == False:
                        lineSizeStop = True

                    elif lineDoneStop == False:
                        if currentTurn==1:
                            heightAngle = heightLineClock*2*math.pi/lineHeightTime + angle
                        lineDoneStop = True
                        initialHSpeed = abs(lineSize*math.cos(heightAngle-angle)/2)
                        ballX = player[selectedPlayer+currentTurn*3].rect.x + 25
                        ballY = player[selectedPlayer+currentTurn*3].rect.y + 50
                        pygame.mixer.Sound.play(snowThrow)
        if event.type == pygame.MOUSEBUTTONUP:
            buttonUp = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (not(potionBtn.rect.collidepoint(mouse) and potionUp[currentTurn])) or (not(extraBtn.rect.collidepoint(mouse) and extraUp[currentTurn])) or (not(gunBtn.rect.collidepoint(mouse) and gunUp[currentTurn])) or (not(chillBtn.rect.collidepoint(mouse) and chillUp[currentTurn])):
                if playerChosen == True:
                    if lineAngleStop == False:
                        lineAngleStop = True
                        if currentTurn==1:
                            angle = -(angle + 2*math.pi/2)
                    elif lineSizeStop == False:
                        lineSizeStop = True
                    elif lineDoneStop == False:
                        lineDoneStop = True
                        if currentTurn==1:
                            heightAngle = heightLineClock*2*math.pi/lineHeightTime + angle
                        initialHSpeed = abs(lineSize*math.cos(heightAngle-angle)/2)
                        ballX = player[selectedPlayer+currentTurn*3].rect.x + 25
                        ballY = player[selectedPlayer+currentTurn*3].rect.y + 50
                        pygame.mixer.Sound.play(snowThrow)

    clicked = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    if(chillActivated[currentTurn]):
        lineAngleTime = 4
        lineHeightTime = 4
        lineSizeTime = 2
        chillActivated[currentTurn] = False

    if(potionActivated[currentTurn]):
        waitingForRevive = True
        if( (not player[currentTurn*3].isDead) and (not player[1 + currentTurn*3].isDead) and (not player[2+currentTurn*3].isDead)):
            potionActivated[currentTurn] = False
            potionUp[currentTurn] = True
            textToSay = "All players are alive"
            waitingForRevive = False
        else:
            textToSay = "Select a player to revive"
            for i in range(0,3):
                if player[i+currentTurn*3].rect.collidepoint(mouse):
                    if(buttonUp) and (player[i+currentTurn*3].isDead):
                        buttonUp = False
                        if(player[i+currentTurn*3].isMan):
                            player[i+currentTurn*3].reviveMan()
                        elif(player[i+currentTurn*3].isWoman):
                            player[i+currentTurn*3].reviveWoman()
                        elif(player[i+currentTurn*3].isAlien):
                            player[i+currentTurn*3].reviveAlien()
                        if(currentTurn==1):
                            player[i+currentTurn*3].flip()
                        potionActivated[currentTurn] = False
                        waitingForRevive = False
                        textToSay = "Select Player"
                        

    
    
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

    if(not waitingForRevive):
        if playerChosen == False:
            mouse = pygame.mouse.get_pos()
            for i in range(0,3):
              if player[i+currentTurn*3].rect.collidepoint(mouse):
                  if(buttonUp) and (not player[i+currentTurn*3].isDead):
                    selectedPlayer = i
                    playerChosen = True
        else:      
            textToSay = "Select Player"
            if lineDoneStop == False:
        
                if gunActivated[currentTurn]:
                    gunConstant = 30
                    if(currentTurn==0):
                        gunObj.rect.x = player[selectedPlayer+currentTurn*3].rect.x + 60
                    else:
                        gunObj.rect.right = player[selectedPlayer+currentTurn*3].rect.x -60 + player[0].rect.width
                    gunObj.rect.y = player[selectedPlayer+currentTurn*3].rect.y+50
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
                    ballX = player[selectedPlayer+currentTurn*3].rect.x+60*currentDirection+player[0].rect.width*currentTurn+gunConstant*currentDirection
                    ballY = player[selectedPlayer+currentTurn*3].rect.y+50
                    bull.rotate(math.degrees(angle-math.pi/2), ballX, ballY)
                    gunConstant = 0
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
                    heightAngle = heightLineClock*2*math.pi/lineHeightTime + angle - currentTurn*math.pi/2
                    trueY = maximumSize * math.cos(heightAngle)
                    trueX = maximumSize * math.sin(heightAngle)
                    if currentDirection == -1:
                        heightAngle -= heightBoundary
                    yAngleLine = lineSize * math.cos(heightAngle)
                    xAngleLine = lineSize * math.sin(heightAngle)
                    pygame.draw.line(screen, black, (player[selectedPlayer+currentTurn*3].rect.x+60*currentDirection+player[0].rect.width*currentTurn, player[selectedPlayer+currentTurn*3].rect.y+50), (trueX + player[selectedPlayer+currentTurn*3].rect.x + 60*currentDirection+player[0].rect.width*currentTurn, trueY + player[selectedPlayer+currentTurn*3].rect.y + 50), 4)
                yLine = lineSize * math.cos(angle)
                xLine = lineSize * math.sin(angle)

                #LINE PROCESSS
                #
                #
                

                if(not lineAngleStop):

                    yConstant=50

                    
                    if(currentTurn==0):
                        arrowObj.reset()
                        arrowObj.rotate(math.degrees(abs(angle-math.pi/2)), player[selectedPlayer+currentTurn*3].rect.x+gunConstant*currentDirection+60*currentDirection+player[0].rect.width*currentTurn, player[selectedPlayer+currentTurn*3].rect.y+yConstant-arrowHeight*math.cos(abs(angle-math.pi/2-currentTurn*math.pi))-arrowWidth*math.sin(abs(angle-math.pi/2-currentTurn*math.pi))+arrowHeight)
                        if(angle-math.pi/2 -currentTurn*math.pi)<0:
                            arrowObj.flip(player[selectedPlayer+currentTurn*3].rect.y+yConstant-arrowHeight*math.cos(abs(angle-math.pi/2-currentTurn*math.pi))-arrowWidth*math.sin(abs(angle-math.pi/2-currentTurn*math.pi))+arrowHeight+arrowWidth*math.sin(abs(angle-math.pi/2-currentTurn*math.pi)))
                        
                    else:
                        arrowObj.resetLeft()
                        arrowObj.rotateLeft(math.degrees(-abs(angle-3*math.pi/2)), player[selectedPlayer+currentTurn*3].rect.x+gunConstant*currentDirection+60*currentDirection+player[0].rect.width*currentTurn, player[selectedPlayer+currentTurn*3].rect.y+yConstant-arrowHeight*math.cos(abs(angle-math.pi/2-currentTurn*math.pi))-arrowWidth*math.sin(abs(angle-math.pi/2-currentTurn*math.pi))+arrowHeight)
                        if(angle-math.pi/2 -currentTurn*math.pi)<0:
                            arrowObj.flip(player[selectedPlayer+currentTurn*3].rect.y+yConstant-arrowHeight*math.cos(abs(angle-math.pi/2-currentTurn*math.pi))-arrowWidth*math.sin(abs(angle-math.pi/2-currentTurn*math.pi))+arrowHeight+arrowWidth*math.sin(abs(angle-math.pi/2-currentTurn*math.pi)))
                arrowList.update()
                arrowList.draw(screen)


                
                if(lineAngleStop):
                    power.reset()
                    power.scale((lineSize/maximumSize)*power.rect.width,powerHeight)
                    powerHold.rect.x = player[selectedPlayer+currentTurn*3].rect.x - player[selectedPlayer+currentTurn*3].rect.width/2
                    powerHold.rect.y = player[selectedPlayer+currentTurn*3].rect.y + 80
                    power.rect.x = player[selectedPlayer+currentTurn*3].rect.x - player[selectedPlayer+currentTurn*3].rect.width/2
                    power.rect.y = player[selectedPlayer+currentTurn*3].rect.y + 80
                
                    pwBarList.update()
                    pwBarList.draw(screen)
        
            else:
                if(not gunActivated[currentTurn]):
                    if (height > 0):
                        timer += 1/fps
                        height += initialHSpeed - gravity*timer
                        ballX += lineSize*math.sin(angle)*fps/300
                        ballY += bounce*lineSize*math.cos(angle)*fps/300
                        screen.blit(shadowImg,(ball.rect.x+abs(height)*0.01,+ball.rect.y+abs(height)*0.005))
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
                       
                    if(height <= 0) or (ball.rect.right<0) or (ball.rect.x>screenWidth):
                        pygame.mixer.Sound.play(snowFall)
                        currentTurn = swapTurn(currentTurn)
                        currentDirection *= -1
                        for i in range(0,3):
                            if (ball.collides(gifts[i]) and ball.rect.bottom>=100):
                                pygame.mixer.Sound.play(presentSound)
                                obtainedItem = randomItem(extraUp[swapTurn(currentTurn)],chillUp[swapTurn(currentTurn)],gunUp[swapTurn(currentTurn)],potionUp[swapTurn(currentTurn)])
                                if obtainedItem==0:
                                    extraUp[swapTurn(currentTurn)] = True
                                if obtainedItem==1:
                                    chillUp[swapTurn(currentTurn)] = True
                                if obtainedItem==2:
                                    gunUp[swapTurn(currentTurn)] = True
                                if obtainedItem==3:
                                    potionUp[swapTurn(currentTurn)] = True
                                
                            if (ball.collides(player[i+currentTurn*3])) and (not player[i+currentTurn*3].isDead):
                                player[i+currentTurn*3].kill()
                                if(player[currentTurn*3].isDead) and (player[1+currentTurn*3].isDead) and (player[2+currentTurn*3].isDead):
                                    #RESET GAME
                                    pygame.mixer.Sound.play(gameEnd)
                                    newUserChoice = gameOver(userChoice[currentTurn])
                                    
                                    
                                    for i in range(0,6):
                                        if(player[i].isDead):
                                            if(player[i].isMan):
                                                player[i].reviveMan()
                                            elif(player[i].isWoman):
                                                player[i].reviveWoman()
                                            elif(player[i].isAlien):
                                                player[i].reviveAlien()
                                            if(i>=2):
                                                player[i].flip()

                                    if not(newUserChoice[0]==-1):
                                        userChice = newUserChoice
                                        if(userChoice[0]==0):
                                            player[0].becomeMan()
                                            player[1].becomeMan()
                                            player[2].becomeMan()
                                        if(userChoice[0]==1):
                                            player[0].becomeWoman()
                                            player[1].becomeWoman()
                                            player[2].becomeWoman()
                                        elif(userChoice[0]==2):
                                            player[0].becomeAlien()
                                            player[1].becomeAlien()
                                            player[2].becomeAlien()


                                        if(userChoice[1]==0):
                                            player[3].becomeMan()
                                            player[4].becomeMan()
                                            player[5].becomeMan()
                                        if(userChoice[1]==1):
                                            player[3].becomeWoman()
                                            player[4].becomeWoman()
                                            player[5].becomeWoman()
                                        elif(userChoice[1]==2):
                                            player[3].becomeAlien()
                                            player[4].becomeAlien()
                                            player[5].becomeAlien()

                                        player[3].flip()
                                        player[4].flip()
                                        player[5].flip()



                                        
                                    extraUp = [False, False]
                                    extraInButton = False
                                    extraActivated = [False, False]
                                    chillUp = [False, False]
                                    chillInButton = False
                                    chillActivated = [False, False]
                                    gunUp = [False, False]
                                    gunInButton = False
                                    gunActivated = [False, False]
                                    potionUp = [False, False]
                                    potionInButton = False
                                    potionActivated = [False, False]
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
                    ballX += lineSize*math.sin(angle)*fps/150
                    ballY += bounce*lineSize*math.cos(angle)*fps/150
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
                                newUserChoice = gameOver(userChoice[currentTurn])
                                #RESET GAME
                                for i in range(0,6):
                                    if(player[i].isDead):
                                        if(player[i].isWoman):
                                            player[i].reviveWoman()
                                        elif(player[i].isMan):
                                            player[i].reviveMan()
                                        elif(player[i].isAlien):
                                            player[i].reviveAlien()
                                        if(i>=2):
                                            player[i].flip()

                                if not(newUserChoice[0]==-1):
                                    userChoice = newUserChoice
                                    if(userChoice[0]==0):
                                        player[0].becomeMan()
                                        player[1].becomeMan()
                                        player[2].becomeMan()
                                    if(userChoice[0]==1):
                                        player[0].becomeWoman()
                                        player[1].becomeWoman()
                                        player[2].becomeWoman()
                                    elif(userChoice[0]==2):
                                        player[0].becomeAlien()
                                        player[1].becomeAlien()
                                        player[2].becomeAlien()


                                    if(userChoice[1]==1):
                                        player[3].becomeWoman()
                                        player[4].becomeWoman()
                                        player[5].becomeWoman()
                                    if(userChoice[1]==0):
                                        player[3].becomeMan()
                                        player[4].becomeMan()
                                        player[5].becomeMan()
                                    elif(userChoice[1]==2):
                                        player[3].becomeAlien()
                                        player[4].becomeAlien()
                                        player[5].becomeAlien()

                                    player[3].flip()
                                    player[4].flip()
                                    player[5].flip()
                                
                                extraUp = [False, False]
                                extraInButton = False
                                extraActivated = [False, False]
                                chillUp = [False, False]
                                chillInButton = False
                                chillActivated = [False, False]
                                gunUp = [False, False]
                                gunInButton = False
                                gunActivated = [False, False]
                                potionUp = [False, False]
                                potionInButton = False
                                potionActivated = [False, False]
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



        
    
    currentPos = 500

    
    if (extraUp[currentTurn] and (not playerChosen)):
        if(currentTurn==1):
            extraBtn.rect.right = screenWidth - 200   
        else:
            extraBtn.rect.x = 200
            
        extraBtn.rect.y = currentPos
        currentPos -= 40
        powerList.update()
        powerList.draw(screen)
        if extraBtn.rect.collidepoint(mouse):
            if(buttonUp):
                buttonUp = False
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
        if(currentTurn==1):
            chillBtn.rect.right = screenWidth - 200   
        else:
            chillBtn.rect.x = 200

        chillBtn.rect.y = currentPos
        currentPos -= 40
        
        chillList.update()
        chillList.draw(screen)
        if chillBtn.rect.collidepoint(mouse):
            if(buttonUp):
                buttonUp = False
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
    
        if(currentTurn==1):
            gunBtn.rect.right = screenWidth - 200   
        else:
            gunBtn.rect.x = 200

        gunBtn.rect.y = currentPos
        currentPos -= 40
        
        gunButList.update()
        gunButList.draw(screen)
        if gunBtn.rect.collidepoint(mouse):
            if(buttonUp):
                buttonUp = False
                pygame.mixer.Sound.play(gunActivationSound)
                gunActivated[currentTurn] = True
                gunUp[currentTurn] = False
                if(currentTurn==1):
                    gunObj.swap()
                else:
                    gunObj.reset()
            if(not gunInButton): 
                gunBtn.highlight()
                gunInButton = True
        if not(gunBtn.rect.collidepoint(mouse)):
            if(gunInButton):    
                gunBtn.unhighlight()
                gunInButton = False


    if (potionUp[currentTurn] and (not playerChosen)):
    
        if(currentTurn==1):
            potionBtn.rect.right = screenWidth - 200   
        else:
            potionBtn.rect.x = 200

        potionBtn.rect.y = currentPos
        currentPos -= 40
        
        potionList.update()
        potionList.draw(screen)
        if potionBtn.rect.collidepoint(mouse):
            if(buttonUp):
                buttonUp = False
                potionActivated[currentTurn] = True
                potionUp[currentTurn] = False
            if(not potionInButton): 
                potionBtn.highlight()
                potionInButton = True
        if not(potionBtn.rect.collidepoint(mouse)):
            if(potionInButton):    
                potionBtn.unhighlight()
                potionInButton = False


            
    font = pygame.font.Font('freesansbold.ttf', 20)
    if playerChosen == False:
        if(textToSay=="Select Player"):
            if(userChoice[0]==userChoice[1]):
                textToSay = "Team " + str(currentTurn+1) + ": Select Player"
            else:
                if(userChoice[currentTurn]==0):
                    textToSay = "Men: Select Player"
                if(userChoice[currentTurn]==1):
                    textToSay = "Women: Select Player"
                if(userChoice[currentTurn]==2):
                    textToSay = "Aliens: Select Player"  
        screen.blit(font.render(str(textToSay), True, black), (10,10))

    pygame.display.update()
        
pygame.quit()

    






