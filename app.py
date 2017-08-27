import pygame
from pygame.locals import *
from random import randint, choice
import itertools
import cfg
from colorsys import hls_to_rgb, rgb_to_hls


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
		
		
class WinMessage:

    def __init__(self):
        """This function gets called once, just to create the text (but not display it)."""
        pygame.font.init() 
        self.myfont = pygame.font.SysFont('TimesNewRoman', 30)

    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        textsurface = self.myfont.render('Congratulations! You found each other!', False, (0, 0, 0))
        screen.fill((152, 145, 241))
        screen.blit(textsurface,(99,250))
       
        return


class StartGame:

    continue_button = K_SPACE

    def __init__(self):
        """This function gets called once, just to create the text (but not display it)."""
        pygame.font.init()
        self.myfont = pygame.font.SysFont('TimesNewRoman', 25)

    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        text = "Welcome to the Game! \n \nTo start the game please press the Space Button"
        #textsurface = self.myfont.render("This is Start Screen \nPress the Space Button to start", False, (0, 0, 0))
        screen.fill((75,166,193))
        blit_text(screen, text, (99,250), self.myfont)
        return


class GameText:

    def __init__(self):
        """This function gets called once, just to create the text (but not display it)."""
        pygame.font.init()
        self.myfont = pygame.font.SysFont('TimesNewRoman', 30)

    def draw(self, screen):
        """This is the function that gets called to actually display on the screen."""
        textsurface = self.myfont.render('Congratulations! You found each other!', False, (0, 0, 0))
        screen.blit(textsurface,(99,250))
        return


class Tile:

    def __init__(self, x, y, px, py, r, g, b):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * px, y * py, px, py)
        self.color = color.Color(r, g, b, 50)

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

        self.win_text = WinMessage()

    def move_player(self, player, dx, dy, dt):

        def cycle(val, min, max):
            if val < min:
                return max - (val - min) - 2
            elif val >= max:
                return min + (val - max) + 0
            else:
                return val

        print(player.x + dx, player.y + dy, flush=False)
        x = cycle(player.x + dx, min=0, max=self.width)
        y = cycle(player.y + dy, min=0, max=self.height)
        print(x, y)

        player.x, player.y = x, y
        new_tile = self.board[y][x]
        old_hue = rgb_to_hls(new_tile.color.r, new_tile.color.g, new_tile.color.b)[0]

        while old_hue == rgb_to_hls(new_tile.color.r, new_tile.color.g, new_tile.color.b)[0]:
            new_tile.randomize_color_from_theme(self.theme)
        self.check_for_win(player)

    def check_for_win(self, player_moving):
        for p1, p2 in itertools.combinations(self.players, 2):
            if p1.xy == p2.xy:
                print('Contact! {} Wins!'.format(player_moving.name))

    def draw(self):
        for tile in itertools.chain(*self.board):
            for player in self.players:
                if player.x == tile.x and player.y == tile.y:
                    # if max(tile.color.r, tile.color.g, tile.color.b) < 255 - cfg.brighten_rate:

                    h, l, s = rgb_to_hls(tile.color.r, tile.color.g, tile.color.b)
                    if l > cfg.min_lightness:
                        l += cfg.brighten_rate
                        r, g, b = hls_to_rgb(h, l, s)
                        tile.color.r = int(r)
                        tile.color.g = int(g)
                        tile.color.b = int(b)
            tile.draw(self.screen)
        self.win_text.draw(screen=self.screen)
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
            player, x, y, = movement_inputs[event.key]
            self.move_player(player, x, y, dt)

    def show_start_screen(self):
        start_msg = StartGame()
        while True:
            start_msg.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == start_msg.continue_button:
                        return
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def run(self):

        # First Screen
        self.show_start_screen()

        # GamePlay
        while True:
            dt = self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == KEYUP:
                    self.handle_keys(dt, event)

            self.draw()



if __name__ == '__main__':

    theme = cfg.themes[0]
    game = Game(width=cfg.board_size, height=cfg.board_size, theme=theme)
    game.run()


