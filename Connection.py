



class parent():
    def __init__(self) -> None:
        self.x = 1

    def func(self):
        self.vfunc()


class child1(parent):
    def __init__(self) -> None:
        super().__init__()
        self.y = 2

    def vfunc(self):
        print(self.y)

class child2(parent):
    def __init__(self) -> None:
        super().__init__()
        self.y = 3

    def vfunc(self):
        print(self.y)


c1 = child1()
c1.func()

c2 = child2()
c2.func()






class Connection():
    pass