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
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()
    )
    game_images['flappybird'] = pygame.image.load(player).convert_alpha()
    game_images['sea_level'] = pygame.image.load(foreground).convert_alpha()
    game_images['background'] = pygame.image.load(background).convert_alpha()
    game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(pipe)
                                                        .convert_alpha(),
                                                        180),
                                pygame.image.load(pipe).convert_alpha())

    print("WELCOME TO THE FLAPPY BIRD GAME")
    print("Press space or enter to start the game")