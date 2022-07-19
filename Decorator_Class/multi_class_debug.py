from functools import wraps
from inspect import Parameter, Signature


def debug(func):
    # func is a function to be wrapped
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Print debug message and return the function with the parameters back
        print("--> Function: ", func.__qualname__, "\tClass: ", func.__class__)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls: classmethod):
    # cls is a class
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


class debugmeta(type):
    def __new__(cls, classname, bases, classdict):
        clsobj = super().__new__(cls, classname, bases, classdict)
        clsobj = debugmethods(clsobj)
        return clsobj


class Base(metaclass=debugmeta):
    def __init__(self) -> None:
        self.x = "*     *"
        pass

    def baseconst(self):
        self.x = "*Defined*"


class Spam(Base):
    def __init__(self) -> None:
        super().__init__()

    def test(self):
        print(self.x)

    def baseconst(self):
        return super().baseconst()


if __name__ == "__main__":

    c = Base()
    c.baseconst()
    d = Spam()
    d.test()
    d.baseconst()
    d.test()
