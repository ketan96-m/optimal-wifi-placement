import sys
import random
import numpy as np
import pygame

#Initialize the pygame module
pygame.init()
#Create window
disp_width, disp_height = 500, 500
disp = pygame.display.set_mode((disp_width, disp_height),)
clock = pygame.time.Clock()
pygame.time.wait(3000)
isLeftPressed = False
isRightPressed = False
isKeyPressed = False

def routerPlacement(screen, pressedEnter = False):
    """
    randomly place a rectangle on the screen
    :param screen:
    :type screen:
    :return:
    :rtype:
    """
    list_wifi = []
    while True:
        x, y = random.randrange(disp_width), random.randrange(disp_height)
        list_wifi.append((x, y))
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 5, 5), 0)
        pygame.display.update()
        pygame.time.wait(30)
        pygame.draw.rect(screen, (0,0,0),(*list_wifi.pop(), 5, 5),0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pressedEnter = True
        if pressedEnter:
            return

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            isLeftPressed = False
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pressed(3))
            if pygame.mouse.get_pressed()[0]:
                isLeftPressed = True
            if pygame.mouse.get_pressed()[2]:
                isRightPressed = True
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(disp, (0, 0, 255), (pos[0], pos[1], 10, 10), 0)
            pos = pygame.mouse.get_pos()
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION and isLeftPressed:
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(disp, (255, 0, 0), (pos[0], pos[1], 10, 10), 0)
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            isKeyPressed = True


    if isKeyPressed:
        routerPlacement(disp, False)
        isKeyPressed = False

    # pygame.display.flip()
