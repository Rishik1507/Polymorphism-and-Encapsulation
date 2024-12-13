class poly:
    def __init__(self):
        self.__side=0
        self.__length=0
    def setside(self,s):
        self.__side=s
    def setlength(self,l):
        self.__length=l
    def peri(self):
        print(f'The perimeter is {self.__length*self.__side}')
p=poly()
p.setlength(5)
p.setside(6)
p.peri()