class Stock:
    def __init__(self, name, price, shares) -> None:
        self.name = name
        self.price = price
        self.shares = shares


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Address:
    def __init__(self, hostname, port) -> None:
        self.hostname = hostname
        self.port = port
