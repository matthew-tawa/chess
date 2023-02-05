import socket
import select
import pygame
import pygame_textinput
import Chess
import Constants
import Board_States
import Display
import Config
import Move


class Client():
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # chess game
        self.chess = Chess.Chess(Constants.Color.DARK)

    # connects to server
    def join_server(self):
        print('Connecting to %s port %s' % (self.ip, self.port))
        self.sock.connect((self.ip, self.port))
        self.sock.setblocking(0)

    # runs the game
    def game_loop(self):
        #self.chess.init_board(Board_States.DEFAULT_STATE)
        #self.chess.init_board(Board_States.CASTLING_STATE)
        self.chess.init_board(Board_States.PROMOTION_STATE)

        textinput = pygame_textinput.TextInputVisualizer(None, Display.font_input, True, Config.COLOR_TEXT, 300, 3, Config.COLOR_TEXT)
        my_move = ""
        opp_move = ""

        my_turn = False
        while True:
            Display.update_display_pre()

            # get events
            events = pygame.event.get()
            textinput.update(events)
            
            # display the board and move list
            self.chess.print()

            # show text input
            Display.blit_to_screen(5, 250, textinput.surface)

            # need to check if user clicked enter
            for event in events:
                if event.type == pygame.QUIT:
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if my_turn and len(textinput.value) >1:
                            my_move = Move.Move(textinput.value, self.chess.my_side)
                            
                            if not my_move.castle_k and not my_move.castle_q:
                                my_move.capture = not self.chess.board.board[my_move.destination].is_empty()

                            textinput.value = ""
                            if self.chess.my_move(my_move):
                                my_move.check = self.chess.opp_king_in_check()
                                #TODO my_move.checkmate = 

                                if my_move.promotion:
                                    pass
                                    #TODO manage promotion

                                self.sock.sendall(str(my_move).encode())
                                my_turn = False


                    if event.key == pygame.K_ESCAPE:
                        textinput.value = ""

            Display.update_display_post()

            try:
                if not my_turn:
                    ready = select.select([self.sock], [], [], 0.1)
                    if ready:
                        opp_move_str = self.sock.recv(1024).decode()
                        if len(opp_move_str) > 0:
                            opp_move = Move.Move(opp_move_str, self.chess.opp_side)
                            self.chess.opp_move(opp_move)

                            if opp_move.promotion:
                                self.chess.promote(opp_move.destination, opp_move.promotion_piece)
                                
                            my_turn = True

                if opp_move == 'forfeit':
                    break

            except Exception as e:
                if e.errno == 10035:
                    pass
                else:
                    print(e)
                    break

        print('Connection closed.')
        self.sock.close()








