import pygame
import pygame.freetype

pygame.display.init()
pygame.font.init()
pygame.freetype.init()

import pygame.freetype
import pygame_textinput

import Config
import Connection
import Chess
import Constants
import Display


# initializations
def main():
    # set event types allowed in queue
    pygame.event.set_blocked(None) # block all events
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN])

    # creating an empty board just for displaying purposes, wont be the real playing board
    c = Chess.Chess(Constants.Color.NONE)

    Display.update_display_pre()

    c.print()

    Display.render_to_screen(5, 250, "1- Host a game", Config.COLOR_TEXT)
    Display.render_to_screen(5, 275, "2- Join a game", Config.COLOR_TEXT)
    Display.update_display_post()

    running = True
    while running:
        # wait for an event
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            running = False
        
        # call event handler
        if event.type == pygame.KEYDOWN:
            handle_menu_keypress(event.key)


        


# handles when a key is pressed in a menu
def handle_menu_keypress(key):
    match key:
        case pygame.K_1:
            port = get_server_information()
            server_side_ui = get_user_input("Choose (P)ale or (D)ark...", "", ["P", "p", "D", "d"]).upper()
            server_side = Constants.Color.PALE if server_side_ui == "P" else Constants.Color.DARK

            if port != None:
                s = Connection.Server(port)
                s.start_server(server_side)
                s.game_loop()
        case pygame.K_2:
            ip, port = get_client_information()
            if ip != None and port != None:
                c = Connection.Client(ip, port)
                c.join_server()
                c.game_loop()
        case _:
            pass
    
    return

# returns the port number
# return -> (ip, port) as tuple
def get_server_information() -> str:
    port = get_user_input("Enter Port number (>1024)...")

    return None if (port == None) else int(port)

# returns the ip address and port number
# return -> (ip, port) as tuple
def get_client_information() -> tuple[str, str]:
    ip = get_user_input("Enter IPv4 address...", "192.168.1.")
    if ip != None:
        port = get_user_input("Enter Port number (>1024)...")

    return (None, None) if (ip == None) or (port == None) else (ip, int(port))

# function used to get one string from user
# prompt -> prompt to disply to user
# data_validation -> limit user to enetering certain values
# prompt_x -> x position of prompt (default 5)
# prompt_y -> y position of prompt (default 5)
def get_user_input(prompt: str, default_txt = "", data_validation = [], prompt_x = 5, prompt_y = 5) -> str:
    textmanager = pygame_textinput.TextInputManager()
    textinput = pygame_textinput.TextInputVisualizer(textmanager, Display.font_input, True, Config.COLOR_TEXT, 300, 3, Config.COLOR_TEXT)
    textinput.value = default_txt
    textmanager.cursor_pos = len(textmanager.value)

    result = ""
    user_typing = True
    while user_typing:
        Display.update_display_pre()

        Display.render_to_screen(prompt_x, prompt_y, prompt, Config.COLOR_TEXT)

        events = pygame.event.get()
        textinput.update(events)

        Display.blit_to_screen(prompt_x, prompt_y + 20, textinput.surface)

        # need to check if user clicked enter
        for event in events:
            match event.type:
                case pygame.QUIT:
                    exit()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        result = textinput.value
                        user_typing = data_validation and not result in data_validation 

                    if event.key == pygame.K_ESCAPE:
                        result = None
                        user_typing = False

        Display.update_display_post()
        
        Display.clock.tick(Config.FPS)
    
    return result


    





main()
pygame.quit()