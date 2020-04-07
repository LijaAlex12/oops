# argument or type of argument different
# or different no of parameters
# is Method Overlaoding


class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    # python doesnot support method overloading
    # but kinda trying to implement method overloading

    def sums(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c

        elif a != None and b != None:
            s=a+b

        else:
            s=a

        return s


s1=Student(100,100)
print(s1.sums())