

Boat1 = {
    'classname': 'boat',
    'name': 'santa maria',
    'width': 30,
    'length': 70,
    'doorcount': 0,
    }

Boat2 = {
    'classname': 'boat',
    'name': 'pinta',
    'width': 30,
    'length': 70,
    'doorcount': 0,
    }

Car1 =     {
    'classname': 'car',
    'name': 'dadcar',
    'width': 6,
    'length': 12,
    'doorcount': None,
    'carbrand': 'toyota',
    'carmodel': 'camry',
    'year': 2019,
    }


#Does it quack like a duck? Does it look like a duck?  --> then its ducktyped as a duck
def IsBoatCheck( BoatCandidate ):
    Result = True
    BoatKeys = [ 'classname', 'name', 'width', 'length','doorcount',]
    ExtraKeys   =  set(BoatCandidate.keys() ) - set(BoatKeys)
    MissingKeys =  set(BoatKeys)              - set(BoatCandidate.keys() ) 
    if len(ExtraKeys) != 0: 
        Result = False
    if len(MissingKeys) != 0:
        Result = False
    if BoatCandidate['classname'] != 'boat':
        return False
    return Result


def IsCarCheck( CarCandidate ):
    Result = True
    CarKeys = [ 'classname', 'name', 'width', 'length','doorcount','carbrand','carmodel', 'year']
    ExtraKeys   =  set(CarCandidate.keys() ) - set(CarKeys)
    MissingKeys =  set(CarKeys)              - set(CarCandidate.keys() ) 
    if len(ExtraKeys) != 0: 
        Result = False
    if len(MissingKeys) != 0:
        Result = False
    if CarCandidate['classname'] != 'car':
        return False
    return Result


print ( IsBoatCheck( Boat1 ) )
print ( IsBoatCheck( Car1 ) )


print ( IsCarCheck( Boat1 ) )
print ( IsCarCheck( Car1 ) )













