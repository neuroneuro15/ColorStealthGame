import pygame
from pygame import locals
from random import randint
import itertools
import cfg



def make_player():
    return {'x': randint(0, cfg.board_size), 'y': randint(0, cfg.board_size)}


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


player_1 = make_player()
player_2 = make_player()


def check_for_win(players, player_moving):
    for p1, p2 in itertools.combinations(players, 2):
        if p1['x'] == p2['x'] and p1['y'] == p2['y']:
            name = 'Player 1' if player_moving == player_1 else 'Player 2'
            print('Contact! {} Wins!'.format(name))




def handle_keys(dt):
    movement_inputs = {
        locals.K_UP: (player_2, 0, -1),
        locals.K_DOWN: (player_2, 0, 1),
        locals.K_LEFT: (player_2, -1, 0),
        locals.K_RIGHT: (player_2, 1, 0),
        locals.K_w: (player_1, 0, -1),
        locals.K_s: (player_1, 0, 1),
        locals.K_a: (player_1, -1, 0),
        locals.K_d: (player_1, 1, 0),
    }



    if event.key == locals.K_ESCAPE:
        pygame.quit()
    else:
        pressed = pygame.key.get_pressed()
        for key, (player, x, y) in movement_inputs.items():
            if pressed[key]:
                move_player(board, player, x, y)
                check_for_win(players=[player_1, player_2],
                              player_moving=player)


def update_game(dt):
    for ai in ai_players:
        move_player(board, ai, randint(-1, 1), randint(-1, 1))



if __name__ == '__main__':

    screen = pygame.display.set_mode(cfg.screen_resolution)
    screen.fill((0, 0, 0))
    px = screen.get_width() // cfg.board_size
    py = screen.get_height() // cfg.board_size

    board = [[pygame.Rect(x * px, y * py, px, py) for x in range(cfg.board_size)] for y in range(cfg.board_size)]

    ai_players = [make_player() for _ in range(cfg.ai_players)]

    blast_board(board)
    clock = pygame.time.Clock()
    while True:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == locals.KEYDOWN:
                handle_keys(dt)

        update_game(dt)
        pygame.display.flip()

