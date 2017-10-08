class Car:
    def __init__(self):
        self.__stereo_volume = 45 #Can only be accessed from another method
    def adjustVol(self,level):
        self.__stereo_volume = level
    def showVol(self):
        print(self.__stereo_volume)
        self.__secretMethod() 
    def __secretMethod(self):
        print("Secret")
mycar = Car()
mycar.adjustVol(50)
mycar.showVol()
mycar.__stereo_volume = 80
mycar.showVol()
