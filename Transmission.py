class Transmission:
    
    def __init__(self, gearType, numOfGears, differentialRatio, **gearRatios) -> None:
        self.gearType = gearType
        self.numOfGears = numOfGears
        self.gearRatios = gearRatios