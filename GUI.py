import pygame

pygame.init()

import pygame.freetype
import pygame_textinput

import Config
import server
import client
import Chess
import Constants
import Display


# initializations
def main():
    # creating an empty board just for displaying purposes, wont be the real playing board
    c = Chess.Chess(Constants.Color.NONE)

    running = True
    while running:
        Display.update_display_pre()

        c.print()

        Display.render_to_screen(5, 250, "1- Host a game", Config.COLOR_TEXT)
        Display.render_to_screen(5, 275, "2- Join a game", Config.COLOR_TEXT)

        # call event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYUP:
                handle_menu_keypress(event.key)

        Display.update_display_post()


# handles when a key is pressed in a menu
def handle_menu_keypress(key):
    match key:
        case pygame.K_1:
            #ip, port = get_hosting_information()
            ip = Constants.SERVER_ADDRESS
            port = Constants.SERVER_PORT
            if ip != None and port != None:
                s = server.Server(ip ,port)
                s.start_server()
                s.game_loop()
        case pygame.K_2:
            #ip, port = get_hosting_information()
            ip = Constants.SERVER_ADDRESS
            port = Constants.SERVER_PORT
            if ip != None and port != None:
                c = client.Client(ip, port)
                c.join_server()
                c.game_loop()
        case _:
            pass
    
    return

# returns the ip address and port number
# return -> (ip, port) as tuple
def get_hosting_information() -> tuple[str, str]:
    ip = get_user_input(5, 5, "Enter IPv4 address...")
    if ip != None:
        port = get_user_input(5, 5, "Enter Port number (>1024)...")

    return (None, None) if (ip == None) or (port == None) else (ip, int(port))

# function used to get one string from user
# prompt -> prompt to disply to user
def get_user_input(prompt_x, prompt_y, prompt: str) -> str:
    textinput = pygame_textinput.TextInputVisualizer(None, Display.font_input, True, Config.COLOR_TEXT, 300, 3, Config.COLOR_TEXT)

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
                        user_typing = False

                    if event.key == pygame.K_ESCAPE:
                        result = None
                        user_typing = False

        Display.update_display_post()
    
    return result


    





main()
pygame.quit()