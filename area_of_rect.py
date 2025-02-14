"""
Write a  Python class named Rectangle constructed 
from length and width and a method that will compute 
the area of a rectangle.
"""

class Rectangle():
    def __init__(self, l, w):
        self.length=l
        self.width=w

    def rectangle_area(self):
        return self.length*self.width
    
new=Rectangle(12, 10)
print(new.rectangle_area())