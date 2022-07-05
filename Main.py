import pygame



pygame.init()


# Creating screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('background.png')



# Title and icon
pygame.display.set_caption("Galaxy rush")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("arcade-game.png")
playerX=370
playerY=480
playerX_change=0



# Game loop
running = True
while running:
    #RGB colors 
    screen.fill((10 ,51, 102))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False