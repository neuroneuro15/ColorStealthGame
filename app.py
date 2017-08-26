import pygame
from pygame.locals import *
from random import randint
import itertools


n_colors = 5
board_size = 15
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))
px, py = screen.get_width() // board_size, screen.get_height() // board_size

board = [[pygame.Rect(x * px, y * py, px, py) for x in range(board_size)] for y in range(board_size)]


def make_player():
    return {'x': randint(0, board_size), 'y': randint(0, board_size)}


n_ai_players = 2
ai_players = [make_player() for _ in range(n_ai_players)]
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
                        if pressed[pygame.K_UP]:
                            move_player(board, player_2, 0, -1)
                        if pressed[pygame.K_DOWN]:
                            move_player(board, player_2, 0, 1)
                        if pressed[pygame.K_LEFT]:
                            move_player(board, player_2, -1, 0)
                        if pressed[pygame.K_RIGHT]:
                            move_player(board, player_2, 1, 0)
                        if pressed[pygame.K_w]:
                            move_player(board, player_1, 0, -1)
                        if pressed[pygame.K_s]:
                            move_player(board, player_1, 0, 1)
                        if pressed[pygame.K_a]:
                            move_player(board, player_1, -1, 0)
                        if pressed[pygame.K_d]:
                            move_player(board, player_1, 1, 0)

            for ai in ai_players:
                move_player(board, ai, randint(-1, 1), randint(-1, 1))

            if done:
                pygame.quit()




            # if is_blue: color = (0, 128, 255)
            # else: color = (255, 100, 0)
            # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

            pygame.display.flip()
            clock.tick(60)
