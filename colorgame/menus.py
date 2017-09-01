import pygame
from . import utils
from pygame.locals import *


class WinMessage:

    continue_button = K_SPACE
    exit = K_ESCAPE


    def __init__(self):
        """This function gets called once, just to create the text (but not display it)."""
        pygame.font.init()
        self.myfont = pygame.font.SysFont('TimesNewRoman', 30)
        self.winner = 'I do not know'
    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        #textsurface = self.myfont.render('Congratulations! You found each other!', False, (0, 0, 0))
        text="Congratulations, {}! You Won! \n \nTo play again press the Space Button \n \nIf you want to exit the game, Press ESC".format(self.winner)
        screen.fill((75,166,193))
        utils.blit_text(screen, text, (99,250), self.myfont)

        return



class StartGame:

    #continue_button = K_SPACE
    easy_mode=K_1
    normal_mode=K_2
    hard_mode=K_3



    def __init__(self):
        """This function gets called once, just to create the text (but not display it)."""
        pygame.font.init()
        self.myfont = pygame.font.SysFont('TimesNewRoman', 25)

    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        text = "Welcome to the Game! \n \nTo start the game please press the following buttons \n \n-To play an Easy Mode Press 1 \n \n-To Play a Normal Mode Press 2 \n \n-To Play a Hard Mode Press 3"
        #textsurface = self.myfont.render("This is Start Screen \nPress the Space Button to start", False, (0, 0, 0))
        screen.fill((75,166,193))
        utils.blit_text(screen, text, (99,150), self.myfont)
        return


class GameText:
    continue_button = K_SPACE
    def __init__(self):
        """This function gets called once, just to create the text (but not display it)."""
        pygame.font.init()
        self.myfont = pygame.font.SysFont('TimesNewRoman', 25)

    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        text = "How to Play the Game!? \n \n-To move up - Press the Up or W Button \n \n-To move down - Press the Down  or S Button \n \n-To move left - Press the Left or A Button \n \n-To move right - Press the Right or D Button \n \nReady to Start? \nLet's Go! Press the Space Button!"
        screen.fill((75,166,193))
        utils.blit_text(screen, text, (30,30), self.myfont)

        return


