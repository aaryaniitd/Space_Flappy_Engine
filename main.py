import random
import sys #sys.exit to exit the program
import pygame
# # from pygame.locals import *
# from sympy import Q

# from test import mainGame #Basic pygame imports

# Global variables for the game
FPS = 32
SCREENWIDTH = 1280
SCREENHEIGHT = 659
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) # Initialize a window or screen for display
GROUNDY =  SCREENHEIGHT*0.5

GAME_SPRITES = {}
GAME_SOUNDS = {}

PLAYER = './gallery/rocket.png'
BACKGROUND = './gallery/back1.png'
PIPE = './gallery/pipe.png'

pygame.init() #Initialise all pygame modules
FPSCLOCK = pygame.time.Clock() #To control FPS of game
pygame.display.set_caption('FLappy Bird by Aaryan Ahuja')
GAME_SPRITES['numbers'] = (
    pygame.image.load('./gallery/0.png').convert_alpha(),
    pygame.image.load('./gallery/1.png').convert_alpha(),
    pygame.image.load('./gallery/2.png').convert_alpha(),
    pygame.image.load('./gallery/3.png').convert_alpha(),
    pygame.image.load('./gallery/4.png').convert_alpha(),
    pygame.image.load('./gallery/5.png').convert_alpha(),
    pygame.image.load('./gallery/6.png').convert_alpha(),
    pygame.image.load('./gallery/7.png').convert_alpha(),
    pygame.image.load('./gallery/8.png').convert_alpha(),
    pygame.image.load('./gallery/9.png').convert_alpha()

) #convert_alpha is to optimize the image for the game
# GAME_SPRITES['message'] = pygame.image.load('./gallery/message.png')
GAME_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
    pygame.image.load(PIPE).convert_alpha()
)
GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

# Shows welcome images on the screen
playerx = int(SCREENWIDTH/5)
playery = int((SCREENHEIGHT- GAME_SPRITES['player'].get_height())/2)
# messagex = int((SCREENWIDTH- GAME_SPRITES['message'].get_width())/2)
# messagey = int((SCREENHEIGHT*0.13))
basex = 0
def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex  = 0

    # Create 2 pipes for blitting on screen 
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list for upperpipes
    upperPipes = [
        {'x':SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']}

    ]
    lowerPipes = [
        {'x':SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']}

    ]
    pipeVelx = -4
    
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 #velocity while flapping
    playerFlapped = False # Only true when bird flaps

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                if playery > 0: # if player is in the screen
                    playerVelY = playerFlapAccv
                    playerFlapped = True
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)

        if crashTest:
            return 

        # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if playerMidPos <= pipeMidPos < pipeMidPos +4:
                score += 1
                print(f"Your score is {score}")

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY


        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES['player'].get_height()
        playery += min(playerVelY, GROUNDY-playery-playerHeight)

        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelx
            lowerPipe['x'] += pipeVelx
        # add a new pipe when the first is about to cross the left part of screen

        if 0 < upperPipes[0]['x']<5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            upperPipes.append(newPipe[1])
        # if the pipe is out of screen, remove it
        if upperPipes[0]['x'] <- GAME_SPRITES['pipe'][0].get_width() :
            upperPipes.pop(0)
            lowerPipes.pop(0) 

        # Blitting our sprites
        SCREEN.blit(GAME_SPRITES['player'],(playerx, playery))
        SCREEN.blit(GAME_SPRITES['background'],(0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'], upperPipe['y']))      
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        myDigits = [int(x) for x in list(str(score))]    
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH-width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()            

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - GAME_SPRITES['player'].get_height() or playery <= 0:
        return True
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if playery< pipeHeight+ pipe['y'] and abs(playerx-pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            return True

    for pipe in lowerPipes:
    
        if playery + GAME_SPRITES['player'].get_height() > pipe['y'] and abs(playerx-pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            return True

    return False        


def getRandomPipe():
    # Generate positions of two pipes for blitting on the screen

    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0,int(SCREENHEIGHT-1.2*offset))
    pipeX = SCREENWIDTH+10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x':pipeX, 'y':-y1},
        {'x':pipeX, 'y':y2}
    ]
    return pipe
while True:
    for event in pygame.event.get():
        #if user clicks cross button, close the game
        if event.type == pygame.QUIT or (event.type== pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
        # If the user presses space or up key, start the game for them
        elif event.type==pygame.KEYDOWN and (event.key==pygame.K_SPACE or event.key == pygame.K_UP):
            mainGame()
            pygame.display.update()

        else:
            SCREEN.blit(GAME_SPRITES['background'], (0,0))
            SCREEN.blit(GAME_SPRITES['player'], (playerx,playery))        
            # SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey))        
            # SCREEN.blit(GAME_SPRITES['base'], (basex,GROUNDY))
            pygame.display.update()       
            FPSCLOCK.tick(FPS) # to keep limit of fps to FPS
    

    


        # This will be the point from where our game will start


    # Game Sounds - Left for future

