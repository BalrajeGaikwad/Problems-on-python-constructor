class A(object):
    def __init__(self, something):
        print("A init called")
        self.something= something

class B(A):
    def __init__(self, something):
        A.__init__(self, something)
        print("B init called")
        self.something=something

obj=B("something")



class C(object):
    def __init__(self, happy):
        print("c init is called")
        self.happy=happy


class D(C):
    def __init__(self, happy):
        print("D is called")
        self.happy=happy
        C.__init__(self,happy)

obj=D("happy")