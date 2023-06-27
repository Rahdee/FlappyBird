import pygame
import random
from pygame.locals import *

pygame.init()
screen_width = 288
screen_height = 512
window = pygame.display.set_mode((screen_width,screen_height))
fps = pygame.time.Clock()

# Declare variables
BACKGROUND = pygame.image.load("media/background.png").convert_alpha()
BASE = pygame.image.load("media/base.png").convert_alpha()
BOTTOM_PIPE = pygame.image.load("media/pipe.png").convert_alpha()
TOP_PIPE = pygame.transform.flip(BOTTOM_PIPE, False, True)
BIRD =pygame.image.load("media/flappybird-animation.png").convert_alpha()
pipe_height = 320
pipe_width = 52
pipe_gap = 100
pipe_speed = 10

finished = False
flap = False
pipe = [200, 100] # X location of both pipes . Y location of top of gap
bird = [50, 250]
bird_anime_count = 0
jump = 0

#Main game LookupError
while not finished:
    #Process keyboard and mouse events
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    finished = True
                    if  event.key == K_SPACE:
                        flap = True
            if event.type ==  MOUSEBUTTONDOWN:
                flap = True


        #game logic
        if flap:
            jump = 18
            flap = False
        bird[1] -= jump
        if jump > -12:
            jump -= 2
        pipe[0] -= pipe_speed
        if pipe[0] < -pipe_width:
            pipe[0] = screen_width
            pipe[1] = random.randint(50, screen_height-150)
            pipe_gap = random.randint(100,200)

        #draw graphics
        window.fill((0,0,0))
        window.blit(BACKGROUND, (0,0))
        #Base
        window.blit(BASE , (0,400))
        #Pipes
        window.blit(TOP_PIPE, (pipe[0], pipe[1]-pipe_height))
        window.blit(BOTTOM_PIPE, (pipe[0], pipe[1]+pipe_gap))
        #FlappyBird
        window.blit(BIRD, bird, (0,bird_anime_count*24,34,24))
        bird_anime_count = (bird_anime_count + 1) % 3

        pygame.display.update()
        fps.tick(25)

#Loop over , game over
pygame.quit()