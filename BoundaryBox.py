class BoundaryBox:
    """
    container for wrapping the two BoundaryBoxCorner values:
    northwest (NW)
    southeast (SE)
    """
    NW = None
    SE = None

    def __init__(self, nwCorner, seCorner):
        self.NW = nwCorner
        self.SE = seCorner