class Car:
    def __init__(self, make , model, year):
        self.make=make
        self.model=model
        self.year=year


ar=Car("Honda","civic",2022)
print(ar.make)
print(ar.model)
print(ar.year)