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

# input rectangle
input_rect = pygame.Rect(300, 450, 140, 32)

clock = pygame.time.Clock()
FPS = 30


# Define main function
def main():
    running = True

    # Create Sprite group
    sprites = pygame.sprite.Group()
    word_reload_counter = word_reload

    user_text = ""

    while running:
        # if word_reload_counter is not zero then subtract one
        # so go through the refreshes *word_reload* times then create a sprite
        if word_reload_counter:
            word_reload_counter -= 1
        else:
            word = Word(data[random.randint(0, len(data)-1)].strip(), GREEN, 5, user_text)
            print(word.inputText)
            sprites.add(word)
            word_reload_counter = word_reload
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                # check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

        text_surface = my_font.render(user_text, True, WHITE)
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        # Update and draw sprites only if there are events
        sprites.update()
        screen.blit(bg_image, (0, 0))  # Draw background image
        sprites.draw(screen)  # Draw words

        # draw the input rectangle
        pygame.draw.rect(screen, GREEN, input_rect)
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()
        clock.tick(FPS)


# The main function
if __name__ == "__main__":
    main()
    pygame.quit()
