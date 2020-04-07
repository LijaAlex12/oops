class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name},I am {self.age} years old.")

    def speak(self):
        print('I dont know what to say')


class Cat(Pet):

    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def speak(self):
        print("meow")

    def show(self):
        print(f"I am {self.name},I am {self.age} years old.{self.color} in color")




class Dog(Pet):
    def speak(self):
        print('bark')


p=Pet("Tim",19)
p.speak()
c=Cat("Bill",14,'blue')
c.show()
c.speak()
print(c.color,c.name,c.age)
d=Dog("Jill",25)
d.speak()

