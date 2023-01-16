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
        self.chess.init_board(Board_States.DEFAULT_STATE)

        textinput = pygame_textinput.TextInputVisualizer(None, Display.font_input, True, Config.COLOR_TEXT, 300, 3, Config.COLOR_TEXT)
        my_move = ""
        opp_move = ""

        my_turn = False
        while True:
            Display.update_display_pre()

            # get events
            events = pygame.event.get()
            textinput.update(events)
            
            # display the board
            self.chess.print()

            # show text input
            Display.blit_to_screen(5, 250, textinput.surface)

            # need to check if user clicked enter
            for event in events:
                if event.type == pygame.QUIT:
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if my_turn:
                            my_move = Move.Move(textinput.value)
                            #TODO get the status of check, checkmate, capture, etc
                            #TODO validate my_mvoe is a valid move
                            textinput.value = ""
                            self.chess.my_move(my_move)
                            self.sock.sendall(str(my_move).encode())
                            my_turn = False

                    if event.key == pygame.K_ESCAPE:
                        textinput.value = ""


            try:
                if not my_turn:
                    ready = select.select([self.sock], [], [], 0.1)
                    if ready:
                        opp_move = Move.Move(self.sock.recv(1024).decode())
                        self.chess.opp_move(opp_move)
                        my_turn = True

                if opp_move == 'forfeit':
                    break

            except Exception as e:
                if e.errno == 10035:
                    pass
                else:
                    print(e)
                    break
                

            Display.update_display_post()



        print('Connection closed.')
        self.sock.close()








