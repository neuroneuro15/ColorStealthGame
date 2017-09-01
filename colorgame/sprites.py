import itertools
import random
import pygame
from . import cfg


class Tile(pygame.sprite.Sprite):

    def __init__(self, color=(255, 255, 255), x=0, y=0, *args, **kwargs):
        super(Tile, self).__init__(*args, **kwargs)
        self.surf = pygame.Surface((cfg.screen_resolution[0] / cfg.board_size,
                                    cfg.screen_resolution[1] / cfg.board_size))
        self.rect = self.surf.get_rect()
        self.color = color

        self.x = x
        self.y = y

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if not isinstance(value, pygame.Color):
            self.__color = value
        else:
            r, g, b = value
            self.__color = pygame.Color(r, b, g)
        self.surf.fill(self.__color)

    def randomize_color(self, from_theme=True):
        if from_theme:
            self.color = random.choice(cfg.themes)  # choose a color from the theme
        else:
            self.color = [random.randint(0, 255) for _ in range(3)]

    @property
    def x(self):
        return int(self.rect.x / (cfg.screen_resolution[0] / cfg.board_size))

    @x.setter
    def x(self, value):
        val = value % cfg.board_size
        self.rect.x = int(val * cfg.screen_resolution[0] / cfg.board_size)

    @property
    def y(self):
        return int(self.rect.y / (cfg.screen_resolution[0] / cfg.board_size))

    @y.setter
    def y(self, value):
        val = value % cfg.board_size
        self.rect.y = int(val * cfg.screen_resolution[0] / cfg.board_size)

    @property
    def xy(self):
        return self.x, self.y

    @xy.setter
    def xy(self, value):
        self.x, self.y = value

    def move(self, x, y):
        self.x += x
        self.y += y

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.surf, (self.rect.x, self.rect.y))


class Player(Tile):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

    def bomb(self, board, target):
        """Changes colors of surrounding tiles, and returns true if target player is on one of the squares."""
        for x, y in itertools.product([-1, 0, 1], [-1, 0, 1]):
            xt, yt = self.x + x, self.y + y
            try:
                tile = board[xt, yt]
                tile.randomize_color()
                if target.xy == (xt, yt):
                    return True
            except KeyError:
                pass

        else:
            return False