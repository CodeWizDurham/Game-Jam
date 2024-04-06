import pygame
import endings
import random
import time

pygame.init()

#load images
water = pygame.image.load("Assets/water.png")
water = pygame.transform.scale(water, (400, 400))
ship = pygame.image.load("Assets/ship.png")
ship = pygame.transform.scale(ship, (100, 60))
goblin = pygame.image.load("Assets/goblin.png")
attackBtn = pygame.image.load("Assets/fight.png")
attackBtn = pygame.transform.scale(attackBtn, (100, 50))
attackRect = attackBtn.get_rect()
attackRect.center = (200, 200)
plr = pygame.image.load("Assets/player.png")
plr = pygame.transform.scale(plr, (50, 50))
plrRect = plr.get_rect()
plrRect.center = (50, 200)
rock = pygame.image.load("Assets/rock.png")
rock = pygame.transform.scale(rock, (100, 100))
rockRect = rock.get_rect()
rockRect.center = (50, 50)
pygame.font.init()
font = pygame.font.SysFont("Comic Sans", 15, True, False)

#setup
screen = pygame.display.set_mode((350, 300))
pygame.display.set_caption("Shipwrecked - Battle")
pygame.display.set_icon(ship)
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer_music.load("Assets/Captain Scurvy.mp3")
atkSound = pygame.mixer.Sound("Assets/attack.wav")
atkSound.set_volume(25)
rick = pygame.mixer.Sound("Assets/rickrollremakeboot.mp3")
mus = pygame.mixer.Sound("Assets/Captain Scurvy.mp3")
let = pygame.mixer.Sound("Voicy_Let it Go The Remakeboot.mp3")
state = 0
enemyPos = 125
musicOn = False
health = 350
plrHealth = 20
plrX = 50
plrY = 200

def loop():
    global enemyPos
    global state
    global musicOn
    global plrX
    global plrY
    global plrHealth
    global plrRect
    global rockRect
    global health
    
    enemyImg = goblin
    rocks = []
    waiting = 1
    enemyRect = enemyImg.get_rect()
    atkTime = 1
    enemyRot = 0
    enemyImgCopy = enemyImg
    
    #main loop
    run = True
    while run:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #render sprites
        screen.blit(water, (0, 0))
        screen.blit(enemyImgCopy, (enemyPos, 10))
        plrHp = font.render("Your Health: " + str(plrHealth), 1, (50, 255, 50))
        screen.blit(plrHp, (200, 250))
        
        #states
        if state == 0:
            if enemyPos >= 1:
                enemyPos -= 2
            else:
                enemyPos = 0
                state =1
        elif state == 1:
            enemyPos = 0
            screen.blit(attackBtn, (200, 200))
            hp = font.render("Enemy Health: " + str(health), 1, (255, 50, 50))
            screen.blit(hp, (15, 25))
            enemyRot = 0
            enemyImgCopy = enemyImg
        elif state == 2:
            screen.blit(plr, plrRect.center)
            attack = 1
            atkTime += 1
            enemyRot += 5
            enemyImgCopy = pygame.transform.rotate(enemyImg, enemyRot)
            if attack == 1 and atkTime >= 4:
                for i in range(2):
                    tempRect = rockRect
                    tempRect.center = (random.randint(0, 250), random.randint(100, 300))
                    rocks.append(tempRect)
                    atkTime = 1
        
        if state != 0:
            #music
            if musicOn == False:
                mus.play(1)
                musicOn = True
            #pygame.mixer_music.play(1)
        
        #movement
        keys = pygame.key.get_pressed()
        speed = 5
        if keys[pygame.K_w]:
            plrY -= speed
        if keys[pygame.K_s]:
            plrY += speed
        if keys[pygame.K_a]:
            plrX -= speed
        if keys[pygame.K_d]:
            plrX += speed
        plrRect.center = (plrX, plrY)
        
        #rocks
        for i in range(len(rocks)):
            screen.blit(rock, rocks[i].center)
            if plrRect.colliderect(rocks[i]):
                plrHealth -= 2
                atkSound.play(1)
                rocks.clear()
                break
            
        if plrHealth <= 0:
            mus.stop()
            rick.play(1)
            endings.loop(2)
        
        if state == 2:
            waiting += 1
            if waiting >= 15:
                state = 1
                waiting = 1
                
        if health <= 0:
            mus.stop()
            let.play(1)
            endings.loop(1)
        
        mouse = pygame.mouse.get_pos()
        mouse2 = pygame.mouse.get_pressed()
        minPos = (attackRect.center[0], attackRect.center[1])
        maxPos = (attackRect.center[0] * 2, attackRect.center[1] * 2)
        if mouse[0] >= minPos[0] and mouse[0] <= maxPos[0]:
                if mouse[1] >= minPos[1] and mouse[1] <= maxPos[1]:
                    if mouse2[0] and state == 1:
                        print("attack")
                        atkSound.play()
                        state = 2
                        health -= 50
                        enemyPos = 175
                        plrX = 50
                        plrY = 200
        
        pygame.display.flip()