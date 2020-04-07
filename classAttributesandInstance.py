class Person:
    no_of_people=0
    def __init__(self,name):
       self.name=name
       # Person.no_of_people+=1
       Person.add_person()

    @classmethod
    def number_of_people(cls):
       return cls.no_of_people

    @classmethod
    def add_person(cls):
       cls.no_of_people+=1

p1=Person("Tim")
# print(Person.no_of_people)
print(p1.number_of_people())
print(Person.number_of_people())
p2=Person("Lija")
# print(Person.no_of_people)
print(p2.number_of_people())
print(Person.number_of_people())

#classes are exportable and class attributes useful while exporting
#no_of_people specific to class and not instance

# print(Person.no_of_people)
# print(p1.no_of_people)
# Person.no_of_people=8
# print(p2.no_of_people)


