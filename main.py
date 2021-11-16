import random
import sys
import pygame
from pygame.locals import *

#bird = pygame.image.load(flappy bird.png).convert()
player = 'gallery/images/flappy bird.png'
background = 'gallery/images/background.jpeg'
pipe = 'gallery/images/pipe.png'


fps = 64
screen_width = 289
screen_height = 511
screen = pygame.display.set_mode((screen_width, screen_height))
ground_y = screen_height*0.8
game_images = {}
game_sounds = {}