class Person:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print("Hey! I am "+self.name+".")

new_person = Person("Hariharan")
new_person.sayHello()
