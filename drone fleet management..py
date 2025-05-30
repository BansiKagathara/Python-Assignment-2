#2 drone fleet management
class Device:
       def init(self,id):
              self.id=id

class Flyer:
       def fly(self):
              print("FLying.....")

class Drone(Device,Flyer):
       def init(self,id):
              Device.init(self,id)
                      
       def capture_image(self):
              print("Capturing image....")

d=Drone("g545")
print("Device id: ",d,id)
d.fly()
d.capture_image()
