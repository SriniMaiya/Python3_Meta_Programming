from inspect import Parameter, Signature

"""Pros: Better readability of code
Cons: Code repition (reduced, but still present)
        Still lacks type checking"""


def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)


class Structure:
    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs) -> None:
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


class Stock(Structure):
    __signature__ = make_signature(["name", "shares", "price"])


class Point(Structure):
    __signature__ = make_signature(["x", "y"])


if __name__ == "__main__":

    stock = Stock("GOOG", 490.1, 100)
    print("---> Stock 1")
    print("Name: ", stock.name)
    print("Price", stock.price)
    print("Shares: ", stock.shares)

    print("---> Stock 2")
    try:
        stock2 = Stock("GOOG", 250)  # ERROR!
    except TypeError as e:
        print("ERROR: ", e)

    p1 = Point(-1, 3)
    print(f"p1.x: {p1.x}\tp1.y: {p1.y}")
