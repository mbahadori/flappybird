import random
import sys
import pygame
from pygame.locals import *

fps = 32
screen_width = 288
screen_height = 560
screen = pygame.display.set_mode((screen_width,screen_height))
ground_y = screen_height*0.8
game_images = {}
player = 'bird/bird.png'
background = 'background/background.png'
pipe = 'pipe/pipe.png'
title = 'title/title.png'
message = 'background/background.png'

def welcomeScreen():
    player_x = int(screen_width/8)
    player_y = int((screen_height - game_images['player'].get_height())/2)
    message_x = int((screen_width - game_images['message'].get_width()) / 2)
    message_y = int(screen_height * 0.2)
    title_x = int((screen_width - game_images['message'].get_width()) / 2)
    title_y = int(screen_height * 0.04)
    base_x = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                screen.blit(game_images['background'], (0, 0))
                screen.blit(game_images['message'], (message_x, message_y))
                screen.blit(game_images['player'], (player_x, player_y))
                screen.blit(game_images['base'], (base_x, ground_y))
                screen.blit(game_images['title'], (title_x, title_y))
                pygame.display.update()
                fps_clock.tick(fps)


def mainGame():
    score = 0
    player_x = int(screen_width / 8)
    player_y = int(screen_height / 2)
    base_x = 0

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    upperPipes = [
        {'x': screen_width + 200, 'y': newPipe1[0]['y']},
        {'x': screen_width + (screen_width / 2) + 200, 'y': newPipe2[0]['y']}
    ]

    lowerPipes = [
        {'x': screen_width + 200, 'y': newPipe1[1]['y']},
        {'x': screen_width + (screen_width / 2) + 200, 'y': newPipe2[1]['y']}
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapVel = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if player_y > 0:
                    playerVelY = playerFlapVel
                    playerFlapped = True

        crashTest = isCollide(player_x, player_y, upperPipes, lowerPipes)
        if crashTest:
            return

        playerMidPos = player_x + game_images['player'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + game_images['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                print(f"Your Score is {score}")

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = game_images['player'].get_height()
        player_y = player_y + min(playerVelY, ground_y - player_y - playerHeight)

        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        if 0 < upperPipes[0]['x'] < 5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        if upperPipes[0]['x'] < -game_images['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        screen.blit(game_images['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            screen.blit(game_images['pipe'][0], (upperPipe['x'], upperPipe['y']))
            screen.blit(game_images['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        screen.blit(game_images['base'], (base_x, ground_y))
        screen.blit(game_images['player'], (player_x, player_y))

        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += game_images['numbers'][digit].get_width()
        Xoffset = (screen_width - width) / 2

        for digit in myDigits:
            screen.blit(game_images['numbers'][digit], (Xoffset, screen_height * 0.12))
            Xoffset += game_images['numbers'][digit].get_width()
        pygame.display.update()
        fps_clock.tick(fps)


def isCollide(player_x, player_y, upperPipes, lowerPipes):
    if player_y > ground_y - 25 or player_y < 0:
        return True

    for pipe in upperPipes:
        pipeHeight = game_images['pipe'][0].get_height()
        if (player_y < pipeHeight + pipe['y']) and (
                abs(player_x - pipe['x']) < game_images['pipe'][0].get_width() - 15):
            return True

    for pipe in lowerPipes:
        if (player_y + game_images['player'].get_height() > pipe['y']) and (
                abs(player_x - pipe['x']) < game_images['pipe'][0].get_width() - 15):
            return True

    return False


def getRandomPipe():
    pipeHeight = game_images['pipe'][0].get_height()
    offset = screen_height / 2
    y2 = offset + random.randrange(0, int(screen_height - game_images['base'].get_height() - 1.2 * offset))
    pipeX = screen_width + 20
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe

if __name__ == "__main__":
    pygame.init()
    fps_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    game_images['numbers'] = (
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
    game_images['base'] = pygame.image.load('base/ground.png').convert_alpha()
    game_images['message'] = pygame.image.load('background/background.png').convert_alpha()
    game_images['pipe'] = (
        pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(), 180),
        pygame.image.load(pipe).convert_alpha()
    )
    game_images['title'] = pygame.image.load(title).convert_alpha()
    game_images['background'] = pygame.image.load(background).convert_alpha()
    game_images['player'] = pygame.image.load(player).convert_alpha()

    while True:
        welcomeScreen()
        mainGame()