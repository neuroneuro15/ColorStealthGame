import pygame
from pygame.locals import *
from random import randint, choice
import itertools
import cfg


class Tile:

    def __init__(self, x, y, px, py, r, g, b):
        self.rect = pygame.Rect(x * px, y * py, px, py)
        self.color = color.Color(r, g, b, a=255)

    def draw(self, screen):
        r, g, b = self.color.r, self.color.g, self.color.b
        pygame.draw.rect(screen, (r, g, b), self.rect)

    def randomize_color(self):
        self.color.r = randint(0, 255)
        self.color.g = randint(0, 255)
        self.color.b = randint(0, 255)

    def randomize_color_from_theme(self, theme):
        r, g, b = choice(theme)  # choose a color from the theme
        self.color.r, self.color.g, self.color.b = r, g, b

    @classmethod
    def from_theme(cls, x, y, px, py, theme):
        r, g, b = choice(theme)  # choose a color from the theme
        return cls(x, y, px, py, r, g, b)

class Player:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    @property
    def xy(self):
        return self.x, self.y


class Game:

    def __init__(self, width, height, theme):
        self.theme = theme

        self.screen = pygame.display.set_mode(cfg.screen_resolution)
        self.screen.fill((100, 0, 0))

        self.clock = pygame.time.Clock()

        self.width = width
        self.height = height
        self.board = self.generate_board()
        self.players = [Player(name='Player 1', x=randint(0, cfg.board_size), y=randint(0, cfg.board_size)),
                        Player(name='Player 2', x=randint(0, cfg.board_size), y=randint(0, cfg.board_size)),]

    def move_player(self, player, dx, dy, dt):
        x, y = player.x + dx, player.y + dy
        if (0 <= x < self.width) and (0 <= y < self.height):
            player.x, player.y = x, y
            new_tile = self.board[y][x]
            new_tile.randomize_color_from_theme(self.theme)
            self.check_for_win(player)

    def check_for_win(self, player_moving):
        for p1, p2 in itertools.combinations(self.players, 2):
            if p1.xy == p2.xy:
                print('Contact! {} Wins!'.format(player_moving.name))

    def draw(self):
        for tile in itertools.chain(*self.board):
            tile.draw(self.screen)
        pygame.display.flip()

    def generate_board(self):
        px = self.screen.get_width() // self.width
        py = self.screen.get_height() // self.height
        return [[Tile.from_theme(x, y, px, py, self.theme) for x in range(self.width)] for y in range(self.height)]

    def handle_keys(self, dt, event):
        movement_inputs = {
            K_UP: (self.players[0], 0, -1),
            K_DOWN: (self.players[0], 0, 1),
            K_LEFT: (self.players[0], -1, 0),
            K_RIGHT: (self.players[0], 1, 0),
            K_w: (self.players[1], 0, -1),
            K_s: (self.players[1], 0, 1),
            K_a: (self.players[1], -1, 0),
            K_d: (self.players[1], 1, 0),
        }

        if event.key == K_ESCAPE:
            pygame.quit()
        else:
            pressed = pygame.key.get_pressed()
            for key, (player, x, y) in movement_inputs.items():
                if pressed[key]:
                    self.move_player(player, x, y, dt)


    def run(self):
        while True:
            dt = self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.handle_keys(dt, event)

            self.draw()



if __name__ == '__main__':

    theme = cfg.themes[0]
    game = Game(width=cfg.board_size, height=cfg.board_size, theme=theme)
    game.run()


