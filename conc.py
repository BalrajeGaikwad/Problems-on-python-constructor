class Person:
    def __init__(self, name):
        self.name=name

    def say_hi(self):
        print("hello, my na,e is ",self.name)

p=Person('nikhil')
p.say_hi()