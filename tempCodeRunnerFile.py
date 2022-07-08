ame.init() #Initialise all pygame modules
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
GAME_SPRITES['player'