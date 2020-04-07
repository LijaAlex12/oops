class A:
    def __init__(self):
        print('init A')
    def feature1(self):
        print('feature1 A')

    def feature2(self):
        print('feature2')

# subclass
class B():
    def __init__(self):
        super().__init__()
        print('b init')
    def feature1(self):
        print('feature1 B')

    def feature4(self):
        print('feature4')

class C(A,B):
    def __init__(self):
        super().__init__()
        super().feature1()
        print('c init')

a1=C()
