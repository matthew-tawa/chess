from Tiles import Tiles

# completely empty board
EMPTY_STATE = {\
    Tiles.A1: "", Tiles.A2: "", Tiles.A3: "", Tiles.A4: "", Tiles.A5: "", Tiles.A6: "", Tiles.A7: "", Tiles.A8: "",\
    Tiles.B1: "", Tiles.B2: "", Tiles.B3: "", Tiles.B4: "", Tiles.B5: "", Tiles.B6: "", Tiles.B7: "", Tiles.B8: "",\
    Tiles.C1: "", Tiles.C2: "", Tiles.C3: "", Tiles.C4: "", Tiles.C5: "", Tiles.C6: "", Tiles.C7: "", Tiles.C8: "",\
    Tiles.D1: "", Tiles.D2: "", Tiles.D3: "", Tiles.D4: "", Tiles.D5: "", Tiles.D6: "", Tiles.D7: "", Tiles.D8: "",\
    Tiles.E1: "", Tiles.E2: "", Tiles.E3: "", Tiles.E4: "", Tiles.E5: "", Tiles.E6: "", Tiles.E7: "", Tiles.E8: "",\
    Tiles.F1: "", Tiles.F2: "", Tiles.F3: "", Tiles.F4: "", Tiles.F5: "", Tiles.F6: "", Tiles.F7: "", Tiles.F8: "",\
    Tiles.G1: "", Tiles.G2: "", Tiles.G3: "", Tiles.G4: "", Tiles.G5: "", Tiles.G6: "", Tiles.G7: "", Tiles.G8: "",\
    Tiles.H1: "", Tiles.H2: "", Tiles.H3: "", Tiles.H4: "", Tiles.H5: "", Tiles.H6: "", Tiles.H7: "", Tiles.H8: ""\
    }

# normal chess game setup
DEFAULT_STATE = {\
    Tiles.A1: "rook:pale",     Tiles.A2: "pawn:pale",     Tiles.A7: "pawn:dark",     Tiles.A8: "rook:dark",\
    Tiles.B1: "knight:pale",   Tiles.B2: "pawn:pale",     Tiles.B7: "pawn:dark",     Tiles.B8: "knight:dark",\
    Tiles.C1: "bishop:pale",   Tiles.C2: "pawn:pale",     Tiles.C7: "pawn:dark",     Tiles.C8: "bishop:dark",\
    Tiles.D1: "queen:pale",    Tiles.D2: "pawn:pale",     Tiles.D7: "pawn:dark",     Tiles.D8: "queen:dark",\
    Tiles.E1: "king:pale",     Tiles.E2: "pawn:pale",     Tiles.E7: "pawn:dark",     Tiles.E8: "king:dark",\
    Tiles.F1: "bishop:pale",   Tiles.F2: "pawn:pale",     Tiles.F7: "pawn:dark",     Tiles.F8: "bishop:dark",\
    Tiles.G1: "knight:pale",   Tiles.G2: "pawn:pale",     Tiles.G7: "pawn:dark",     Tiles.G8: "knight:dark",\
    Tiles.H1: "rook:pale",     Tiles.H2: "pawn:pale",     Tiles.H7: "pawn:dark",     Tiles.H8: "rook:dark"\
    }

# setup allowing castles
CASTLING_STATE = {\
    Tiles.A1: "rook:pale",     Tiles.A2: "pawn:pale",     Tiles.A7: "pawn:dark",     Tiles.A8: "rook:dark",\
                               Tiles.B2: "pawn:pale",     Tiles.B7: "pawn:dark",\
                               Tiles.C2: "pawn:pale",     Tiles.C7: "pawn:dark",\
                               Tiles.D2: "pawn:pale",     Tiles.D7: "pawn:dark",\
    Tiles.E1: "king:pale",     Tiles.E2: "pawn:pale",     Tiles.E7: "pawn:dark",     Tiles.E8: "king:dark",\
                               Tiles.F2: "pawn:pale",     Tiles.F7: "pawn:dark",\
                               Tiles.G2: "pawn:pale",     Tiles.G7: "pawn:dark",\
    Tiles.H1: "rook:pale",     Tiles.H2: "pawn:pale",     Tiles.H7: "pawn:dark",     Tiles.H8: "rook:dark"\
    }

# setup allowing promotions
PROMOTION_STATE = {\
    Tiles.A1: "rook:pale",     Tiles.A2: "pawn:pale",     Tiles.A7: "pawn:dark",     Tiles.A8: "rook:dark",\
                               Tiles.B2: "pawn:pale",     Tiles.B7: "pawn:dark",\
                               Tiles.C2: "pawn:pale",     Tiles.C7: "pawn:dark",\
                               Tiles.D2: "pawn:pale",     Tiles.D7: "pawn:dark",\
    Tiles.E1: "king:pale",     Tiles.E2: "pawn:pale",     Tiles.E7: "pawn:dark",     Tiles.E8: "king:dark",\
                               Tiles.F2: "pawn:pale",     Tiles.F7: "pawn:dark",\
                               Tiles.G2: "pawn:dark",     Tiles.G7: "pawn:pale",\
    Tiles.H1: "rook:pale",     Tiles.H2: "pawn:pale",     Tiles.H7: "pawn:dark",     Tiles.H8: "rook:dark"\
    }

# board state with ambiguous moves
AMBIGUOUS_STATE = {\
    Tiles.D8: "rook:dark", Tiles.H8: "rook:dark",\
        Tiles.A5: "rook:pale", Tiles.A1: "rook:pale",\
        Tiles.E4: "queen:pale", Tiles.H4: "queen:pale", Tiles.H1: "queen:pale"\
    }