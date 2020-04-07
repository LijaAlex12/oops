class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(x, other):
        m1 = x.m1+other.m1
        m2 = x.m2+other.m2
        Student.s3=Student(m1,m2)

        return Student.s3

    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        return False

    def __str__(self):
        # return self.m1,self.m2
        return '{} {}'.format(self.m1,self.m2)



s1=Student(55,99)
s2=Student(89,100)

s3=s1+s2
print(s3.m1)
print(s3.m2)

print(s3)

if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')