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


class Server():
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # client info (to be populated on connection)
        self.conn = None
        self.addr = None

        # chess game
        self.chess = Chess.Chess(Constants.Color.PALE)

    # opens server and waits for a connection
    def start_server(self):
        print('Starting server on %s, port %s.' % (self.ip, self.port))
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)

        # find connections
        self.conn, self.addr = self.sock.accept()
        self.conn.setblocking(0)
        print('Client with address %s connected.' % self.addr[0])

    # runs the game
    def game_loop(self):
        #self.chess.init_board(Board_States.DEFAULT_STATE)
        #self.chess.init_board(Board_States.CASTLING_STATE)
        self.chess.init_board(Board_States.PROMOTION_STATE)

        textinput = pygame_textinput.TextInputVisualizer(None, Display.font_input, True, Config.COLOR_TEXT, 300, 3, Config.COLOR_TEXT)
        my_move = ""
        opp_move = ""

        my_turn = True
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
                            my_move = Move.Move(textinput.value.upper(), self.chess.my_side)

                            if not my_move.castle_k and not my_move.castle_q:
                                my_move.capture = not self.chess.board.board[my_move.destination].is_empty()

                            textinput.value = ""
                            if self.chess.my_move(my_move):
                                if my_move.promotion:
                                    # update the display
                                    Display.update_display_pre()
                                    self.chess.print()
                                    Display.blit_to_screen(5, 250, textinput.surface)
                                    Display.render_to_screen(5, 275, "Press N B R Q to promote pawn...", Config.COLOR_TEXT)
                                    Display.update_display_post()
                                    
                                    promotion_piece = None
                                    while promotion_piece == None:
                                        promotion_event = pygame.event.wait()
                                        
                                        if promotion_event.key == pygame.K_n:
                                            promotion_piece = "N"
                                        elif promotion_event.key == pygame.K_b:
                                            promotion_piece = "B"
                                        elif promotion_event.key == pygame.K_r:
                                            promotion_piece = "R"
                                        elif promotion_event.key == pygame.K_q:
                                            promotion_piece = "Q"
                                    
                                    self.chess.promote(my_move.destination, promotion_piece)
                                    my_move.promotion_piece = promotion_piece

                                my_move.check = self.chess.opp_king_in_check()
                                #TODO my_move.checkmate = 

                                self.conn.sendall(str(my_move).encode())
                                my_turn = False

                    if event.key == pygame.K_ESCAPE:
                        textinput.value = ""

            Display.update_display_post()
            
            try:
                if not my_turn:
                    ready = select.select([self.conn], [], [], 0.1)
                    if ready:
                        opp_move_str = self.conn.recv(1024).decode()
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
        self.conn.close()
        self.sock.close()







