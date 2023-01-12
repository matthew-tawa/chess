import pygame
import pygame_textinput
import Board
import Board_States
import Constants



class Chess():
    def __init__(self, side: Constants.Color) -> None:
        self.board = Board.Board()
        self.side = side

    # set the board up with a specific state
    def init_board(self, state):
        self.board.apply_board_state(state)

    def myturn(self):
        # display that its my turn
        # wait for user to press enter
        # if a piece isnt selected, do nothing
        # if piece is selected display possible moves
        # user chooses a move
        # send

        running = True
        while running:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running = False
                    case pygame.KEYUP:
                        if event.key == pygame.K_RETURN:

                    case _:
                        pass


        pass


