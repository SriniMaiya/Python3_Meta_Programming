from inspect import Parameter, Signature


def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)


class Descriptor:
    def __init__(self, name) -> None:
        self.name = name

    # def __get__(self, instance, cls):
    #     print("Get ", self.name)
    #     return instance.__dict__[self.name]
    # instance: is the current instance being manipulated
    def __set__(self, instance, value):
        print("Set ", self.name, value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("Delete ", self.name)
        del instance.__dict__[self.name]


class Typed(Descriptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError("Expected %s " % self.ty)
        super().__set__(instance, value)


class Integer(Typed):
    ty = int


class Float(Typed):
    ty = float


class String(Typed):
    ty = str


class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Must be >= 0")
        super().__set__(instance, value)


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


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
    name = String("name")
    price = PositiveFloat("price")
    shares = PositiveInteger("shares")


class Point(Structure):
    _fields = ["x", "y"]


if __name__ == "__main__":
    s = Stock("ACME", 200, 490.1)
    # print(s.__dict__)
    try:
        s.shares = 490.1
    except TypeError as e:
        print("Error setting 's.shares = 490.1': ", e)

    try:
        s.price = -490.1
    except ValueError as e:
        print("Error setting 's.price = -490.1': ", e)
