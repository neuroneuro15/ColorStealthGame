import sys
import itertools
import random
import pygame
from pygame.locals import *
from sprites import Player, Tile
import cfg, utils
from contextlib import contextmanager

pygame.font.init()

CONTINUE_EVENT = USEREVENT + 100
continue_event = pygame.event.Event(CONTINUE_EVENT)


class Scene:

    bg_color = (122, 122, 122)


    def __init__(self, *args, **kwargs):
        super(Scene, self).__init__(*args, **kwargs)

    @contextmanager
    def prep_screen(self, screen):
        screen.fill(self.bg_color)
        yield
        pygame.display.flip()

    def draw(self, screen):
        with self.prep_screen(screen):
            pass

    def update(self, screen):
        pass

    def run(self, screen):
        while True:
            # for loop through the event queue
            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))
                    else:
                        try:
                            action, *args = self.keyboard_inputs[event.key]
                            action(*args)
                        except KeyError:
                            pass
                elif event.type == CONTINUE_EVENT:
                    print("Continue detected.")
                    return
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.update(screen)

            self.draw(screen)



class GameScene(Scene):

    bg_color = (0, 200, 0)

    def __init__(self, *args, **kwargs):
        super(GameScene, self).__init__(*args, **kwargs)
        self.player1 = Player(color=(255, 255, 255))
        self.player2 = Player(color=(0, 0, 0))

        self.tiles = {}
        for x, y in itertools.product(range(0, cfg.board_size), range(0, cfg.board_size)):
            self.tiles[x, y] = Tile(x=x, y=y, color=random.choice(cfg.themes))

        self.keyboard_inputs = {
            K_ESCAPE: (pygame.quit,),
            K_UP: (self.player1.move, 0, -1),
            K_DOWN: (self.player1.move, 0, 1),
            K_LEFT: (self.player1.move, -1, 0),
            K_RIGHT: (self.player1.move, 1, 0),
            K_RSHIFT: (self.player1.bomb, self.tiles, self.player2),
            K_w: (self.player2.move, 0, -1),
            K_s: (self.player2.move, 0, 1),
            K_a: (self.player2.move, -1, 0),
            K_d: (self.player2.move, 1, 0),
            K_LSHIFT: (self.player2.bomb, self.tiles, self.player1),
        }

    def draw(self, screen):
        with self.prep_screen(screen):
            for tile in self.tiles.values():
                tile.draw(screen)
            self.player1.draw(screen)
            self.player2.draw(screen)

    def update(self, screen):
        for num, player in enumerate([self.player1, self.player2]):
            if player.check_if_won():
                print('posting continue event...')
                pygame.event.post(continue_event)
                return


class WinMessage(Scene):

    bg_color = (75,166,193)

    def __init__(self, *args, **kwargs):
        super(WinMessage, self).__init__(*args, **kwargs)

        self.font = pygame.font.SysFont('TimesNewRoman', 30)
        self.text = """
        Congratulations, {}! You Won!

        To play again press the Space Button

        If you want to exit the game, Press ESC
        """

        self.winner = 'I do not know'

        self.keyboard_inputs = {K_SPACE: (pygame.event.post, continue_event)}

    def draw(self, screen):
        with self.prep_screen(screen):
            utils.blit_text(screen, self.text.format(self.winner), (99, 250), self.font)


class StartGame(Scene):

    SET_DIFFICULTY = USEREVENT + 1
    bg_color = (75,166,193)

    def __init__(self, *args, **kwargs):
        super(StartGame, self).__init__(*args, **kwargs)
        self.font = pygame.font.SysFont('TimesNewRoman', 25)
        self.text = """
        Welcome to the Game!

        To start the game please press the following buttons

        -To play an Easy Mode Press 1

        -To Play a Normal Mode Press 2

        -To Play a Hard Mode Press 3
        """

        self.keyboard_inputs = {
            K_1: (self.set_difficulty, 3, 1),
            K_2: (self.set_difficulty, 7, 3),
            K_3: (self.set_difficulty, 7, 5),
            K_ESCAPE: (pygame.event.post, pygame.event.Event(QUIT))
        }

    def draw(self, screen):
        with self.prep_screen(screen):
            utils.blit_text(screen, self.text, (99,150), self.font)

    def set_difficulty(self, ai_players, move_prob):
        print('Setting difficulty: ', ai_players, move_prob)
        cfg.ai_players = ai_players
        cfg.ai_move_probability = move_prob
        pygame.event.post(continue_event)



class GameText(Scene):

    bg_color = (75,166,193)

    def __init__(self):
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

        self.keyboard_inputs = {
            K_SPACE: (pygame.event.post, continue_event)
        }

    def draw(self, screen):
        with self.prep_screen(screen):
            utils.blit_text(screen, self.text, (30,30), self.font)






