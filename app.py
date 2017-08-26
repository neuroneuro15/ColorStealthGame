import pygame
from pygame.locals import *
from random import randint
import itertools
import cfg


screen = pygame.display.set_mode(cfg.screen_resolution)
screen.fill((0, 0, 0))
px = screen.get_width() // cfg.board_size
py = screen.get_height() // cfg.board_size

board = [[pygame.Rect(x * px, y * py, px, py) for x in range(cfg.board_size)] for y in range(cfg.board_size)]


def make_player():
    return {'x': randint(0, cfg.board_size), 'y': randint(0, cfg.board_size)}



ai_players = [make_player() for _ in range(cfg.ai_players)]
player_1 = make_player()
player_2 = make_player()

def move_player(board, player, x, y):
    x_new, y_new = player['x'] + x, player['y'] + y
    if (0 <= x_new < len(board[0])) and (0 <= y_new < len(board)):
        player['x'] = x_new
        player['y'] = y_new
        new_tile = board[y_new][x_new]
        color = tuple(randint(0, 255) for _ in range(3))
        pygame.draw.rect(screen, color, new_tile)


def blast_board(board):
    for tile in itertools.chain(*board):
        color = tuple(randint(0, 255) for _ in range(3))
        pygame.draw.rect(screen, color, tile)


movement_inputs = {
    pygame.K_UP: (player_2, 0, -1)),
    pygame.K_DOWN: (player_2, 0, 1)),
    pygame.K_LEFT: (player_2, -1, 0)),
    pygame.K_RIGHT: (player_2, 1, 0)),
    pygame.K_w: (player_1, 0, -1)),
    pygame.K_s: (player_1, 0, 1)),
    pygame.K_a: (player_1, -1, 0)),
    pygame.K_d: (player_1, 1, 0)),
}


if __name__ == '__main__':

    blast_board(board)

    done = False
    clock = pygame.time.Clock()
    while not done:
            for event in pygame.event.get():
                    if event.type == QUIT:
                            done = True
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            done = True
                    if event.type == pygame.KEYDOWN:
                        pressed = pygame.key.get_pressed()
                        for key, (player, x, y) in movement_inputs.items():
                            if pressed[key]:
                                move_player(board, player, x, y)

            for ai in ai_players:
                move_player(board, ai, randint(-1, 1), randint(-1, 1))

            if done:
                pygame.quit()




            # if is_blue: color = (0, 128, 255)
            # else: color = (255, 100, 0)
            # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

            pygame.display.flip()
            clock.tick(60)
