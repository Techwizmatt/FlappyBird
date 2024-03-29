import pygame
import random
import numpy as np

def getHitPoints(x,y,width,height):
    xLoc = list(range((int(x) - int(width / 2)), (int(x) + int(width / 2))))
    yLoc = list(range((int(y) - int(height / 2)), (int(y) + int(height / 2))))

    HitPoints = []

    for x1 in xLoc:
        for y1 in yLoc:
            HitPoints.append([x1, y1])

    return HitPoints


def common_data(list1, list2):
    result = False

    # traverse in the 1st list
    for x in list1:

        # traverse in the 2nd list
        for y in list2:

            # if one common
            if x == y:
                result = True
                return result

    return result

def start():
    screenWidth = 480
    screenHeight = 640

    pygame.init()

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('Flappy Bird')

    # Background
    backgroundHeight = 480
    backgroundWidth = 580

    background = pygame.image.load('assets/background.png').convert()
    background = pygame.transform.scale(background, (backgroundHeight, backgroundWidth))

    # Ground
    groundWidth = 25
    groundHeight = 80

    ground = pygame.image.load('assets/ground.png').convert()
    ground = pygame.transform.scale(ground, (groundWidth, groundHeight))

    # Pipes

    pipeWidth = 100
    pipeHeight = 700

    pipe = pygame.image.load('assets/pipe.png').convert_alpha()
    pipe = pygame.transform.scale(pipe, (pipeWidth, pipeHeight))

    rPipe = pygame.transform.rotate(pipe, 180)

    # Bird

    birdArray = [pygame.image.load('assets/bird0.png').convert_alpha(),
                 pygame.image.load('assets/bird1.png').convert_alpha(),
                 pygame.image.load('assets/bird2.png').convert_alpha()]

    birdWidth = 70
    birdHeight = 50
    birdX = (screenWidth / 2) - birdWidth
    birdY = (screenHeight / 2) - birdHeight
    birdFlap = 0
    birdRotation = 0

    birdSpriteRect = pygame.Rect(0, 0, 0, 0)

    running = True  # Wether or not the game should be open or closed.
    started = False  # Wether or not the player is playing the game.
    pipeDisplacment = 200  # The height the bird has to fit within the pipe.
    pipeDistance = 300  # The width between the pipes within the surface.
    frameRate = 60  # Also known as FPS.
    movingSpeed = 3  # How many ticks (milliseconds) should pass before the next movement of the screen. (pipes, ground)

    pipesPlacement = []
    pipesHeight = []

    for i in range(0, 10000):
        pipesPlacement.append(screenWidth)
        pipesHeight.append((random.randint(300, 500)))

    xPos = 0;
    xPipePos = 0

    clock = pygame.time.Clock()

    while running:

        screen.blit(background, (0, 0))  # Paint the background to the surface (canvas) at the X0, Y0 pos.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if started:
                    print("Jump up")
                else:
                    print("Jump up and start the game")
                    started = True

        # screen.blit(birdArray[birdFlap],(0,0))

        # The game has started so we can start the creation of the pipes.

        if started:

            # Pipes
            pipeCreation = (pipeDistance / movingSpeed) * movingSpeed

            pipeNumber = int(xPipePos / pipeCreation)

            xPipePos = xPipePos + movingSpeed

            min = pipeNumber - 5

            if min < 0:
                min = 0

            for i in range(min, pipeNumber):
                # Screen generation

                tempBottomPipe = pipe
                tempTopPipe = rPipe

                x = pipesPlacement[i]
                pipesPlacement[i] = pipesPlacement[i] - movingSpeed

                screen.blit(tempBottomPipe, (x, pipesHeight[i]))
                screen.blit(tempTopPipe, (x, (pipesHeight[i] - pipeHeight) - pipeDisplacment))

                # Hit Detection

                # birdLocList = getHitPoints(birdX, birdY, birdWidth, birdHeight)
                #
                # bottomPipeLocList = getHitPoints(x,pipesHeight[i], pipeWidth, pipeHeight)
                # topPipeLocList = getHitPoints(x,((pipesHeight[i] - pipeHeight) - pipeDisplacment),pipeWidth,pipeHeight)
                #
                # if common_data(birdLocList,topPipeLocList):
                #     print("HITTT!!")

                print(tempTopPipe.get_rect())
                print(birdSprite.get_rect())

                #ISSUES UGGHH



        # Ground
        for i in range(int(xPos / groundWidth), int((screenWidth / groundWidth) + xPos)):
            screen.blit(ground, ((i * groundWidth) - xPos, screenHeight - groundHeight))

        # Bird

        if xPos % 4 == 0:
            birdFlap = birdFlap + 1

            if birdFlap >= 3:
                birdFlap = 0

        birdSprite = pygame.transform.rotate(pygame.transform.scale(birdArray[birdFlap], (birdWidth, birdHeight)),
                                             birdRotation)

        birdSpriteRect = birdSprite.get_rect()

        screen.blit(birdSprite, (birdX, birdY))

        xPos = xPos + movingSpeed
        # Update the display (canvas or surface)
        pygame.display.update()

        # Set the frame rate of the game
        clock.tick(frameRate)

start()