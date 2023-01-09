import pygame
import pygame.freetype
import math
import Constants
import Config
import Board
import Board_States
from Tiles import Tiles

# global variables
b = Board.Board()
cursor = Tiles.NOWHERE
last_selected_piece = ("", Tiles.NOWHERE)



# initializations
def main():
    global b

    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((Config.WINDOW_SIZE_X, Config.WINDOW_SIZE_Y))
    pygame.display.set_caption("chess")

    # creating the font
    font = pygame.freetype.Font('font\Roboto-Regular.ttf', 24)

    # creating the Board
    b.apply_board_state(Board_States.DEFAULT_STATE)

    # game loop
    running = True
    in_game = False
    tick = 0
    while running:

        # printing the Board
        screen.fill(Config.COLOR_WINDOW_BACKGROUND)
        b.print(screen, font)

        if (in_game):

            # drawing the cursor
            if (cursor != Tiles.NOWHERE and tick%1000 in range(0,500)):
                cursor_x = 24 * (cursor.value % 8)
                cursor_y = 24 * math.floor(cursor.value / 8)
                pygame.draw.rect(screen, Config.COLOR_CURSOR, pygame.Rect(cursor_x, cursor_y,24 ,24))

            # call event handlers
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running = False

                    case pygame.KEYUP:
                        handle_keypress(event.key)

                    case _:
                        pass
        else:
            
        
        pygame.display.update()
        tick += 1



# handles when a key is pressed
def handle_keypress(key):
    global b, cursor, last_selected_piece

    # finding the new starting position to look for pieces
    incremented_pos = last_selected_piece[1].value + 8
    start_looking_from = Tiles(incremented_pos) if incremented_pos < 64 else None

    match key:
        case Config.KEY_CYCLE_PAWNS:
            piece_str = "pawn"
            cursor = b.get_next_piece_position(piece_str, Constants.Color.DARK, None if (last_selected_piece[0] != piece_str) else start_looking_from)
            last_selected_piece = (piece_str, cursor)
            print(last_selected_piece)
        case Config.KEY_CYCLE_KNIGHT:
            piece_str = "knight"
            cursor = b.get_next_piece_position(piece_str, Constants.Color.DARK, None if last_selected_piece[0] != piece_str else start_looking_from)
            last_selected_piece = (piece_str, cursor)
            print(last_selected_piece)
        case Config.KEY_CYCLE_BISHOP:
            piece_str = "bishop"
            cursor = b.get_next_piece_position(piece_str, Constants.Color.DARK, None if last_selected_piece[0] != piece_str else start_looking_from)
            last_selected_piece = (piece_str, cursor)
            print(last_selected_piece)
        case Config.KEY_CYCLE_ROOK:
            piece_str = "rook"
            cursor = b.get_next_piece_position(piece_str, Constants.Color.DARK, None if last_selected_piece[0] != piece_str else start_looking_from)
            last_selected_piece = (piece_str, cursor)
            print(last_selected_piece)
        case Config.KEY_CYCLE_QUEEN:
            piece_str = "queen"
            cursor = b.get_next_piece_position(piece_str, Constants.Color.DARK, None if last_selected_piece[0] != piece_str else start_looking_from)
            last_selected_piece = (piece_str, cursor)
            print(last_selected_piece)
        case Config.KEY_CYCLE_KING:
            piece_str = "king"
            cursor = b.get_next_piece_position(piece_str, Constants.Color.DARK, None if last_selected_piece[0] != piece_str else start_looking_from)
            last_selected_piece = (piece_str, cursor)
            print(last_selected_piece)
        case Config.KEY_FLIP_BOARD:
            b.flipped = not b.flipped
        case Config.KEY_SELECT:
            pass
        case Config.KEY_BACK:
            pass

    





main()
pygame.quit()