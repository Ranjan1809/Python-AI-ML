class A:

    def __init__(self):
        print("A super class")


class B(A):

    def __init__(self):
        super().__init__()
        print("In B")
        print("B sub class of A")


class C(A):

    def __init__(self):
        super().__init__()
        print("In c")
        print("C sub class of A")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D sub class of B and C")


obj = D()

