import pygame
import os
pygame.font.init()

colors: dict = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "dark_red": (164, 0, 0),
    "blue": (0, 0, 255),
    "dark_blue": (0, 0, 164),
    "cyan": (0, 255, 255),
    "lime": (0, 255, 0),
    "green": (0, 164, 0),
    "dark_green": (0, 64, 0),
    "grey": (120, 120, 120),
    "gray": (120, 120, 120),
    "yellow": (255, 255, 0)
}

class image:
    def __init__(self, osl: list, rotation: int, scale: tuple, rect: pygame.Rect):
        try:
            self.img = pygame.image.load(os.path.join(osl[0], osl[1], osl[2]))
        except:
            self.img = pygame.image.load(os.path.join(osl[0], osl[1]))
        pos = [rect.x, rect.y]
        rect.center
        self.rotation = rotation
        self.scale = scale
        self.pos = pos
        self.image = pygame.transform.rotate(pygame.transform.scale(self.img, scale), rotation)
        self.rect = rect
    def update(self):
        self.image = pygame.transform.rotate(pygame.transform.scale(self.img, self.scale), self.rotation)
        self.pos = (self.rect.x, self.rect.y)
    def m_up(self, amount: int):
        self.pos[1] -= amount
    def m_down(self, amount: int):
        self.pos[1] += amount
    def m_right(self, amount: int):
        self.pos[0] += amount
    def m_left(self, amount: int):
        self.pos[0] -= amount
    def __str__(self):
        return f"image: {self.img} scale: {self.scale}"
class Text:
    def __init__(self, size: int, text: str, position: tuple, font: str, color="black"):
        if font == "0":
            font2 = pygame.font.Font(None, size)
        else:
            font2 = pygame.font.SysFont(font, size)
        text2 = font2.render(text, True, colors.get(color))
        rect = text2.get_rect()
        rect.center = position
        self.pos = (rect.x, rect.y)
        self.image = text2
        self.font = font
        self.text = text
        self.color = color
        self.rect = rect
        self.textt = text
    def __str__(self):
        return f"text: {self.text} rect: {self.text_rect} font: {self.font} color: {self.color}"