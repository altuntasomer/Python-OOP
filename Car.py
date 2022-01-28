from Dimensions import Dimensions
from Engine import Engine
from Transmission import Transmission
from Wheel import Wheel


class Car(Dimensions,Engine, Transmission, Wheel):

    def __init__(self, productionDate, color) -> None:
        
        self.color = color
        self.top_speed = None

        