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

clock = pygame.time.Clock()
FPS = 30

text = my_font.render("asd", True, WHITE)


# Define main function
def main():
    running = True

    # Create Sprite group
    words = pygame.sprite.Group()
    word1 = Word(data[4], 5, WHITE, 10, 10, 10, screen)
    words.add(word1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing the image at position (0, 0)
        # screen.blit(bg_image, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

        words.draw(screen)
        # screen.blit(text, (0, 0))

        # pygame.time.set_timer(pygame.event.Event(), 2000, 5)


# The main function
if __name__ == "__main__":
    print(data[0])
    main()
    pygame.quit()
