class p:
    #company = 'XYZ'
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def show(self):
        print('name:',self.name,'age',self.age,'address',self.address)

    def work(self):
        print("name",self.name,"address",self.address)

Shubh = p('Shubh','22','USA')
Sakshi = p('sakshi','23','Los Angeles')
 

Shubh.show()
Sakshi.work()

