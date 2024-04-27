import pygame
import time

pygame.init()

#load images
water = pygame.image.load("Assets/water.png")
water = pygame.transform.scale(water, (400, 400))
ship = pygame.image.load("Assets/ship.png")
ship = pygame.transform.scale(ship, (100, 60))
rick = pygame.image.load("Assets/rick.png")
goblin = pygame.image.load("Assets/goblin.png")
ground = pygame.image.load("Assets/ground.png")
ground = pygame.transform.scale(ground, (400, 400))
goblinSecret = pygame.image.load("Assets/creepy.png")

#set values
shipX = 300
goblinSize = 100
effectSize = 50

#setup
pygame.mixer.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Shipwrecked - Ending")
pygame.display.set_icon(ship)
clock = pygame.time.Clock()
pygame.mixer_music.load("Assets/cursedrickroll.mp3")

def loop(ending):
    global shipX
    global effectSize
    global goblinSize
    global rick
    global goblin
    #main loop
    run = True
    while run:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #render sprites
        if ending == 1:
            screen.blit(water, (0, 0))
            screen.blit(ship, (shipX, 130))
            shipX -= 1
            if shipX <= 50:
                run = False      
        elif ending == 2:
            screen.blit(ground, (0, 0))
            pygame.mixer_music.play(1)
            goblin = pygame.transform.scale(goblin, (goblinSize, goblinSize))
            if goblinSize <= 1:
                effectSize += 10
                thingfromspaceNew = pygame.transform.scale(rick, (effectSize, effectSize))
                screen.blit(thingfromspaceNew, (50 - effectSize / 4, 50 - effectSize / 4))
            elif goblinSize >= 2:
                goblinSize -= 1
                screen.blit(goblin, (50 - goblinSize / 4, 100 - goblinSize / 4))
                
            if effectSize >= 600:
                run = False
        elif ending == 3:
            screen.blit(ground, (0, 0))
            screen.blit(goblinSecret, (100, 150))
            pygame.display.update()
            time.sleep(5)
            run = False
        pygame.display.flip()
    pygame.quit()