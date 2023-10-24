# local imports
from enums import Player
from BoundaryBox import BoundaryBox
from BoundaryBoxes import BoundaryBoxes
from BoundaryBoxCorner import BoundaryBoxCorner

class PlayerTextBoxes:
    score = None
    breakdown = None
    perfect = None
    great = None
    good = None
    bad = None
    miss = None
    combo = None
    kcal = None
    difficulty = None
    name = None
    title = None

    def __init__(self, imageMatrix, player):
        lengthX = imageMatrix.shape[1]
        heightY = imageMatrix.shape[0]

        if player == Player.P1:
            bb = BoundaryBoxes.P1
        if player == Player.P2:
            bb = BoundaryBoxes.P2

        self.score = BoundaryBox(
            BoundaryBoxCorner((round(bb.Score.top*heightY), round(bb.Score.left*lengthX))),
            BoundaryBoxCorner((round(bb.Score.bot*heightY), round(bb.Score.right*lengthX)))
        )
        self.breakdown = BoundaryBox(
            BoundaryBoxCorner((round(bb.Breakdown.top*heightY), round(bb.Breakdown.left*lengthX))),
            BoundaryBoxCorner((round(bb.Breakdown.bot*heightY), round(bb.Breakdown.right*lengthX)))
        )
        self.perfect = BoundaryBox(
            BoundaryBoxCorner((round(bb.Perfect.top*heightY), round(bb.Perfect.left*lengthX))),
            BoundaryBoxCorner((round(bb.Perfect.bot*heightY), round(bb.Perfect.right*lengthX)))
        )
        self.great = BoundaryBox(
            BoundaryBoxCorner((round(bb.Great.top*heightY), round(bb.Great.left*lengthX))),
            BoundaryBoxCorner((round(bb.Great.bot*heightY), round(bb.Great.right*lengthX)))
        )
        self.good = BoundaryBox(
            BoundaryBoxCorner((round(bb.Good.top*heightY), round(bb.Good.left*lengthX))),
            BoundaryBoxCorner((round(bb.Good.bot*heightY), round(bb.Good.right*lengthX)))
        )
        self.bad = BoundaryBox(
            BoundaryBoxCorner((round(bb.Bad.top*heightY), round(bb.Bad.left*lengthX))),
            BoundaryBoxCorner((round(bb.Bad.bot*heightY), round(bb.Bad.right*lengthX)))
        )
        self.miss = BoundaryBox(
            BoundaryBoxCorner((round(bb.Miss.top*heightY), round(bb.Miss.left*lengthX))),
            BoundaryBoxCorner((round(bb.Miss.bot*heightY), round(bb.Miss.right*lengthX)))
        )
        self.combo = BoundaryBox(
            BoundaryBoxCorner((round(bb.Combo.top*heightY), round(bb.Combo.left*lengthX))),
            BoundaryBoxCorner((round(bb.Combo.bot*heightY), round(bb.Combo.right*lengthX)))
        )
        self.kcal = BoundaryBox(
            BoundaryBoxCorner((round(bb.Kcal.top*heightY), round(bb.Kcal.left*lengthX))),
            BoundaryBoxCorner((round(bb.Kcal.bot*heightY), round(bb.Kcal.right*lengthX)))
        )
        self.difficulty = BoundaryBox(
            BoundaryBoxCorner((round(bb.Difficulty.top*heightY), round(bb.Difficulty.left*lengthX))),
            BoundaryBoxCorner((round(bb.Difficulty.bot*heightY), round(bb.Difficulty.right*lengthX)))
        )
        self.name = BoundaryBox(
            BoundaryBoxCorner((round(bb.Name.top*heightY), round(bb.Name.left*lengthX))),
            BoundaryBoxCorner((round(bb.Name.bot*heightY), round(bb.Name.right*lengthX)))
        )
        self.title = BoundaryBox(
            BoundaryBoxCorner((round(bb.Title.top*heightY), round(bb.Title.left*lengthX))),
            BoundaryBoxCorner((round(bb.Title.bot*heightY), round(bb.Title.right*lengthX)))
        )