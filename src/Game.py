import random
import sys

import pygame
from Word import *
from config import *


class Pane(object):

    def __init__(self):
        pygame.init()
        self.my_font = pygame.font.SysFont("arialunicode", 20)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The typing game")

        # importing the image
        self.bg_image = pygame.image.load("background_img.jpg")
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT))

        # input rectangle
        self.input_rect = pygame.Rect(300, 450, 140, 32)
        self.clock = pygame.time.Clock()
        self.word_reload_counter = word_reload
        self.running = True

    def new(self):
        # a new game starts
        self.playing = True
        self.user_text = ""
        self.score = 0
        self.hp = 5

        # Create Sprite group
        self.sprites = pygame.sprite.Group()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:

                # check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e end.
                    self.user_text = self.user_text[:-1]

                # unicode standard is used for string
                # formation
                else:
                    self.user_text += event.unicode

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))  # Draw background image
        self.sprites.draw(self.screen)  # Draw words

        text_surface = self.my_font.render(self.user_text, True, WHITE)
        # set width of textfield so that text cannot get

        # outside of user's text input
        self.input_rect.w = max(100, text_surface.get_width() + 10)

        # draw the input rectangle
        pygame.draw.rect(self.screen, GREEN, self.input_rect)

        # render at position stated in arguments
        self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

        # rendering the score text on the screen
        score_text = self.my_font.render("SCORE: " + str(self.score), True, WHITE)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (WIDTH - 100, 20)
        self.screen.blit(score_text, score_text_rect)

        # rendering the hp of the current game
        hp_text = self.my_font.render("HP: " + str(self.hp), True, WHITE)
        hp_text_rect = hp_text.get_rect()
        hp_text_rect.center = (100, 20)
        self.screen.blit(hp_text, hp_text_rect)

        self.clock.tick(FPS)
        pygame.display.flip()

    def update(self):
        # game loop updates
        self.sprites.update()
        # if the player loses all the hp, then it's game over :(
        if self.hp < 1:
            self.playing = False

        # if word_reload_counter is not zero then subtract one
        # so go through the refreshes *word_reload* times then create a sprite
        if self.word_reload_counter:
            self.word_reload_counter -= 1
        else:
            word = Word(data[random.randint(0, len(data) - 1)].strip(), GREEN, 3)
            self.sprites.add(word)
            self.word_reload_counter = word_reload

            # iterating through the sprites in the group and if the input text is equal
            # to its value then killing it and resetting the input text
        if len(self.sprites.sprites()) > 0:
            for el in self.sprites.sprites():
                if self.user_text == el.value:
                    el.kill()
                    self.user_text = ""
                    self.score += len(el.value)
                # killing the sprite if it hits the floor and the player loses a hp
                elif el.rect.y > 500:
                    el.kill()
                    self.hp -= 1

    def mainFunc(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def gameOver(self):
        pass
        self.screen.fill(WHITE)
        text = self.my_font.render('Game Over', True, WHITE)
        text_rect = text.get_rect()

        restart_button = Button(10, HEIGHT - 60, 120, 50, "Restart", 32)

        for sprite in self.sprites.sprites():
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

    def introScreen(self):
        intro = True

        title = self.my_font.render("Typing Game",True, WHITE)
        title_rect = title.get_rect(center=(WIDTH/2, 50))

        play_button = Button(0, 150, 100, 50, "Start Game", 20)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.bg_image, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


# THE GAME LOOP
g = Pane()
g.introScreen()
g.new()

while g.running:
    g.mainFunc()
    g.gameOver()

pygame.quit()
sys.exit()
