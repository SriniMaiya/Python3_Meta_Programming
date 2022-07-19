from functools import wraps

# Copies metadata of the wrapped function and stores


def debug(func):
    # func is a function to be wrapped
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Print debug message and return the function with the parameters back
        print("-->", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls: classmethod):
    # cls is a class
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


@debugmethods
class Spam:
    d = 100
    c = 100

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b

    def div(self) -> float:
        return self.a / self.b

    @classmethod
    def add_cm(cls):
        return cls.d + cls.c


if __name__ == "__main__":
    s = Spam(8, 9)
    s.add()
    s.mult()
    x = s.add_cm()
    print(x)
