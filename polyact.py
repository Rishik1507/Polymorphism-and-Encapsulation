class car:
    def travel(self):
        print("I am a Road Transport")
    
class plane:
    def travel(self):
        print("I am an Air Transport")
class ship:
    def travel(self):
        print("I am a Water Transport")
c=car()
p=plane()
s=ship()
for transport in (c,p,s):
    transport.travel()
    