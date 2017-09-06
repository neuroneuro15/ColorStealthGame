import pygame
import cfg
import scenes


def main():
    # Our main loop!
    pygame.init()
    screen = pygame.display.set_mode(cfg.screen_resolution)

    while True:
        win_screen = scenes.WinMessage()
        start_screen = scenes.StartGame()
        start_screen.run(screen)
        # instruction_screen = scenes.GameText()
        # instruction_screen.run(screen)
        game = scenes.GameScene()
        game.run(screen)
        win_screen.run(screen)


if __name__ == '__main__':
    main()