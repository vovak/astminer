def funWithNoClass():
    pass

class Class1:

    def funInClass1():
        pass

    class Class2:

        def funInClass2():
            pass

def functionWithNoParameters():
    pass

def functionWithOneParameter(p1):
    pass

def functionWithOneTypedParameter(p1: int):
    pass

def functionWithThreeParameters(p1, p2 = 4, p3: int = 3):
    pass

def functionContainingFunction():
    def someFunction():
        pass
    pass

hello = lambda x, y: x + y