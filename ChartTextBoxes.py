# local imports
from enums import Player
from BoundaryBox import BoundaryBox
from BoundaryBoxes import BoundaryBoxes
from BoundaryBoxCorner import BoundaryBoxCorner

class ChartTextBoxes:
    name = None
    def __init__(self, imageMatrix):
        lengthX = imageMatrix.shape[1]
        heightY = imageMatrix.shape[0]
        bb = BoundaryBoxes.SongTitle
        self.name = BoundaryBox(
            BoundaryBoxCorner((round(bb.top*heightY), round(bb.left*lengthX))),
            BoundaryBoxCorner((round(bb.bot*heightY), round(bb.right*lengthX)))
        )