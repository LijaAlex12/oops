# association with inheritance
# same method
class A:
    def show(self):
        print('A fjn')

class B(A):
    def show(self):
        print('B fernf')
    pass

a=A()
b=B()
a.show()
b.show()