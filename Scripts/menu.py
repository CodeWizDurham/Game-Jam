import pygame

pygame.init()

water = pygame.image.load("Assets/water.png")
water = pygame.transform.scale(water, (400, 400))

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Shipwrecked - Main Menu")
pygame.display.set_icon(water)

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
        
        font = pygame.font.SysFont("calibri", 40)
        mainText = font.render("Shipwrecked", 1, (255, 255, 255))
        screen.blit(mainText, (25, 100))
        
        spaceText = font.render("Space to start.", 1, (255, 255, 255))
        screen.blit(spaceText, (25, 250))
        
        pygame.display.update()