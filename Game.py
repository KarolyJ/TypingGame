import pygame

pygame.init()

# Basic parameters for the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The typing game")

# Importing the image
bg_image = pygame.image.load("background_img.jpg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 30


def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing the image at position (0, 0)
        screen.blit(bg_image, (0, 0))
        pygame.display.update()
        clock.tick(FPS)


# The main function
if __name__ == "__main__":
    main()
    pygame.quit()
