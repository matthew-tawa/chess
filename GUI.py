import pygame
import pygame.freetype
import math
import Constants
import Config
import server
import client

# initialize pygame
pygame.init()

# globals
font_menu = pygame.freetype.Font('font\Roboto-Regular.ttf', 14)
font_game = pygame.freetype.Font('font\Roboto-Regular.ttf', 24)

# create the screen
screen = pygame.display.set_mode((Config.WINDOW_SIZE_X, Config.WINDOW_SIZE_Y))
pygame.display.set_caption("chess")


# initializations
def main():
    global b, screen, font_menu, font_game

    font_menu.render_to(screen, (0, 5), "1- Host a game", Config.COLOR_TEXT)
    font_menu.render_to(screen, (0, 24), "2- Join a game", Config.COLOR_TEXT)
    
    user_input = ""

    running = True
    while running:
        # call event handlers
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYUP:
                    match handle_menu_keypress(event.key):
                        case 1:
                            ip, port = get_hosting_information()
                            s = server.Server(ip ,port)
                            s.game_loop()
                        case 2:
                            ip, port = get_hosting_information()
                            c = client.Client(ip, port)
                        case _:
                            pass # ignore
                case _:
                    pass # ignore
            
        pygame.display.update()

# handles when a key is pressed in a menu
def handle_menu_keypress(key):
    result = -1
    match key:
        case pygame.K_1:
            result = 1
        case pygame.K_2:
            result = 2
        case _:
            pass
    
    return result

# returns the ip address and port number
# return -> (ip, port) as tuple
def get_hosting_information() -> tuple[str, str]:
    ip = get_user_input("Enter IP:")
    port = get_user_input("Enter Port:")
    return (ip, port)

# function used to get one string from user
# prompt -> prompt to disply to user
def get_user_input(prompt: str) -> str:
    global screen, font_menu

    user_input = ""

    getting_info = True
    while getting_info:
        for event in pygame.event.get():
            match event.type:
                case pygame.K_RETURN:
                    return user_input
                case pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                case pygame.TEXTINPUT:
                    user_input += event.text
                case pygame.K_ESCAPE:
                    getting_info = False
            
        font_menu.render_to(screen, (0, 24), user_input, Config.COLOR_TEXT)


    





main()
pygame.quit()