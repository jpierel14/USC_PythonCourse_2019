import Example_ClassVehicle


Vehicle = Example_ClassVehicle.Vehicle
class Car(Vehicle):
    def __init__(
        self, 
        name = None,
        width = None,
        length = None,

        doorcount = None,
        carbrand = None,
        carmodel = None,
        year = None,
        ):
        Vehicle.__init__( 
            self, 
            name = name, 
            width = width, 
            length = length)

        self.classname = 'car'
        self.doorcount = doorcount
        self.carbrand = carbrand
        self.carmodel = carmodel
        self.year = year



    def printself(self):
        print( 'classname', self.classname )
        print( 'name', self.name )
        print( 'width', self.width )
        print( 'length', self.length )
        print( 'doorcount', self.doorcount )
        print( 'carbrand', self.carbrand )
        print( 'carmodel', self.carmodel )
        print( 'year', self.year )

car1 = Car(
    name = 'dadcar', 
    carbrand = 'toyota', 
    carmodel = 'camry', 
    year = '2019', 
    width = 6, 
    length = 12)


car1.printself()

