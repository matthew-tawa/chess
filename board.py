import constants
import pieces
import board_states


class Board:
    def __init__(self) -> None:
        # creating board of empty pieces
        self.board = {chr(x+65): {y: pieces.Empty() for y in range(1,constants.BOARD_Y+1)} for x in range(0,constants.BOARD_X)}


    # takes in a board state and sets the board up
    def apply_board_state(state) -> None:
        pass

    # print the board to the screen
    def print() -> None:
        pass



b = Board()
print(b.board["A"][1])
print(b.board["A"][2])
print(b.board["G"][8])
print(b.board["H"][6])