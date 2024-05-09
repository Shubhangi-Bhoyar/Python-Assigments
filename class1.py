class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
    
    def car(self):
        print ("speed and mileage are " ,self.maxspeed ,"and", self.mileage ,"respectively")

verna = vehicle(210,20.6 )
verna.car()

