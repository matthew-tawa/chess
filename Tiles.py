from enum import Enum
from math import floor

# enum holding all the tile names
class Tiles(Enum):
    A8 = 0
    B8 = 1
    C8 = 2
    D8 = 3
    E8 = 4
    F8 = 5
    G8 = 6
    H8 = 7
    A7 = 8
    B7 = 9
    C7 = 10
    D7 = 11
    E7 = 12
    F7 = 13
    G7 = 14
    H7 = 15
    A6 = 16
    B6 = 17
    C6 = 18
    D6 = 19
    E6 = 20
    F6 = 21
    G6 = 22
    H6 = 23
    A5 = 24
    B5 = 25
    C5 = 26
    D5 = 27
    E5 = 28
    F5 = 29
    G5 = 30
    H5 = 31
    A4 = 32
    B4 = 33
    C4 = 34
    D4 = 35
    E4 = 36
    F4 = 37
    G4 = 38
    H4 = 39
    A3 = 40
    B3 = 41
    C3 = 42
    D3 = 43
    E3 = 44
    F3 = 45
    G3 = 46
    H3 = 47
    A2 = 48
    B2 = 49
    C2 = 50
    D2 = 51
    E2 = 52
    F2 = 53
    G2 = 54
    H2 = 55
    A1 = 56
    B1 = 57
    C1 = 58
    D1 = 59
    E1 = 60
    F1 = 61
    G1 = 62
    H1 = 63
    NOWHERE = -100

# converts string to tile
# s -> string to convert to tile. Must be in format: [A-Ha-h][1-8]
def str_to_tile(s: str) -> Tiles:
    return Tiles((8-int(s[1]))*8 + ord(s[0].upper())-65)

# converts tile to str
def tile_to_str(t: Tiles) -> str:
    return get_file_str(t) + get_rank_str(t)

# get the file of a tile as an integer
# return -> 1 for A, 2 for B, ... 8 for H
def get_file_int(t: Tiles) -> int:
    return t.value % 8

# get the rank of a tile as an integer
# return -> integer between 1 and 8 inclusively
def get_rank_int(t: Tiles) -> int:
    return 8 - floor(t.value/8)

# get the file of a tile as a string
# return -> A, B, ... H
def get_file_str(t: Tiles) -> str:
    return chr(t.value % 8 + 65)

# get the rank of a tile as a string
# return -> 1, 2, ... 8
def get_rank_str(t: Tiles) -> str:
    return str(get_rank_int(t))