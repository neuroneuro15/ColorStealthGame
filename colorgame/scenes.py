import itertools
import random
import pygame
from pygame.locals import *
from sprites import Player, Tile
import cfg


class GameScene:

    def __init__(self):
        self.player1 = Player(color=(255, 255, 255), x=random.randint(0, cfg.board_size), y=random.randint(0, cfg.board_size))
        self.player2 = Player(color=(0, 0, 0), x=random.randint(0, cfg.board_size), y=random.randint(0, cfg.board_size))

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
        # Draw the player to the screen
        screen.fill((0, 200, 0))

        for tile in self.tiles.values():
            tile.draw(screen)
        self.player1.draw(screen)
        self.player2.draw(screen)

        pygame.display.flip()

    def run(self, screen):
        while True:
            # for loop through the event queue
            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    try:
                        action, *args = self.keyboard_inputs[event.key]
                        action(*args)
                    except KeyError:
                        pass
                elif event.type == QUIT:
                    pygame.quit()

            for num, player in enumerate([self.player1, self.player2]):
                if player.check_if_won():
                    return

            self.draw(screen)


