def add(*args):
    # tuple
    print(type(args))
    sum_result = 0
    for n in args:
        sum_result += n
    return sum_result


print(add(3, 4, 5, 6))


def calculate(n, **kwargs):
    # dictionary
    print(type(kwargs))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.model)