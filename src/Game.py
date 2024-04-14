import random

import pygame
from Word import Word

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


# define main function
class Pane(object):

    def __init__(self):
        pygame.init()
        self.my_font = pygame.font.SysFont("arialunicode", 20)
        # basic parameters for the screen
        self.WIDTH, self.HEIGHT = 900, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("The typing game")
        # importing the image
        self.bg_image = pygame.image.load("background_img.jpg")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.WIDTH, self.HEIGHT))
        # importing words from the txt file
        self.file = open("words.txt", "r")
        self.data = self.file.readlines()
        # reload rate for the words
        self.word_reload = 25
        # input rectangle
        self.input_rect = pygame.Rect(300, 450, 140, 32)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        # Create Sprite group
        self.sprites = pygame.sprite.Group()
        self.word_reload_counter = self.word_reload
        self.running = True


    def main(self):
        user_text = ""
        score = 0
        hp = 5

        while self.running:
            # if the player loses all the hp, then it's game over :(
            if hp < 1:
                self.gameOver()

            # if word_reload_counter is not zero then subtract one
            # so go through the refreshes *word_reload* times then create a sprite
            if self.word_reload_counter:
                self.word_reload_counter -= 1
            else:
                word = Word(self.data[random.randint(0, len(self.data) - 1)].strip(), GREEN, 3)
                self.sprites.add(word)
                self.word_reload_counter = self.word_reload
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    # check for backspace
                    if event.key == pygame.K_BACKSPACE:

                        # get text input from 0 to -1 i.e end.
                        user_text = user_text[:-1]

                    # unicode standard is used for string
                    # formation
                    else:
                        user_text += event.unicode

            text_surface = self.my_font.render(user_text, True, WHITE)
            # set width of textfield so that text cannot get
            # outside of user's text input
            self.input_rect.w = max(100, text_surface.get_width() + 10)

            # iterating through the sprites in the group and if the input text is equal
            # to its value then killing it and resetting the input text
            if len(self.sprites.sprites()) > 0:
                for el in self.sprites.sprites():
                    if user_text == el.value:
                        el.kill()
                        user_text = ""
                        score += len(el.value)
                    # killing the sprite if it hits the floor and the player loses a hp
                    elif el.rect.y > 500:
                        el.kill()
                        hp -= 1

            # update and draw sprites only if there are events
            self.sprites.update()
            self.screen.blit(self.bg_image, (0, 0))  # Draw background image
            self.sprites.draw(self.screen)  # Draw words

            # draw the input rectangle
            pygame.draw.rect(self.screen, GREEN, self.input_rect)
            # render at position stated in arguments
            self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

            # rendering the score text on the screen
            score_text = self.my_font.render("SCORE: " + str(score), True, WHITE)
            score_textRect = score_text.get_rect()
            score_textRect.center = (self.WIDTH - 100, 20)
            self.screen.blit(score_text, score_textRect)

            # rendering the hp of the current game
            hp_text = self.my_font.render("HP: " + str(hp), True, WHITE)
            hp_textRect = hp_text.get_rect()
            hp_textRect.center = (100, 20)
            self.screen.blit(hp_text, hp_textRect)

            pygame.display.flip()
            self.clock.tick(self.FPS)

    def mainFunc(self):
        if __name__ == '__main__':
            self.main()
            pygame.quit()

    def gameOver(self):
        self.screen.fill(WHITE)

        for sprite in self.sprites.sprites():
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()



display = Pane()
display.mainFunc()
