length = float(input("enter length ",))
breadth = float(input("enter breadth ",))
height = float(input("enter height ",))    
class Box:
    def __init__(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def volume(self):
        print("the volume is :",self.length * self.breadth * self.height )

    def Area(self):
        print("the total surface area is :" , (2 * ( self.length * self.breadth + self.breadth * self.height + self.height * self.length )))
v = Box(length,breadth,height)
v.volume()
v.Area()
        
