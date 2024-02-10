import pygame
import random
import PygE
import start

screen = pygame.display.set_mode((900, 600))
screen.fill("gray")
pygame.display.set_caption("Shipwrecked - Game Jam")
ship = pygame.image.load("Assets/ship.png")
pygame.display.set_icon(ship)
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
        E_Button = PygE.image(["Assets", "E.png"], 0, (30, 30), pygame.Rect(0, 0, 50, 50))
        for i in range(0, 3, 1):
            pygame.draw.rect(screen, (0, 150, 0), trees[i])
        if player_rect.colliderect(trees[0]):
            screen.blit(E_Button.image, (trees[0].x + 12, trees[0].y + 12))
            first_active = True
        if player_rect.colliderect(trees[1]):
            screen.blit(E_Button.image, (trees[1].x + 12, trees[1].y + 12))
            second_active = True
        if player_rect.colliderect(trees[2]):
            screen.blit(E_Button.image, (trees[2].x + 12, trees[2].y + 12))
            third_active = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            y -= 0.1
        if key[pygame.K_q]:
            player.inventory.open()
        if key[pygame.K_a]:
            x -= 0.1
        if key[pygame.K_d]:
            x += 0.1
        if key[pygame.K_s]:
            y += 0.1
        pygame.display.update()
        
        

if __name__ == "__main__":
    main()