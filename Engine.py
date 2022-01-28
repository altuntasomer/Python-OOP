class Engine:

    def __init__(self, code, power, torque, rpm, location, displacement, numOfCyclinders, posOfCyclinders, valvePerCyclinder, fuelSystem, fuelType, aspiration) -> None:
        
        self.code = code
        self.power = power
        self.torque = torque
        self.rpm = rpm
        self.location = location
        self.displacement = displacement
        self.numOfCyclinders = numOfCyclinders
        self.posOfCyclinders = posOfCyclinders
        self.valvePerCyclinder = valvePerCyclinder
        self.fuelSystem = fuelSystem
        self.fuelType = fuelType
        self.aspiration = aspiration