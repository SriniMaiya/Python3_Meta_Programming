from inspect import Parameter, Signature


class Descriptor:
    def __init__(self, name) -> None:
        self.name = name

    # def __get__(self, instance, cls):
    #     # instance: is the current instance being manipulated
    #     print("Get ", self.name)
    #     return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("Set ", self.name, value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("Delete ", self.name)
        del instance.__dict__[self.name]


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
    shares = Descriptor("shares")  # Redefine .shares of the class instance
    name = Descriptor("name")


class Point(Structure):
    _fields = ["x", "y"]
