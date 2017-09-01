import pygame
from pygame.locals import *
import cfg
import itertools
import random

class Player(pygame.sprite.Sprite):

    def __init__(self, color=(255, 255, 255), x=0, y=0):
        super(Player, self).__init__()
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
        r, g, b = value
        self.__color = pygame.Color(r, b, g)
        self.surf.fill(self.__color)

    @property
    def x(self):
        return int(self.rect.x / (cfg.screen_resolution[0] / cfg.board_size))

    @x.setter
    def x(self, value):
        self.rect.x = int(value * cfg.screen_resolution[0] / cfg.board_size)

    @property
    def y(self):
        return int(self.rect.y / (cfg.screen_resolution[0] / cfg.board_size))

    @y.setter
    def y(self, value):
        self.rect.y = int(value * cfg.screen_resolution[0] / cfg.board_size)

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


player = Player(color=(255, 255, 255))

tiles = {}
for x, y in itertools.product(range(0, cfg.board_size), range(0, cfg.board_size)):
    tiles[x, y] = Player(x=x, y=y, color=random.choice(cfg.themes[0]))



keyboard_inputs = {
    K_ESCAPE: (pygame.quit, ),
    K_UP: (player.move, 0, -1),
    K_DOWN: (player.move, 0, 1),
    K_LEFT: (player.move, -1, 0),
    K_RIGHT: (player.move, 1, 0),
}

# Our main loop!
pygame.init()
screen = pygame.display.set_mode(cfg.screen_resolution)
while True:
    # for loop through the event queue
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            action, *args = keyboard_inputs[event.key]
            action(*args)
            print(player.x, player.y)
        elif event.type == QUIT:
            pygame.quit()

    # Draw the player to the screen
    screen.fill((0, 0, 0))

    for tile in tiles.values():
        tile.draw(screen)
    player.draw(screen)

    pygame.display.flip()
