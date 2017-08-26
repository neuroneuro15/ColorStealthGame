import pygame
from pygame.locals import *
from random import randint
import itertools



def move_player(board, player, x, y):

    x_new, y_new = player.x + x, player.y + y
    print('old: ({}, {})\t new: ({}, {})'.format(x, y, x_new, y_new))
    if (0 <= x_new < len(board[0])) and (0 <= y_new < len(board)):
        player.x, player.y = x_new, y_new
        new_tile = board[y_new][x_new]
        color = tuple(randint(0, 255) for _ in range(3))
        pygame.draw.rect(screen, color, new_tile)


def blast_board(board):
    for tile in itertools.chain(*board):
        color = tuple(randint(0, 255) for _ in range(3))
        pygame.draw.rect(screen, color, tile)

class Entity:

    def __init__(self):
        self.x = randint(0, board_size)
        self.y = randint(0, board_size)



if __name__ == '__main__':

    n_colors = 5
    board_size = 15
    screen = pygame.display.set_mode((800, 800))
    px, py = screen.get_width() // board_size, screen.get_height() // board_size
    board = [[pygame.Rect(x * px, y * py, px, py) for x in range(board_size)] for y in range(board_size)]
    #



    # Create Player
    player = Entity()


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
                        print('pressed button')
                        if pressed[pygame.K_UP]:
                            print('Up')
                            move_player(board, player, 0, -1)
                        if pressed[pygame.K_DOWN]:
                            print('Down')
                            move_player(board, player, 0, 1)
                        if pressed[pygame.K_LEFT]:
                            print('Left')
                            move_player(board, player, -1, 0)
                        if pressed[pygame.K_RIGHT]:
                            print('Right')
                            move_player(board, player, 1, 0)
            if done:
                pygame.quit()

            blast_board(board)

            # screen.fill((0, 0, 0))
            # if is_blue: color = (0, 128, 255)
            # else: color = (255, 100, 0)
            # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

            pygame.display.flip()
            clock.tick(60)
