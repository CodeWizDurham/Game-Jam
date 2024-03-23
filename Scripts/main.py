import pygame
import random
import PygE
import start
import fight
pygame.font.init()

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

class hotbarC:
    def __init__(self, hotbar: list):
        self.hotbar = hotbar
    def add_item(self, id: int):
            self.hotbar.append(id)
    def add_screen(self):
            rect1 = pygame.Rect(100, 525, 50, 50)
            rect2 = pygame.Rect(200, 525, 50, 50)
            rect3 = pygame.Rect(200 + 100, 525, 50, 50)
            rect4 = pygame.Rect(200 + 200, 525, 50, 50)
            rect5 = pygame.Rect(200 + 300, 525, 50, 50)
            for i in range(len(self.hotbar)):
                rect_to_use = rect1
                if i + 1 == 2:
                    rect_to_use = rect2
                elif i + 1 == 3:
                    rect_to_use = rect3
                elif i + 1 == 4:
                    rect_to_use = rect4
                elif i + 1 == 5:
                    rect_to_use = rect5
                pickaxeImage = pygame.image.load("Assets/pickaxe.png")
                pickaxeImage = pygame.transform.scale(pickaxeImage, (50, 50))
                woodImg = pygame.image.load("Assets/wood.png")
                woodImg = pygame.transform.scale(woodImg, (50, 50))
                if self.hotbar[i] == 1:
                        screen.blit(woodImg, rect_to_use)
                stoneImg = pygame.image.load("Assets/stone.png")
                stoneImg = pygame.transform.scale(stoneImg, (50, 50))
                if self.hotbar[i] == 2:
                    screen.blit(stoneImg, rect_to_use)
                if self.hotbar[i] == 4:
                    screen.blit(pickaxeImage, rect_to_use)


hotbar = hotbarC([])
clock = pygame.time.Clock()

def crafting():
    pickaxe_text = PygE.Text(30, "1. Pickaxe: 3 Wood, 2 Sticks", (450, 200), "Arial")
    sword_text = PygE.Text(30, "2. Sword: 2 Stone, 1 Stick", (450, 350), "Arial")
    stick_text = PygE.Text(30, "3. Stick: 1 Wood", (450, 500), "Arial")
    screen.fill("gray")
    screen.blit(pickaxe_text.image, pickaxe_text.pos)
    screen.blit(sword_text.image, sword_text.pos)
    screen.blit(stick_text.image, stick_text.pos)

    items = [0, 0, 0]

    key5 = pygame.key.get_pressed()

    try:
        for q in range(len(hotbar)):
            if hotbar[q] == 1:
                items[0] += 1
            if hotbar[q] == 2:
                items[1] += 1
            if hotbar[q] == 3:
                items[2] += 1
    except:
        None

    if key5[pygame.K_1]:
        if items[0] >= 3 and items[1] >= 2:
            hotbar.add_item(4)
            for z in range(3):
                if hotbar[len(hotbar) - 1] == 1:
                    hotbar.pop(len(hotbar) - 1)
            for x in range(2):
                if hotbar[len(hotbar) - 1] == 3:
                    hotbar.pop(len(hotbar) - 1)

    for event in pygame.event.get():
        key3 = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            quit()
        if key3[pygame.K_q]:
            return False
                

def main():
    key = pygame.key.get_pressed()
    x = 450
    y = 300
    trees = [pygame.Rect(random.randint(0, 900), random.randint(0, 600), 50, 50), pygame.Rect(random.randint(0, 450), random.randint(0, 300), 50, 50),
             pygame.Rect(random.randint(0, 900), random.randint(0, 600), 50, 50), pygame.Rect(random.randint(0, 900), random.randint(0, 600), 50, 50),
             pygame.Rect(random.randint(0, 900), random.randint(0, 600), 50, 50), pygame.Rect(random.randint(0, 900), random.randint(0, 600), 50, 50)]
    groundImg = pygame.image.load("Assets/ground.png")
    groundImg = pygame.transform.scale(groundImg, (900, 600))
    E_Button = PygE.image(["Assets", "E.png"], 0, (25, 25), pygame.Rect(0, 0, 25, 25))
    door = PygE.image(["Assets", "door.png"], 0, (100, 100), pygame.Rect(800, 300, 100, 100))
    run = True
    speed = 1

    while run == True:
        clock.tick(60)
        first_active = None
        second_active = None
        third_active = None
        fourth_active = None
        fifth_active = None
        sixth_active = None
        seventh_active = None
        screen.fill("gray")
        screen.blit(groundImg, (0, 0))
        PlAYeR = PygE.image(["Assets", "player.png"], 0, (50, 50), pygame.Rect(x - (50 / 2), y - (50 / 2), 50, 50))
        screen.blit(PlAYeR.image, PlAYeR.rect.center)
        hotbar.add_screen()
        global open1
        open1 = False

        for i in range(0, 6, 1):
            tree = PygE.image(["Assets", "tree.png"], 0, (75, 75), pygame.Rect(trees[i].x, trees[i].y, 75, 75))
            if i == 2 or i == 3 or i == 5:
                stone = PygE.image(["Assets", "cave.png"], 0, (75, 75), pygame.Rect(trees[i].x, trees[i].y, 75, 75))
                screen.blit(stone.image, (trees[i].x, trees[i].y))
            else:
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
        if PlAYeR.rect.colliderect(trees[3]):
            if trees[3] != 0:
                screen.blit(E_Button.image, (trees[3].x + 25, trees[3].y + 25))
                fourth_active = True
        if PlAYeR.rect.colliderect(trees[4]):
            if trees[4] != 0:
                screen.blit(E_Button.image, (trees[4].x + 25, trees[4].y + 25))
                sixth_active = True
        if PlAYeR.rect.colliderect(trees[5]):
            if trees[5] != 0:
                screen.blit(E_Button.image, (trees[5].x + 25, trees[5].y + 25))
                seventh_active = True
        
        screen.blit(door.image, door.rect.center)
        if PlAYeR.rect.colliderect(door.rect):
            screen.blit(E_Button.image, (door.rect.x + 25, door.rect.y + 75))
            fifth_active = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_q]:
            open1 = not open1
        if key[pygame.K_LSHIFT]:
            speed = 2
        else:
            speed = 1
        if key[pygame.K_w] and y > 0:
            y -= speed
        if key[pygame.K_a] and x > 0:
            x -= speed
        if key[pygame.K_d] and x < 900:
            x += speed
        if key[pygame.K_s] and y < 600:
            y += speed

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
        if fourth_active == True:
            if key[pygame.K_e]:
                trees.pop(3)
                trees.insert(3, pygame.Rect(-1000, -1000, 0, 0))
                hit_sound.play()
                hotbar.add_item(2)
        if sixth_active == True:
            if key[pygame.K_e]:
                trees.pop(4)
                trees.insert(4, pygame.Rect(-1000, -1000, 0, 0))
                hit_sound.play()
                hotbar.add_item(2)
        if seventh_active == True:
           if key[pygame.K_e]:
               trees.pop(5)
               trees.insert(4, pygame.Rect(-1000, -1000, 0, 0))
               hit_sound.play()
               hotbar.add_item(2)
        if fifth_active == True:
            if key[pygame.K_e]:
                run = False
                pygame.mixer_music.stop()
                pygame.display.set_mode((350, 300))
                pygame.display.set_caption("Shipwrecked - Battle")
                fight.loop()

        if open1 == True:
            open1 = crafting()

        pygame.display.update()
        
if __name__ == "__main__":
    main()