class vehicle():

    def __init__(self,engine):
        self.engine = engine
        #print("engine details ")

class car(vehicle):
    def __init__(self,engine,maxspeed):
        super().__init__(engine)
        self.maxspeed = maxspeed
        #print("max speed details")
class car2(car):
    def __init__(self,engine,maxspeed,mileage):
        super().__init__(engine,maxspeed)
        self.mileage = mileage
        
jaguar = car2('5000 cc','217kmph','14.49kmpl')
print('engine={jaguar.engine},speed={jaguar.maxspeed},mileage={jaguar.mileage}')


