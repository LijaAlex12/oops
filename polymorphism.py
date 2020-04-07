class Pycharm:
    def execute(self):
        print("compiling")
        print("running")

class Myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()

#
# ide=Pycharm()
ide=Myeditor()
lap1=Laptop()
lap1.code(ide)