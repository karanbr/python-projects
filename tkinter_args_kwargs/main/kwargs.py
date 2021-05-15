# keyword arguments

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=5, multiply=7)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]  # mandatory with []
        self.model = kwargs.get("model")  # if this isn't specified it will return None


car = Car(make="Audi", model="A4")
print(car.model, car.make)
