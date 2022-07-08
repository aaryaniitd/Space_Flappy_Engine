import pygame
import sys
import random
import time

pygame.init()

def game_floor():
    screen.blit(floor_base,(floor_x_pos,600))
    

clock = pygame.time.Clock()
rocket_movement = 150
gravity = 1
screen = pygame.display.set_mode((1289, 800))
background = pygame.image.load('./gallery/back1.png').convert_alpha()
background_x_pos = 0
# background = pygame.transform.scale2x(background)
rocket = pygame.image.load('./gallery/rocket.png').convert_alpha()
rocket_rect = rocket.get_rect(center=(100,330))
rocket1 = pygame.image.load('./gallery/rocket.png').convert_alpha()

rocket_rect1 = rocket1.get_rect()

floor_base = pygame.image.load('./gallery/base.png').convert_alpha()
floor_base = pygame.transform.scale2x(floor_base)

message = pygame.image.load('./gallery/message1.png').convert_alpha()

# Building Pipes
pipe_surface1 = pygame.image.load('./gallery/pipe.png').convert_alpha()
# pipe_surface1 = pygame.transform.scale2x(pipe_surface1)
pipe_surface2 = pygame.transform.flip(pipe_surface1, False, True)
pipe_list = []

pipe_height = [280,380,480]

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
CHECKSCORE = pygame.USEREVENT
pygame.time.set_timer(CHECKSCORE, 400)
def welcome_screen():
    pass
def score():
    score = 0
    pass
def check_collision(pipes):
    
    for i in range(2,len(pipes),2):
        if pipes[i].left < rocket_rect.centerx and pipes[i].right > rocket_rect.centerx :
            if (rocket_rect.centery > pipes[i].top or rocket_rect.centery < pipes[i+1].bottom):
                return False

    if rocket_rect.top <= -100 or rocket_rect.bottom >= 660:
        return False
    else:
        return True
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    if len(pipe_list) > 0:    
        
        top_pipe1 = pipe_surface1.get_rect(midbottom = (260, random_pipe_pos-200))
        bottom_pipe1 = pipe_surface2.get_rect(midtop = (660, random_pipe_pos))
        top_pipe1.centerx = bottom_pipe1.centerx = pipe_list[-1].centerx + 644.5   
        
        top_pipe2 = pipe_surface1.get_rect(midbottom = (260, random_pipe_pos-200))
        bottom_pipe2 = pipe_surface2.get_rect(midtop = (660, random_pipe_pos))
        top_pipe2.centerx = bottom_pipe2.centerx = pipe_list[-1].centerx + 644.5*2

        # top_pipe3 = pipe_surface1.get_rect(midbottom = (260, random_pipe_pos-200))
        # bottom_pipe3 = pipe_surface2.get_rect(midtop = (660, random_pipe_pos))
        # top_pipe3.centerx = bottom_pipe3.centerx = pipe_list[-1].centerx + 429.667*3
    
    if len(pipe_list) == 0:

        top_pipe1 = pipe_surface1.get_rect(midbottom = (260, random_pipe_pos-200))
        bottom_pipe1 = pipe_surface2.get_rect(midtop = (660, random_pipe_pos))
        top_pipe1.centerx = bottom_pipe1.centerx = 50   
        
        top_pipe2 = pipe_surface1.get_rect(midbottom = (260, random_pipe_pos-200))
        bottom_pipe2 = pipe_surface2.get_rect(midtop = (660, random_pipe_pos))
        top_pipe2.centerx = bottom_pipe2.centerx = 50 + 644.5*1

        # top_pipe3 = pipe_surface1.get_rect(midbottom = (260, random_pipe_pos-200))
        # bottom_pipe3 = pipe_surface2.get_rect(midtop = (660, random_pipe_pos))
        # top_pipe3.centerx = bottom_pipe3.centerx = 50 + 429.667*2
    
    return bottom_pipe1, top_pipe1, bottom_pipe2, top_pipe2 #bottom_pipe3, top_pipe3

def move_pipes(pipes):
    
    n = len(pipes)
    i = 0
    while i < n:
        pipes[i].centerx = pipes[i+1].centerx
        pipes[i+1].centerx -= 3
        pipes[i].centerx -= 3
        i += 2
    return pipes    

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 540:
            screen.blit(pipe_surface1, pipe)
        else:
            screen.blit(pipe_surface2, pipe)    
        # screen.blit(pipe_surface2, pipe2)
# temp = []
# for i in range(4):
#     temp.extend(create_pipe())
# for i in range(2,7,2):
#     #  temp[i].centerx = temp[i+1].centerx   
#      temp[i].centerx = 200*i
#      temp[i+1].centerx = 200*i

# for i in temp:
#     pipe_list.append(i)
# move_pipes(pipe_list)
# draw_pipes(pipe_list)


floor_x_pos = 0
game_active = True
# piper(pipe_list)
sco = 0
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_active and (event.key == pygame.K_SPACE or event.key==pygame.K_UP):
                # rocket_movement = 0
                rocket_movement -= 22 # background_x_pos -= 1
            if game_active == False and (event.key == pygame.K_SPACE or event.key==pygame.K_UP):
                # rocket_movement = 0
                rocket_rect.center = (100,330)
                rocket_movement = 100
                pipe_list.clear()
                sco = 0
                game_active = True
        if event.type == SPAWNPIPE and game_active:    
            pipe_list.extend(create_pipe())
            sco += 3 
        # if event.type == CHECKSCORE and game_active and len(pipe_list) > 0:    
        #     if rocket_rect.centerx == pipe_list[-1].centerx:
        #         score += 1  
    # piper(pipe_list)
                # pipes = pipe_list.copy()
     
    screen.blit(background, (background_x_pos,0))
    
    game_active = check_collision(pipe_list)  
    font = pygame.font.SysFont(None, 24) 
     
    img = font.render(f'{sco}', True, (0,0,255)) 
    if game_active:
    # for i in range(10):
    #     screen.blit(background, (background_x_pos + 1289*i,0))
        # gravity += 0.01
        
        
        rocket_movement += gravity
        rocket_rect.centery = rocket_movement
        screen.blit(rocket, rocket_rect) 
        screen.blit(img, (20, 20))
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        game_floor()
        if floor_x_pos <= -1289:
            floor_x_pos = 0        

    else:
        score = 0
        pygame.display.set_mode((1289,800))
        screen.blit(message, (background_x_pos,0))

    floor_x_pos -= 1
    # #check for collision



    
    pygame.display.update()
    clock.tick(250)