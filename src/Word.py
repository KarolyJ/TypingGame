import random

import pygame, sys

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
        # Must needed info for the draw method to work
        self.image = my_font.render(self.value, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 800)
        self.rect.y = 0

    def update(self):
        self.rect.y += self.speed * self.speed / 10
