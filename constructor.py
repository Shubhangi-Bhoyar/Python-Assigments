class vehicle():

    def __init__(self,engine):
        self.engine = engine
        print("engine is of ")

class car(vehicle):
    def __init__(self,engine,maxspeed):
        super().__init__(engine)
        self.maxspee = maxspeed
        print("max speed is")

jaguar = car('5000 cc','217kmph')
print('engine={car.engine},speed={car.maxspeed}')


