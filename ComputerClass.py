class Student:
    school='Chavara'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1+self.m2+self.m3)/3

    # def get_m1(self):
    #     return self.m1
    #
    # def set_m1(self,value):
    #     self.m1=value
    @classmethod
    def getSchool(cls):
        return cls.school


    # nothing to do with class and instance variables
    @staticmethod
    def info():
        print("dhgjvf")

s1=Student(45,46,78)
s2=Student(45,56,80)

print(s1.average())
print(s2.average())
print(Student.getSchool())
print(Student.info())