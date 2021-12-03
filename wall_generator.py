import sys
import random
import numpy as np
import pygame
import matplotlib.pyplot as plt

#Initialize the pygame module
pygame.init()
#Create window
disp_width, disp_height = 900,700
disp = pygame.display.set_mode((disp_width, disp_height),)
clock = pygame.time.Clock()
pygame.time.wait(3000)
isLeftPressed = False
isRightPressed = False
isKeyPressed = False
accessPoints = []

def distanceStart(wifi_pos, access_pos):
    distance = np.linalg.norm(wifi_pos - access_pos)
    return distance

def routerPlacement(screen,background, pressedEnter = False ):
    """
    randomly place a rectangle on the screen
    :param screen:
    :type screen:
    :return:
    :rtype:
    """
    distance_list = []
    pos_list = []
    min_distance = np.inf
    list_wifi = []
    iteration_list = []
    closeFound = False
    # background = pygame.Surface((disp_width, disp_height))
    count = 0
    while True:
        count += 1
        # if distance >
        x, y = random.randrange(disp_width), random.randrange(disp_height)
        distance = 0
        for a in accessPoints:
            distance += distanceStart(np.array((x, y)), np.array(a))
            # print(distanceStart(np.array((x, y)), np.array(a)))
        if distance < min_distance:
            distance_list.append((x, y))
            pos_list.append(distance)
            iteration_list.append(count)
            min_distance = distance
            closeFound=True

        # distance_list.append(min_distance)

        list_wifi.append((x, y))
        screen.blit(background, (0, 0))
        # background.blit(screen,(0,0))
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 5, 5), 0)
        # wifiRect = pygame.Rect(x,y, 5,5)
        # screen.blit(screen, x, y)
        # pygame.display.update()
        pygame.time.wait(100)
        # pygame.draw.rect(screen, (0, 0, 0),(*list_wifi.pop(), 5, 5),0)
        # if closeFound :
        #     pygame.draw.rect(screen, (128, 0, 128), (x,y, 5,5),0)
        #     pygame.display.update()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pressedEnter = True
            if event.type == pygame.QUIT:
                pygame.quit()
        if pressedEnter:
            return (pos_list, iteration_list)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            isLeftPressed = False
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                isLeftPressed = True
            if pygame.mouse.get_pressed()[2]:
                isRightPressed = True
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(disp, (0, 0, 255), (pos[0], pos[1], 10, 10), 0)
                # add this position to the accesspoints list
                accessPoints.append(pos)
            pos = pygame.mouse.get_pos()
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION and isLeftPressed:
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(disp, (255, 0, 0), (pos[0], pos[1], 10, 10), 0)
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            isKeyPressed = True

    if isKeyPressed:

        background = pygame.Surface((disp_width, disp_height))
        background.blit(disp, (0, 0))
        pygame.display.flip()
        (X,Y) = routerPlacement(disp, background, False)
        X1, Y1 = 0,0
        X_centroid, Y_centroid = 0,0
        X2, Y2 = 0,0
        for ind, access in enumerate(accessPoints):
            X2 += access[0] - X1
            Y2 += access[1] - Y1
        X_centroid = X2/len(accessPoints)
        Y_centroid = Y2/len(accessPoints)
        small_distance = 0
        for access in accessPoints:
            small_distance += distanceStart(np.array((X_centroid, Y_centroid)), np.array((access)))
        plt.plot(Y, X)
        plt.axhline(y=small_distance, color='r', linestyle='-')
        plt.xlabel('iterations')
        plt.ylabel('distance')
        plt.show()
        isKeyPressed = False

    # pygame.display.flip()


