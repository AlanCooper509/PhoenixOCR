# imports
import enum

class Player(enum.Enum):
    """
    enums for better specifying expected class constructor input values
    """
    P1 = 1
    P2 = 2

class Modes(enum.Enum):
    SCORES = "scores"
    FAST = "fast"
    ALL = "all"