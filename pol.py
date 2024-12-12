class cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f'I am {self.name} and I am {self.age} years old.')
    def sound(self):
        print("Meow")

class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f'I am {self.name} and I am {self.age} years old.')
    def sound(self):
        print("Bark")
c=cat("Kitty",4)
d=dog("Puppy",7)
for ani in (c,d):
    ani.info()
    ani.sound()


        