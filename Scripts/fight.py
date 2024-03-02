import pygame
import endings

pygame.init()

#load images
water = pygame.image.load("Assets/water.png")
water = pygame.transform.scale(water, (400, 400))
ship = pygame.image.load("Assets/ship.png")
ship = pygame.transform.scale(ship, (100, 60))
goblin = pygame.image.load("Assets/goblin.png")
attackBtn = pygame.image.load("Assets/ground.png")
attackBtn = pygame.transform.scale(attackBtn, (100, 50))
attackRect = attackBtn.get_rect()
attackRect.center = (200, 200)

#setup
screen = pygame.display.set_mode((350, 300))
pygame.display.set_caption("Shipwrecked - Battle")
pygame.display.set_icon(ship)
clock = pygame.time.Clock()
pygame.mixer_music.load("Assets/Captain Scurvy.mp3")

def loop(enemyImg):
    pygame.mixer_music.play(1)
    
    #main loop
    run = True
    while run:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #render sprites
        screen.blit(water, (0, 0))
        screen.blit(attackBtn, (200, 200))
        screen.blit(enemyImg, (0, 10))
        
        mouse = pygame.mouse.get_pos()
        mouse2 = pygame.mouse.get_pressed()
        minPos = (attackRect.center[0], attackRect.center[1])
        maxPos = (attackRect.center[0] * 2, attackRect.center[1] * 2)
        if mouse[0] >= minPos[0] and mouse[0] <= maxPos[0]:
                if mouse[1] >= minPos[1] and mouse[1] <= maxPos[1]:
                    if mouse2[0]:
                        print("attack")
        
        pygame.display.flip()
    
loop(goblin)