
# multiple inheritance
class A:
    def feature1(self):
        print('feature1')

    def feature2(self):
        print('feature2')

# subclass
class B():
    def feature3(self):
        print('feature3')

    def feature4(self):
        print('feature4')

class C(A,B):
    def feature5(self):
        print('feature5')

a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature1()
b1.feature3()

c1=C()
c1.feature1()
c1.feature5()