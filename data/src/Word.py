import random
import pygame
from data.src.config import *

pygame.init()

my_font = pygame.font.SysFont("arialunicode", 20)


# Defining word entities in the game
# Making it inherit the Sprite class
class Word(pygame.sprite.Sprite):
    def __init__(self, value, color, speed):
        # Inheriting the sprite class
        pygame.sprite.Sprite.__init__(self)
        self.value = value
        self.color = color
        self.speed = speed
        # Must need info for the draw method to work
        self.image = my_font.render(self.value, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 800)
        self.rect.y = 0

    def update(self, input_text):
        self.rect.y += self.speed * self.speed / 10


class Button:
    def __init__(self, x, y, width, height, content, fontsize):
        self.font = pygame.font.SysFont("arialunicode", fontsize)
        self.content = content

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(center=(WIDTH / 2, y))

        self.text = self.font.render(self.content, True, WHITE)
        self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            # check if the left click button is pressed
            if pressed[0]:
                return True
            return False
        return False

    def is_clicked_once(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed:
                return True
        return False

