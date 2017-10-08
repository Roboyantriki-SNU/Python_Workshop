class Computers:
    def processor(self,name):
        self.processor_name = name
    def memory(self,capacity):
        self.memory_capacity = capacity
    def showSpecs(self):
        print(self.processor_name+" "+self.memory_capacity+" "+self.screen_size) #Even though the base class doesn't have screen size, the derived class has it

class Mobiles(Computers):
    def screenSize(self,size):
        self.screen_size = size

my_mobile = Mobiles()
my_mobile.processor("SD 835")
my_mobile.screenSize("5.6")
my_mobile.memory("4 GB")
my_mobile.showSpecs()
