import random

import pygame
from Word import Word

pygame.init()

my_font = pygame.font.SysFont("arialunicode", 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Basic parameters for the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The typing game")

# Importing the image
bg_image = pygame.image.load("background_img.jpg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Importing words from the txt file
file = open("words.txt", "r")
data = file.readlines()

# reload rate for the words
word_reload = 20

clock = pygame.time.Clock()
FPS = 30


# Define main function
def main():
    running = True

    # Create Sprite group
    sprites = pygame.sprite.Group()
    word_reload_counter = word_reload

    while running:
        # if word_reload_counter is not zero then subtract one
        # so go through the refreshes *word_reload* times then create a sprite
        if word_reload_counter:
            word_reload_counter -= 1
        else:
            word = Word(data[random.randint(0, len(data)-1)], GREEN, 5)
            sprites.add(word)
            word_reload_counter = word_reload
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw sprites only if there are events
        sprites.update()
        screen.blit(bg_image, (0, 0))  # Draw background image
        sprites.draw(screen)  # Draw words
        pygame.display.update()
        clock.tick(FPS)


# The main function
if __name__ == "__main__":
    print(data[0])
    main()
    pygame.quit()
