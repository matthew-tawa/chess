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




class Connection():
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # chess game
        self.chess = Chess.Chess(Constants.Color.NONE)
        self.side = Constants.Color.NONE

    # runs the game
    def game_loop(self):
        self.chess.init_board(Board_States.DEFAULT_STATE, self.side)
        #self.chess.init_board(Board_States.CASTLING_STATE, self.side)
        #self.chess.init_board(Board_States.PROMOTION_STATE, self.side)
        #self.chess.init_board(Board_States.AMBIGUOUS_STATE, self.side)

        textinput = pygame_textinput.TextInputVisualizer(None, Display.font_input, True, Config.COLOR_TEXT, 300, 3, Config.COLOR_TEXT)
        my_move = ""
        opp_move = ""

        my_turn = self.side == Constants.Color.PALE
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
                        if my_turn and len(textinput.value) >2:
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
                                        
                                        if promotion_event.key == Config.KEY_KNIGHT:
                                            promotion_piece = "N"
                                        elif promotion_event.key == Config.KEY_BISHOP:
                                            promotion_piece = "B"
                                        elif promotion_event.key == Config.KEY_ROOK:
                                            promotion_piece = "R"
                                        elif promotion_event.key == Config.KEY_QUEEN:
                                            promotion_piece = "Q"
                                    
                                    self.chess.promote(my_move.destination, promotion_piece)
                                    my_move.promotion_piece = promotion_piece

                                my_move.check = self.chess.opp_king_in_check()
                                #TODO my_move.checkmate = 

                                # send() is dependent on whether instance is client/server
                                self.send(str(my_move))
                                my_turn = False

                    if event.key == pygame.K_ESCAPE:
                        textinput.value = ""

            Display.update_display_post()
            
            try:
                if not my_turn:
                    # ready() is dependent on whether instance is client/server
                    if self.ready():
                        # receive() is dependent on whether instance is client/server
                        opp_move_str = self.receive()
                        if len(opp_move_str) > 0:
                            opp_move = Move.Move(opp_move_str, self.chess.opp_side)
                            self.chess.opp_move(opp_move)

                            if opp_move.promotion:
                                self.chess.promote(opp_move.destination, opp_move.promotion_piece)

                            my_turn = True

                if opp_move == 'forfeit':
                    # TODO
                    break

            except Exception as e:
                if e.errno == 10035:
                    pass
                else:
                    print(e)
                    break

            Display.clock.tick(Config.FPS)

        print('Connection closed.')
        self.sock.close()








class Server(Connection):
    def __init__(self, port) -> None:
        Connection.__init__(self, "0.0.0.0", port)

        # client info (to be populated on connection)
        self.conn = None
        self.addr = None

    # opens server and waits for a connection
    # my_side -> my side for the game
    def start_server(self, my_side: Constants.Color):
        self.side = my_side

        print('Starting server on port %s as the %s pieces.' % (self.port, self.side))
        self.sock.bind((self.ip, self.port))
        self.sock.listen(10)

        # find connections
        self.conn, self.addr = self.sock.accept()
        self.conn.setblocking(0)

        # sending opponent their side
        self.send("dark" if self.side == Constants.Color.PALE else "pale")
        print('Client with address %s connected.' % self.addr[0])

    # server send message to client
    def send(self, message: str):
        self.conn.sendall(message.encode())

    # server waits and receives message from client
    def receive(self) -> str:
        return self.conn.recv(1024).decode()
    
    # return -> True if ready to receive something, False otherwise
    def ready(self) -> bool:
        return select.select([self.conn], [], [], 0.1)[0]






class Client(Connection):
    def __init__(self, ip, port) -> None:
        Connection.__init__(self, ip, port)

    # connects to server
    def join_server(self):
        print('Connecting to %s port %s...' % (self.ip, self.port))
        self.sock.connect((self.ip, self.port))

        # receiving my side from server
        self.side = Constants.Color.PALE if self.receive() == "pale" else Constants.Color.DARK
        print('Connection successful, playing as %s pieces.' % (self.side))

        self.sock.setblocking(0)

    # client send message to server
    def send(self, message: str):
        self.sock.sendall(message.encode())

    # client waits and receives message from server
    def receive(self) -> str:
        return self.sock.recv(1024).decode()
    
    # return -> True if ready to receive something, False otherwise
    def ready(self) -> bool:
        return select.select([self.sock], [], [], 0.1)[0]

   
