import pygame
from pygame.locals import *
from . import cfg
import itertools
import random
from .sprites import Tile, Player


player1 = Player(color=(255, 255, 255))
player2 = Player(color=(0, 0, 255))

tiles = {}
for x, y in itertools.product(range(0, cfg.board_size), range(0, cfg.board_size)):
    tiles[x, y] = Tile(x=x, y=y, color=random.choice(cfg.themes))



keyboard_inputs = {
    K_ESCAPE: (pygame.quit, ),
    K_UP: (player1.move, 0, -1),
    K_DOWN: (player1.move, 0, 1),
    K_LEFT: (player1.move, -1, 0),
    K_RIGHT: (player1.move, 1, 0),
    K_RSHIFT: (player1.bomb, tiles),
}

# Our main loop!
pygame.init()
screen = pygame.display.set_mode(cfg.screen_resolution)
while True:
    # for loop through the event queue
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            try:
                action, *args = keyboard_inputs[event.key]
                action(*args)
            except KeyError:
                pass
        elif event.type == QUIT:
            pygame.quit()

    # Draw the player to the screen
    screen.fill((0, 0, 0))

    for tile in tiles.values():
        tile.draw(screen)
    player1.draw(screen)

    pygame.display.flip()
