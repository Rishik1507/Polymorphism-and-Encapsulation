class television:
    def __init__(self):
        self.__sp=40000
    def sell(self):
        print(f'Selling Price : {self.__sp}')
    def set(self,price):
        self.__sp=price
t=television()
t.sell()
t.__sp=50000
t.sell()
t.set(50000)
t.sell()