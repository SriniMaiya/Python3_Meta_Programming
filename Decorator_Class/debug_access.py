def debugattr(cls: classmethod):
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print("Get: ", name)

        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__

    return cls


@debugattr
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


if __name__ == "__main__":
    p = Point(-4, 5)
    p.x
    p.y
