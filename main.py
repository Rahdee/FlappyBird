import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((288,512))
fps = pygame.time.Clock()

# Declare variables
BACKGROUND = pygame.image.load("media/background.png").convert_alpha()
BASE = pygame.image.load("media/base.png").convert_alpha()
BOTTOM_PIPE = pygame.image.load("media/pipe.png").convert_alpha()
TOP_PIPE = pygame.transform.flip(BOTTOM_PIPE, False, True)
pipe_height = 320
pipe_gap = 100

finished = False
FLAP = False
pipe = [200, 100] # X location of both pipes . Y location of top of gap

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

        #draw graphics
        window.fill((0,0,0))
        window.blit(BACKGROUND, (0,0))
        #Base
        window.blit(BASE , (0,400))
        #Pipes
        window.blit(TOP_PIPE, (pipe[0], pipe[1]-pipe_height))
        window.blit(BOTTOM_PIPE, (pipe[0], pipe[1]+pipe_gap))
        #FlappyBird
        pygame.display.update()
        fps.tick(25)

#Loop over , game over
pygame.quit()