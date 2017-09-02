import pygame
import utils, cfg
from pygame.locals import *
import sys


class WinMessage:

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('TimesNewRoman', 30)
        self.text = """
        Congratulations, {}! You Won!

        To play again press the Space Button

        If you want to exit the game, Press ESC
        """
        self.winner = 'I do not know'

    def draw(self, screen):
        screen.fill((75,166,193))
        utils.blit_text(screen, self.text.format(self.winner), (99,250), self.font)
        pygame.display.flip()

    def run(self, screen):

        while True:
            self.draw(screen)

            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        return

                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()



class StartGame:

    SET_DIFFICULTY = USEREVENT + 1

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('TimesNewRoman', 25)
        self.text = """
        Welcome to the Game!

        To start the game please press the following buttons

        -To play an Easy Mode Press 1

        -To Play a Normal Mode Press 2

        -To Play a Hard Mode Press 3
        """

    def draw(self, screen):
        screen.fill((75,166,193))
        utils.blit_text(screen, self.text, (99,150), self.font)
        pygame.display.flip()

    def set_difficulty(self, ai_players, move_prob):
        cfg.ai_players = ai_players
        cfg.ai_move_probability = move_prob

    def run(self, screen):
        while True:
            self.draw(screen)

            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_1:
                        pygame.event.post(pygame.event.Event(self.SET_DIFFICULTY, callback=self.set_difficulty, args=(3, 1)))
                    if event.key == K_2:
                        pygame.event.post(pygame.event.Event(self.SET_DIFFICULTY, callback=self.set_difficulty, args=(7, 3)))
                    if event.key == K_3:
                        pygame.event.post(pygame.event.Event(self.SET_DIFFICULTY, callback=self.set_difficulty, args=(7, 5)))
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == self.SET_DIFFICULTY:
                    event.callback(*event.args)
                    return


class GameText:

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('TimesNewRoman', 25)
        self.text = """
        How to Play the Game!?

        -To move up - Press the Up or W Button

        -To move down - Press the Down  or S Button

        -To move left - Press the Left or A Button

        -To move right - Press the Right or D Button

         Ready to Start?
         Let's Go! Press the Space Button!
         """

    def draw(self, screen):
        screen.fill((75,166,193))
        utils.blit_text(screen, self.text, (30,30), self.font)
        pygame.display.flip()

    def run(self, screen):
        while True:
            self.draw(screen)
            for event in pygame.event.get():
                if event.type==KEYUP:
                    if event.key == K_SPACE:
                        return
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()





