
import Example_ClassVehicle



Vehicle = Example_ClassVehicle.Vehicle
class Boat(Vehicle):
    def __init__(
        self, 
        name = None,
        width = None,
        length = None,
        doorcount = 0,
        ):
        Vehicle.__init__( 
            self, 
            name = name, 
            width = width, 
            length = length)

        self.classname = 'boat'
        self.doorcount = doorcount

    def printself(self):
        print( 'classname', self.classname )
        print( 'name', self.name )
        print( 'width', self.width )
        print( 'length', self.length )
        print( 'doorcount', self.doorcount )

boat1 = Boat(name = 'santa maria', width = 30, length = 70)


boat1.printself()

