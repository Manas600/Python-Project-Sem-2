import pygame
from pygame import mixer
import random
import math


pygame.init()


# Creating screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("TakeOnMe.wav")
mixer.music.play(-1)




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

def isCollison(EnemyX,EnemyY,missileX,missileY):
    distance = math.sqrt((math.pow(EnemyX-missileX,2)) + (math.pow(EnemyY-missileY,2)))
    if distance < 27:
        return True
    else:
        return False


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

    # Player movement
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736 

    #Enemy Movement
    for i in range(num_of_enemies):

        #Game Over 
            if EnemyY[i] > 440:
                for j in range(num_of_enemies):
                    EnemyY[j] = 2000
               
                break
            
            EnemyX[i] += EnemyX_change[i]
            if EnemyX[i] <= 0:
                EnemyX_change[i] = 0.3
                EnemyY[i] += EnemyY_change[i]
            elif EnemyX[i] >= 736:
                EnemyX_change[i] = -0.3
                EnemyY[i] += EnemyY_change[i]




        #Collision
            Collision = isCollison(EnemyX[i],EnemyY[i],missileX,missileY)
            if Collision:
                Explosion_sound = mixer.Sound('explosion.wav')
                Explosion_sound.play()
                missileY = 480
                missile_state = "Ready"
                
                EnemyX[i] = random.randint(0,735)
                EnemyY[i] = random.randint(50,150)

                Enemy(EnemyX[i],EnemyY[i],i)

    #missile movement
    if missileY<=0:
        missileY=480
        missile_state="ready"
    if missile_state is "fire":
        fire_missile(missileX,missileY)
        missileY-=missileY_change


  


























pygame.display.update()                