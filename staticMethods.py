class Math:

    # static mehtods don't need an instance of a class to run
    @staticmethod
    def add5(x):
        return x+5

    @staticmethod
    def add10(x):
        return x+10
    @staticmethod
    def pr():
        print('run')

print(Math.add5(4))
print(Math.add10(2))
Math.pr()
