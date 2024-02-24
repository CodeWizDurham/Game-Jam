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

pygame.mixer.init()
hit_sound = pygame.mixer.Sound("Assets/attack.wav")
pygame.mixer_music.load("Assets/Moonlight Beach.mp3")
pygame.mixer_music.play(1)

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

class hotbarC:
    def __init__(self, hotbar: list):
        self.hotbar = hotbar
    def add_item(self, id: int):
        if id == 1:
            self.hotbar.append(1)
        if id == 2:
            self.hotbar.append(2)

hotbar = hotbarC([])

def main():
    key = pygame.key.get_pressed()
    x = 450
    y = 300
    trees = [pygame.Rect(random.randint(0, 900), random.randint(0, 600), 50, 50), pygame.Rect(random.randint(0, 450), random.randint(0, 300), 50, 50),
             pygame.Rect(random.randint(0, 900), random.randint(0, 600), 50, 50)]

    while True:
        first_active = None
        second_active = None
        third_active = None
        screen.fill("gray")
        PlAYeR = PygE.image(["Assets", "player.png"], 0, (50, 50), pygame.Rect(x - (50 / 2), y - (50 / 2), 50, 50))
        screen.blit(PlAYeR.image, PlAYeR.rect.center)
        E_Button = PygE.image(["Assets", "E.png"], 0, (25, 25), pygame.Rect(0, 0, 25, 25))

        for i in range(0, 3, 1):
            tree = PygE.image(["Assets", "tree.png"], 0, (75, 75), pygame.Rect(trees[i].x, trees[i].y, 75, 75))
            screen.blit(tree.image, (trees[i].x, trees[i].y))

        if PlAYeR.rect.colliderect(trees[0]):
            if trees[0] != 0:
                screen.blit(E_Button.image, (trees[0].x + 25, trees[0].y + 25))
                first_active = True
        if PlAYeR.rect.colliderect(trees[1]):
            if trees[1] != 0:
                screen.blit(E_Button.image, (trees[1].x + 25, trees[1].y + 25))
                second_active = True
        if PlAYeR.rect.colliderect(trees[2]):
            if trees[2] != 0:
                screen.blit(E_Button.image, (trees[2].x + 25, trees[2].y + 25))
                third_active = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_q]:
            player.inventory.open()
        if key[pygame.K_w] and y > 0:
            y -= 0.5
        if key[pygame.K_a] and x > 0:
            x -= 0.5
        if key[pygame.K_d] and x < 900:
            x += 0.5
        if key[pygame.K_s] and y < 600:
            y += 0.5

        if first_active == True:
            if key[pygame.K_e]:
                trees.pop(0)
                trees.insert(0, pygame.Rect(-1000, -1000, 0, 0))
                hit_sound.play()
                hotbar.add_item(1)
        if second_active == True:
            if key[pygame.K_e]:
                trees.pop(1)
                trees.insert(1, pygame.Rect(-1000, -1000, 0, 0))
                hit_sound.play()
                hotbar.add_item(1)
        if third_active == True:
            if key[pygame.K_e]:
                trees.pop(2)
                trees.insert(2, pygame.Rect(-1000, -1000, 0, 0))
                hit_sound.play()
                hotbar.add_item(1)
        pygame.display.update()
        
if __name__ == "__main__":
    main()