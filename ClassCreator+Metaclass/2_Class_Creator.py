class Structure:
    """Generalized class initializer.
    --> Pros: A single initializer for all the classes.
    --> Cons: Loses keyword arguments.
              No type setting.
              Allows Initialization of incomplete class instance.
              Loses keyword signature
    """

    _fields = []

    def __init__(self, *args) -> None:
        for name, val in zip(self.__class__._fields, args):
            setattr(self, name, val)


class Stock(Structure):
    _fields = ["name", "price", "shares"]


class Point(Structure):
    _fields = ["x", "y"]


class Address(Structure):
    _fields = ["hostname", "port"]


if __name__ == "__main__":
    # Creation of the Stock class instance.
    stock = Stock("GOOG", 490.1, 100)
    print("Name: ", stock.name)
    print(stock._fields[1].capitalize() + ": ", stock.price)
    print("Shares: ", stock.shares)
    # Bad example, allows incomplete instance creation and resulting in an error, while accessing the non initialized keyword 'shares'
    stock2 = Stock("GOOG", 250)  # No error, but 'shares' variable is not created
    print("Name: ", stock2.name)
    print(stock2._fields[1].capitalize() + ": ", stock2.price)
    print("Shares: ", stock2.shares)  # ERROR!
