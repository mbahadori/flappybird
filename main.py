import random
import sys
import pygame
from pygame.locals import *

#bird = pygame.image.load(flappy bird.png).convert()
player = 'gallery/images/flappy bird.png'
background = 'gallery/images/background.jpeg'
pipe = 'gallery/images/pipe.png'
foreground = '/images/base.png'

fps = 64
screen_width = 289
screen_height = 511
screen = pygame.display.set_mode((screen_width, screen_height))
ground_y = screen_height*0.8
game_images = {}
game_sounds = {}

# game start
if __name__ == "__main__":
    pygame.init() # modules of pygame library
    framepersecond_clock = pygame.time.Clock()

    pygame.display.set_caption('Flappy Bird Game')

    game_images['scoreimages'] = (
        pygame.image.load('0/0.png').convert_alpha(),
        pygame.image.load('1/1.png').convert_alpha(),
        pygame.image.load('2/2.png').convert_alpha(),
        pygame.image.load('3/3.png').convert_alpha(),
        pygame.image.load('4/4.png').convert_alpha(),
        pygame.image.load('5/5.png').convert_alpha(),
        pygame.image.load('6/6.png').convert_alpha(),
        pygame.image.load('7/7.png').convert_alpha(),
        pygame.image.load('8/8.png').convert_alpha(),
        pygame.image.load('9/9.png').convert_alpha()
    )
    game_images['flappybird'] = pygame.image.load(player).convert_alpha()
    game_images['foreground'] = pygame.image.load(foreground).convert_alpha()
    game_images['background'] = pygame.image.load(background).convert_alpha()
    game_images['pipe'] = (pygame.transform.rotate(pygame.image.load(pipe)
                                                        .convert_alpha(),
                                                        180),
                                pygame.image.load(pipe).convert_alpha())

    print("WELCOME TO THE FLAPPY BIRD GAME")
    print("Press space or enter to start the game")

    while True:

        # sets the coordinates of flappy bird
        horizontal = int(screen_width / 5)
        vertical = int((screen_height - game_images['flappybird'].get_height()) / 2)

        # foreground
        ground = 0
        while True:
            for event in pygame.event.get():

                # cross button = close the game
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()

                    # exit game
                    sys.exit()

                    # space or up key = start game
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    flappygame()

                # no keys pressed
                else:
                    screen.blit(game_images['background'], (0, 0))
                    screen.blit(game_images['flappybird'], (horizontal, vertical))
                    screen.blit(game_images['foreground'], (ground, ground_y))

                    # refreshes screen
                    pygame.display.update()

                    # set the rate of frame per second
                    framepersecond_clock.tick(framepersecond)