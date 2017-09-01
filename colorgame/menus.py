import pygame
import utils, cfg
from pygame.locals import *
import sys


class WinMessage:

    continue_button = K_SPACE
    exit = K_ESCAPE

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('TimesNewRoman', 30)
        self.winner = 'I do not know'

    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        #textsurface = self.myfont.render('Congratulations! You found each other!', False, (0, 0, 0))
        text="Congratulations, {}! You Won! \n \nTo play again press the Space Button \n \nIf you want to exit the game, Press ESC".format(self.winner)
        screen.fill((75,166,193))
        utils.blit_text(screen, text, (99,250), self.font)

    def run(self, screen):
        while True:
            self.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == self.continue_button:
                        return

                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()



class StartGame:

    easy_mode=K_1
    normal_mode=K_2
    hard_mode=K_3

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('TimesNewRoman', 25)

    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        text = "Welcome to the Game! \n \nTo start the game please press the following buttons \n \n-To play an Easy Mode Press 1 \n \n-To Play a Normal Mode Press 2 \n \n-To Play a Hard Mode Press 3"
        #textsurface = self.font.render("This is Start Screen \nPress the Space Button to start", False, (0, 0, 0))
        screen.fill((75,166,193))
        utils.blit_text(screen, text, (99,150), self.font)
        return

    def run(self, screen):
        while True:
            self.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == self.easy_mode:
                        cfg.ai_players = 3
                        cfg.ai_move_probability = 1
                        return
                    if event.key == self.normal_mode:
                        cfg.ai_players = 7
                        cfg.ai_move_probability = 5
                        return
                    if event.key == self.hard_mode:
                        cfg.ai_players = 15
                        cfg.ai_move_probability = 10
                        return
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()


class GameText:

    continue_button = K_SPACE

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('TimesNewRoman', 25)

    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        text = "How to Play the Game!? \n \n-To move up - Press the Up or W Button \n \n-To move down - Press the Down  or S Button \n \n-To move left - Press the Left or A Button \n \n-To move right - Press the Right or D Button \n \nReady to Start? \nLet's Go! Press the Space Button!"
        screen.fill((75,166,193))
        utils.blit_text(screen, text, (30,30), self.font)

    def run(self, screen):
        while True:
            self.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==KEYUP:
                    if event.key ==self.continue_button:
                        return
                    if event.key==K_ESCAPE:
                        pygame.quit()
                        sys.exit()





