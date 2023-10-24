class BoundaryBoxCorner:
    """
    x,y coordinate pair parameters, just for making calling code more readable
    """
    x = -1
    y = -1
    def __init__(self, tuplePair):
        self.x = tuplePair[1]
        self.y = tuplePair[0]