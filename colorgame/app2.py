import pygame
from pygame.locals import *
from . import cfg
import itertools
import random
from .sprites import Tile, Player
from .menus import WinMessage


# Create Game Objects
win_screen = WinMessage()

player1 = Player(color=(255, 255, 255), x=random.randint(0, cfg.board_size), y=random.randint(0, cfg.board_size))
player2 = Player(color=(0, 0, 0), x=random.randint(0, cfg.board_size), y=random.randint(0, cfg.board_size))

tiles = {}
for x, y in itertools.product(range(0, cfg.board_size), range(0, cfg.board_size)):
    tiles[x, y] = Tile(x=x, y=y, color=random.choice(cfg.themes))


# Configure Inputs
keyboard_inputs = {
    K_ESCAPE: (pygame.quit, ),
    K_UP: (player1.move, 0, -1),
    K_DOWN: (player1.move, 0, 1),
    K_LEFT: (player1.move, -1, 0),
    K_RIGHT: (player1.move, 1, 0),
    K_RSHIFT: (player1.bomb, tiles, player2),
    K_w: (player2.move, 0, -1),
    K_s: (player2.move, 0, 1),
    K_a: (player2.move, -1, 0),
    K_d: (player2.move, 1, 0),
    K_LSHIFT: (player2.bomb, tiles, player1),
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


    for num, player in enumerate([player1, player2]):
        if player.check_if_won():
            win_screen.winner = 'Player {}'.format(num + 1)
            pygame.quit()

    # Draw the player to the screen
    screen.fill((0, 0, 0))

    for tile in tiles.values():
        tile.draw(screen)
    player1.draw(screen)
    player2.draw(screen)

    pygame.display.flip()


