import pygame, sys

pygame.init()

my_font = pygame.font.SysFont("arialunicode", 20)


# Defining word entities in the game
# Making it inherit the Sprite class
class Word(pygame.sprite.Sprite):
    def __init__(self, value, speed, color, posx, posy, width, screen):
        # Inheriting the sprite class
        pygame.sprite.Sprite.__init__(self)
        self.value = value
        self.speed = speed
        self.color = color
        self.posx = posx
        self.posy = posy
        self.width = width
        self.screen = screen
        # Must needed info for the draw method to work
        self.image = my_font.render(self.value, True, self.color)
        self.rect = self.image.get_rect()

    def display(self):
        text = my_font.render(self.value, True, self.color)
        self.screen.blit(text, (self.posx, self.posy))

    def update(self):
        self.posy += self.speed
