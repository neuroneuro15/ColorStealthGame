import pygame
import cfg
import menus
import scenes


def main():
    # Our main loop!
    pygame.init()
    screen = pygame.display.set_mode(cfg.screen_resolution)

    while True:
        win_screen = menus.WinMessage()
        start_screen = menus.StartGame()
        start_screen.run(screen)
        instruction_screen = menus.GameText()
        instruction_screen.run(screen)
        game = scenes.GameScene()
        game.run(screen)
        win_screen.run(screen)




if __name__ == '__main__':
    main()