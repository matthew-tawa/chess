import pygame
import pygame.freetype
import Constants
import Config
import Board
import Board_States

import pieces

# initializations
def main():
    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((Config.WINDOW_SIZE_X, Config.WINDOW_SIZE_Y))
    pygame.display.set_caption("chess")

    # creating the font
    font = pygame.freetype.Font('font\Roboto-Regular.ttf', 24)

    # creating the Board
    b = Board.Board()
    b.apply_Board_state(Board_States.DEFAULT_STATE)
    #b.Board[Board.Tiles.A1] = pieces.Rook("A1", Constants.Color.PALE)
    #b.Board[Board.Tiles.B1] = pieces.Knight("B1", Constants.Color.PALE)

    # game loop
    running = True
    while running:

        # printing the Board
        screen.fill(Config.COLOR_WINDOW_BACKGROUND)
        b.print(screen, font)
                
                



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
        case Config.KEY_CYCLE_PAWNS:
            pass
        case Config.KEY_CYCLE_KNIGHT:
            pass
        case Config.KEY_CYCLE_BISHOP:
            pass
        case Config.KEY_CYCLE_ROOK:
            pass
        case Config.KEY_CYCLE_QUEEN:
            pass
        case Config.KEY_CYCLE_KING:
            pass
        case Config.KEY_FLIP_Board:
            pass

    





main()
pygame.quit()