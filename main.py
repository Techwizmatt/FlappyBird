import pygame
from random import randint


pygame.init()

screenWidth = 480
screenHeight = 640

screen = pygame.display.set_mode((480, 640))
pygame.display.set_caption('Flappy Bird')

#Background
backgroundHeight = 480
backgroundWidth = 580

background = pygame.image.load('assets/background.png').convert()
background = pygame.transform.scale(background, (backgroundHeight, backgroundWidth))

screen.blit(background, (0,0)) #Paint the background to the surface (canvas) at the X0, Y0 pos.
pygame.display.flip() #Update the surface

#Ground
groundWidth = 25
groundHeight = 80

ground = pygame.image.load('assets/ground.png').convert()
ground = pygame.transform.scale(ground, (groundWidth, groundHeight))

#Pipes

pipeWidth = 100
pipeHeight = 700

pipe = pygame.image.load('assets/pipe.png').convert()
pipe = pygame.transform.scale(pipe, (pipeWidth, pipeHeight))

rPipe = pygame.transform.rotate(pipe, 180)

running = True # Wether or not the game should be open or closed.
started = False # Wether or not the player is playing the game.
pipeHeight = 100 # The height the bird has to fit within the pipe.
pipeDistance = 300 # The width between the pipes within the surface.
frameRate = 60 # Also known as FPS.
movingSpeed = 3 # How many ticks (milliseconds) should pass before the next movement of the screen. (pipes, ground)

xPos = 0;
xPipePos = 0

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if started:
                print("Jump up")
            else:
                print("Jump up and start the game")
                started = True

    for i in range(int(xPos / groundWidth), int((screenWidth / groundWidth) + xPos)):
        screen.blit(ground, ((i * groundWidth) - xPos, screenHeight - groundHeight))

    # The game has started so we can start the creation of the pipes.
    if started:

        pipes = []

        for i in range(0, 100):
            pipes.append(pipe)

        pipeCreation = (pipeDistance / movingSpeed) * movingSpeed

        pipeNumber = (xPipePos / pipeCreation)

        xPipePos = xPipePos + movingSpeed

        for i in range(0,int(pipeNumber)):
            screen.blit(pipes[i], (xPipePos, 0))


    xPos = xPos + movingSpeed
    # Update the display (canvas or surface)
    pygame.display.flip()

    # Set the frame rate of the game
    clock.tick(frameRate)



