import pygame
import time
import menu

pygame.init()

#load images
water = pygame.image.load("Assets/water.png")
water = pygame.transform.scale(water, (400, 400))
ship = pygame.image.load("Assets/ship.png")
ship = pygame.transform.scale(ship, (100, 60))
rock = pygame.image.load("Assets/rock.png")
rock = pygame.transform.scale(rock, (100, 100))
isle = pygame.image.load("Assets/island.png")
isle = pygame.transform.scale(isle, (200, 200))
effect = pygame.image.load("Assets/explode.png")

#set a few values
run = False
shipX = 300
effectSize = 5
try:
    cursed = file = open("Scripts/Save.txt", 'r')
except:
    cursed = None

#end functions
def end():
    pygame.display.update()
    time.sleep(1)
   
#menu 
playing = menu.intro()
if playing:
    run = True
else:
    pygame.quit()

#setup
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Shipwrecked - Begining")
pygame.display.set_icon(ship)
clock = pygame.time.Clock()
if cursed:
    water = pygame.image.load("Assets/blood.png")
    water = pygame.transform.scale(water, (400, 400))

#main loop
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
    #render sprites
    screen.blit(water, (0, 0))
    if shipX >= 140:
        screen.blit(ship, (shipX, 130))
        screen.blit(rock, (0, 100))
    elif shipX <= 100:
        #end game
        screen.blit(isle, (200, 50))
        font = pygame.font.SysFont("Sans", 20, True)
        if not cursed:
            text = font.render("Welcome to the island.", 1, (0, 0, 0))
        else:
            text = font.render("Welcome to the HELL.", 1, (255, 0, 0))
        screen.blit(text, (0, 50))
        pygame.display.update()
        time.sleep(1)
        end()
        run = False
    elif shipX <= 139:
        #explode the boat
        ship = pygame.transform.rotate(ship, 0.1)
        screen.blit(ship, (shipX, 130))
        effect = pygame.image.load("Assets/explode.png")
        effect = pygame.transform.scale(effect, (effectSize, effectSize))
        screen.blit(effect, (shipX - effectSize / 4, effectSize / 50 + 130))
        screen.blit(rock, (0, 100))
        effectSize += 5
        
    shipX -= 1
        
    pygame.display.flip()
            
pygame.quit()