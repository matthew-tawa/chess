import Tiles
import Constants
import math
import re



class Move():

    def __init__(self, move_str, color: Constants.Color, capture = False, check = False, checkmate = False) -> None:

        self.color = color
        self.castle_q = "0-0-0" in move_str
        self.castle_k = "0-0" in move_str and not self.castle_q
        self.destination = None
        self.promotion = False

        matches = False
        if "0-0" not in move_str:
            pattern_text = "(?P<piece>^.{1})(?P<file_or_rank>[A-H1-8][1-8]?)?(?P<capture>x)?(?P<destination>[A-H][1-8])(?P<promotion>=.?)?(?P<check>\+)?(?P<checkmate>\+)?"
            pattern = re.compile(pattern_text)
            matches = pattern.match(move_str)

            self.piece = matches.group("piece") if matches and "piece" in matches.groupdict() else "K"
            self.file_or_rank = matches.group("file_or_rank") if matches and "file_or_rank" in matches.groupdict() else None
            self.capture = matches.group("capture") == "x" if matches and "capture" in matches.groupdict() else capture
            self.destination = Tiles.str_to_tile(matches.group("destination")) if matches and "destination" in matches.groupdict() else None
            self.promotion = self.get_piece() == "pawn" and Tiles.get_rank_int(self.destination) == (8 if self.color == Constants.Color.PALE else 1)
            self.promotion_piece = matches.group("promotion") if matches and "promotion" in matches.groupdict() else ""
            self.check = matches.group("check") == "+" if matches and "check" in matches.groupdict() else check
            self.checkmate = matches.group("checkmate") == "++" if matches and "checkmate" in matches.groupdict() else checkmate

            self.ambiguous = self.file_or_rank != None and self.file_or_rank != ""

            if self.file_or_rank == None:
                self.file_or_rank = ""

            if self.promotion_piece == None:
                self.promotion_piece = ""

            # if the promotion piece was obtained from the string, it will have the "=" included, so we need to get rid of the "="
            if len(self.promotion_piece) > 1:
                self.promotion_piece = self.promotion_piece[-1]


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
            result += Tiles.tile_to_str(self.destination)
            result += ("=" + self.promotion_piece) if self.promotion else ""
            result += "+" if self.check else "++" if self.checkmate else ""
        
        return result

    # return piece as string
    def get_piece(self) -> str:
        match self.piece:
            case "":
                return "pawn"
            case "P":
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

        
