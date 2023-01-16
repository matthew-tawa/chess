from Tiles import Tiles



class Move():

    def __init__(self, move_str, capture = False, castle_k = False, castle_q = False, check = False, checkmate = False) -> None:
        self.piece = move_str[0] if len(move_str) > 2 else ""
        self.file_or_rank = move_str[1] if len(move_str) > 3 else ""
        self.destination = move_str if len(move_str) == 2 else move_str[-2:]
        self.ambiguous = len(move_str) > 3
        self.capture = capture
        self.castle_k = castle_k
        self.castle_q = castle_q
        self.check = check
        self.checkmate = checkmate

    # convert move to string
    def __str__(self) -> str:
        result = ""

        if self.castle_k:
            result = "0-0"

        elif self.castle_q:
            result = "0-0-0"

        else:
            result += self.piece
            result += self.file_or_rank
            result += "x" if self.capture else ""
            result += self.destination
            result += "+" if self.check else "++" if self.checkmate else ""
        
        return result

    # return piece as string
    def get_piece(self) -> str:
        match self.piece:
            case "":
                return "pawn"
            case "N":
                return "knight"
            case "B":
                return "bishop"
            case "R":
                return "rook"
            case "Q":
                return "queen"
            case "K":
                return "king"

    # return destination as Tiles
    def get_destination(self) -> Tiles:
        return Tiles((8 - int(self.destination[1])) * 8 + ord(self.destination[0]) - 65)