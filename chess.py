import pygame
import config
import board

# initializations
def main():
    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((config.WINDOW_SIZE_X, config.WINDOW_SIZE_Y))
    pygame.display.set_caption("chess")

    # game loop
    game_loop()



# game loop
def game_loop():
    running = True
    while running:

        b = board.Board()

        for row in b.board.items():
            for tile in row[1].items():
                



        # call event handlers
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

                case pygame.KEYUP:
                    handle_keypress(event.key)

                case _:
                    pass
        
        pygame.display.update()



# handles when a key is pressed
def handle_keypress(key):
    match key:
        case config.KEY_CYCLE_PAWNS:
            pass
        case config.KEY_CYCLE_KNIGHT:
            pass
        case config.KEY_CYCLE_BISHOP:
            pass
        case config.KEY_CYCLE_ROOK:
            pass
        case config.KEY_CYCLE_QUEEN:
            pass
        case config.KEY_CYCLE_KING:
            pass
        case config.KEY_FLIP_BOARD:
            pass

    





main()