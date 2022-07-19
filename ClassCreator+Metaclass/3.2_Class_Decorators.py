from inspect import Parameter, Signature


def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)


class Structure:
    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs) -> None:
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


def add_signature(*names):
    def decorate(cls: classmethod):
        cls.__signature__ = make_signature(names)
        return cls

    return decorate


@add_signature("name", "shares", "price")
class Stock(Structure):
    pass


@add_signature("x", "y")
class Point(Structure):
    pass
