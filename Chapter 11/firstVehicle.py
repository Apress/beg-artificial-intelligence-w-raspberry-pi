import breve

class Controller(breve.BraitenbergControl):
    def __init__(self):
        breve.BraitenbergControl.__init__(self)
        self.vehicle = None
        self.leftSensor = None
        self.rightSensor = None
        self.leftWheel = None
        self.rightWheel = None
        self.simSpeed = 0
        self.light = None
        Controller.init(self)

    def init(self):
        self.light = breve.createInstances(breve.BraitenbergLight, 1)
        self.light.move(breve.vector(10, 1, 0))
        self.vehicle = breve.createInstances(breve.BraitenbergVehicle,1)
        self.watch(self.vehicle)
        self.vehicle.move( breve.vector(0, 2, 18))        self.leftWheel = self.vehicle.addWheel(breve.vector(-0.500000,0,-1.500000))        self.rightWheel = self.vehicle.addWheel( breve.vector(-0.500000,0,1.500000))        self.leftWheel.setNaturalVelocity(0.000000)        self.rightWheel.setNaturalVelocity(0.000000)
        self.rightSensor = self.vehicle.addSensor(breve.vector(2.000000, 0.400000, 1.500000))        self.leftSensor = self.vehicle.addSensor( breve.vector(2.000000, 0.400000, -1.500000 ) )        self.leftSensor.link(self.rightWheel)        self.rightSensor.link(self.leftWheel)        self.leftSensor.setBias(15.000000)        self.rightSensor.setBias(15.000000)
        
    def iterate(self):
        breve.BraitenbergControl.iterate(self)
        
breve.Controller = Controller

Controller()
