class Car:

    def __init__(self, color, max_speed, hp, weight) -> None:
        
        self.color = color
        self.max_speed = max_speed
        self.hp = hp
        self.weight = weight


    def printInfo(self):

        print("color is: {}, max speed is: {}, horse power is: {}, weight is: {}".format(self.color, self.max_speed, self.hp, self.weight))

car1 = Car("red", 250, 280, 1540)
car2 = Car("blue", 220, 180, 1240)
car1.printInfo()
car2.printInfo()