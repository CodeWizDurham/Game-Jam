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
pygame.mixer_music.load("Assets/background.mp3")
#pygame.mixer_music.play(1)
music = pygame.mixer.Sound("Assets/background.mp3")
music.set_volume(0.01)

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
            rect6 = pygame.Rect(200 + 400, 525, 50, 50)
            rect7 = pygame.Rect(200 + 500, 525, 50, 50)
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
                elif i + 1 == 6:
                    rect_to_use = rect6
                elif i + 1 == 7:
                    rect_to_use = rect7
                pickaxeImage = pygame.image.load("Assets/pickaxe.png")
                pickaxeImage = pygame.transform.scale(pickaxeImage, (50, 50))
                swordImage = pygame.image.load("Assets/sword.png")
                swordImage = pygame.transform.scale(swordImage, (50, 50))
                woodImg = pygame.image.load("Assets/wood.png")
                woodImg = pygame.transform.scale(woodImg, (50, 50))
                if self.hotbar[i] == 1:
                        screen.blit(woodImg, rect_to_use)
                stoneImg = pygame.image.load("Assets/stone.png")
                stoneImg = pygame.transform.scale(stoneImg, (50, 50))
                if self.hotbar[i] == 2:
                    screen.blit(stoneImg, rect_to_use)
                if self.hotbar[i] == 3:
                    screen.blit(swordImage, rect_to_use)
                if self.hotbar[i] == 4:
                    screen.blit(pickaxeImage, rect_to_use)


hotbar = hotbarC([])
clock = pygame.time.Clock()
pick = False
sword = False
creep = 1

def crafting():
    pickaxe_text = PygE.Text(30, "1. Pickaxe: 4 Wood", (450, 200), "Arial")
    sword_text = PygE.Text(30, "2. Sword: 2 Stone, 1 Wood", (450, 350), "Arial")
    screen.fill("gray")
    screen.blit(pickaxe_text.image, pickaxe_text.pos)
    screen.blit(sword_text.image, sword_text.pos)

    items = [0, 0]

    key5 = pygame.key.get_pressed()
    hotber = hotbar.hotbar
    if len(hotber) != 0:
        for q in range(len(hotber)):
            if hotber[q] == 1:
                items[0] += 1
            if hotber[q] == 2:
                items[1] += 1
    
    for i in range(len(hotber)):
        if hotber[i] == 4:
            global pick
            pick = True
        if hotber[i] == 3:
            global sword
            sword = True

    if key5[pygame.K_1]:
        if items[0] >= 4 and not pick:
            hotbar.add_item(4)
            woodAmount = 0
            while woodAmount < 4:
                for z in range(len(hotber)):
                    if hotber[z - iteration] == 1:
                        hotber.pop(0)
                        woodAmount += 1
                        iteration += 1
    if key5[pygame.K_2]:
        if items[0] >= 1 and not sword and items[1] >= 2:
            hotbar.add_item(3)
            woodAmount = 0
            stoneAmount = 0
            iteration = 0
            while stoneAmount < 2:
                for x in range(len(hotber)):
                    if hotber[x - iteration] == 2:
                        hotber.pop(0)
                        stoneAmount += 1
                        iteration += 1
            while woodAmount < 1:
                for z in range(len(hotber)):
                    if hotber[z - iteration] == 1:
                        hotber.pop(0)
                        woodAmount += 1
                        iteration += 1

    if key5[pygame.K_0]:
        global creep
        creep = 2

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
    trees = [pygame.Rect(random.randint(0, 775), random.randint(0, 475), 50, 50), pygame.Rect(random.randint(0, 775), random.randint(0, 475), 50, 50),
             pygame.Rect(random.randint(0, 775), random.randint(0, 475), 50, 50), pygame.Rect(random.randint(0, 775), random.randint(0, 475), 50, 50),
             pygame.Rect(random.randint(0, 775), random.randint(0, 475), 50, 50), pygame.Rect(random.randint(0, 775), random.randint(0, 475), 50, 50),
             pygame.Rect(random.randint(0, 775), random.randint(0, 475), 50, 50)]
    groundImg = pygame.image.load("Assets/ground.png")
    groundImg = pygame.transform.scale(groundImg, (900, 600))
    E_Button = PygE.image(["Assets", "E.png"], 0, (25, 25), pygame.Rect(0, 0, 25, 25))
    door = PygE.image(["Assets", "door.png"], 0, (100, 100), pygame.Rect(800, -100, 100, 100))
    run = True
    speed = 1
    music.play(1)

    while run == True:
        clock.tick(60)
        first_active = None
        second_active = None
        third_active = None
        fourth_active = None
        fifth_active = None
        sixth_active = None
        seventh_active = None
        eighth_active  = None
        screen.fill("gray")
        screen.blit(groundImg, (0, 0))
        PlAYeR = PygE.image(["Assets", "player.png"], 0, (50, 50), pygame.Rect(x - (50 / 2), y - (50 / 2), 50, 50))
        screen.blit(PlAYeR.image, PlAYeR.rect.center)
        hotbar.add_screen()
        global open1
        open1 = False

        if creep == 2:
            pygame.mixer.stop()
        
        for i in range(0, 7, 1):
            tree = PygE.image(["Assets", "tree.png"], 0, (75, 75), pygame.Rect(trees[i].x, trees[i].y, 75, 75))
            if i == 5 or i == 6:
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
        if PlAYeR.rect.colliderect(trees[6]):
            if trees[6] != 0:
                screen.blit(E_Button.image, (trees[6].x + 25, trees[6].y + 25))
                eighth_active = True
        
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
            speed = 5
        else:
            speed = 1
        if key[pygame.K_w] and y > 10:
            y -= speed
        if key[pygame.K_a] and x > 10:
            x -= speed
        if key[pygame.K_d] and x < 900:
            x += speed
        if key[pygame.K_s] and y < 475:
            y += speed
        
        yes = False
        yes2 = False
        if len(hotbar.hotbar) >= 1:
            for i in range(len(hotbar.hotbar)):
                if hotbar.hotbar[i] == 4:
                    yes = True
                if hotbar.hotbar[i] == 3:
                    yes2 = True

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
                hotbar.add_item(1)
        if sixth_active == True:
            if key[pygame.K_e]:
                trees.pop(4)
                trees.insert(4, pygame.Rect(-1000, -1000, 0, 0))
                hit_sound.play()
                hotbar.add_item(1)
        if seventh_active == True and yes == True:
           if key[pygame.K_e]:
               trees.pop(5)
               trees.insert(4, pygame.Rect(-1000, -1000, 0, 0))
               hit_sound.play()
               hotbar.add_item(2)
        if eighth_active == True and yes == True:
            if key[pygame.K_e]:
                trees.pop(6)
                trees.insert(5, pygame.Rect(-1000, -1000, 0, 0))
                hit_sound.play()
                hotbar.add_item(2)
        if fifth_active == True and yes2 == True:
            if key[pygame.K_e] and hotbar:
                run = False
                pygame.mixer_music.stop()
                pygame.display.set_mode((350, 300))
                pygame.display.set_caption("Shipwrecked - Battle")
                music.stop()
                fight.loop(creep)

        if open1 == True:
            open1 = crafting()

        pygame.display.update()
        
if __name__ == "__main__":
    main()