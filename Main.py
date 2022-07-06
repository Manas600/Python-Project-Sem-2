import pygame
import random


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

#Enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 4
for i in range(num_of_enemies) :
    EnemyImg.append(pygame.image.load('Enemy.png'))
    EnemyX.append(random.randint(0,735))
    EnemyY.append(random.randint(50,150))
    EnemyX_change.append(1)
    EnemyY_change.append(40)

#ready-you can't see the missile on screen
#fire-the missile is currently moving
#missile
missileImg = pygame.image.load("missile.png")
missileX=0
missileY=480
missileX_change=0
missileY_change=5
missile_state="ready"

def player(x,y):
    screen.blit(playerImg,(x,y))

def Enemy(x,y,i):
    screen.blit(EnemyImg[i],(x,y))

def fire_missile(x,y):
    global missile_state
    missile_state="fire"
    screen.blit(missileImg,(x+16,y+10))


# Game loop
running = True
while running:
    #RGB colors 
    screen.fill((10 ,51, 102))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1x_change = 0.5
                print("Right key is pressed")
            if event.key == pygame.K_LEFT:
                player1x_change = -0.5
                print("Left key is pressed")
               
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player1x_change = 0
                print("Keys have been released")    