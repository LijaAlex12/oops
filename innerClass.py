class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        # object of inner class Lpatop
        # inside outer class
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand='Apple'
            self.cpu='i7'
            self.ram=16

        def show(self):
            print(self.brand,self.cpu,self.ram)




s1 = Student('Lija',5)
s2 = Student('Merin',5)
s1.show()
# object of innerclass outside
# outer class in main using
# outer class to call inner class
lap1=Student.Laptop()
# lap1.show()