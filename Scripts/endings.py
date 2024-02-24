import pygame
import time

pygame.init()

#load images
water = pygame.image.load("Assets/water.png")
water = pygame.transform.scale(water, (400, 400))
ship = pygame.image.load("Assets/ship.png")
ship = pygame.transform.scale(ship, (100, 60))
thingfromspace = pygame.image.load("Assets/blackhole.png")
tree = pygame.image.load("Assets/tree.png")
ground = pygame.image.load("Assets/ground.png")
ground = pygame.transform.scale(ground, (400, 400))

#set values
shipX = 300
treeSize = 100
effectSize = 50

#setup
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Shipwrecked - Ending")
pygame.display.set_icon(ship)
clock = pygame.time.Clock()

def loop(ending):
    global shipX
    global effectSize
    global treeSize
    global thingfromspace
    global tree
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
            tree = pygame.transform.scale(tree, (treeSize, treeSize))
            if treeSize <= 1:
                effectSize += 10
                thingfromspaceNew = pygame.transform.scale(thingfromspace, (effectSize, effectSize))
                screen.blit(thingfromspaceNew, (50 - effectSize / 4, 50 - effectSize / 4))
            elif treeSize >= 2:
                treeSize -= 1
                screen.blit(tree, (50 - treeSize / 4, 100 - treeSize / 4))
                
            if effectSize >= 600:
                run = False
        pygame.display.flip()