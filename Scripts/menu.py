import pygame
import time

pygame.init()

pygame.mixer.init()

water = pygame.image.load("Assets/water.png")
water = pygame.transform.scale(water, (400, 400))
ship = pygame.image.load("Assets/ship.png")
ship = pygame.transform.scale(ship, (150, 100))

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Shipwrecked - Main Menu")
pygame.display.set_icon(water)
sound = pygame.mixer.Sound("Assets/introsound.mp3")

def mainMenu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            if event.type == pygame.K_SPACE:
                running = False
                return True
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            running = False
            return True
        
        screen.blit(water, (0, 0))
        
        font = pygame.font.SysFont("Sans", 40)
        mainText = font.render("Shipwrecked", 1, (255, 255, 255))
        screen.blit(mainText, (25, 100))
        
        spaceText = font.render("Space to start.", 1, (255, 255, 255))
        screen.blit(spaceText, (25, 250))
        
        pygame.display.update()
        
def intro():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            if event.type == pygame.K_SPACE:
                running = False
                return True

        screen.blit(water, (0, 0))
        screen.blit(ship, (100, 100))
        
        sound.play()
        pygame.display.update()
        time.sleep(5)
        
        playing = mainMenu()
        return playing