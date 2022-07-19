from inspect import Parameter, Signature

"""Pros: Signature creation
         Class creation automation
Cons:    Missing type checking
         resulting in Creation of garbage class instance"""


def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)


class MetaStructure(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, "__signature__", sig)
        return clsobj


class Structure(metaclass=MetaStructure):
    _fields = []

    def __init__(self, *args, **kwargs) -> None:
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


class Stock(Structure):
    _fields = ["name", "shares", "price"]


class Point(Structure):
    _fields = ["x", "y"]


if __name__ == "__main__":
    s = Stock("GOOG", 400, 401.25)
    s2 = Stock(
        name=256, price="False", shares=4 + 7j
    )  # Allows Garbage class instance creation
    p1 = Point(8, 14)
