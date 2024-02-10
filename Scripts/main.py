import pygame
import random

screen = pygame.display.set_mode((900, 600))
screen.fill("gray")
pygame.display.update()

class player:
    class inventory:
        def open():
                inventory_rect = pygame.Rect(450 - (450 / 2), 300 - (350 / 2), 450, 350)
                inventory_picture_rect = pygame.Rect(230, 130, 650 / 4, 550 / 4)
                pygame.draw.rect(screen, "white", inventory_rect, border_radius=10)
                pygame.draw.rect(screen, "gray", inventory_picture_rect, border_radius=15)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        key2 = pygame.key.get_pressed()
                        if key2[pygame.K_e]:
                            main()
                            break

def main():
    key = pygame.key.get_pressed()
    x = 450
    y = 300
    trees = [pygame.Rect(random.randint(0, 450), random.randint(0, 300), 50, 50), pygame.Rect(random.randint(0, 450), random.randint(0, 300), 50, 50),
             pygame.Rect(random.randint(0, 450), random.randint(0, 300), 50, 50)]

    while True:
        screen.fill("gray")
        player_rect = pygame.Rect(x - (50 / 2), y - (50 / 2), 50, 50)
        pygame.draw.rect(screen, "blue", player_rect, border_radius=20)
        for i in range(0, 3, 1):
            pygame.draw.rect(screen, (0, 150, 0), trees[i])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_e]:
                    player.inventory.open()
                if key[pygame.K_w]:
                    y -= 3
                if key[pygame.K_a]:
                    x -= 3
                if key[pygame.K_d]:
                    x += 3
                if key[pygame.K_s]:
                    y += 3
        pygame.display.update()
        
        

if __name__ == "__main__":
    main()