def make_adder(x: int, y: int) -> tuple([int, int]):
    print("x: ", x)
    print("y: ", y)

    def add():
        return x + y

    def xor():
        return x ^ y

    return add, xor


if __name__ == "__main__":

    x, y = make_adder(8, 14)

    print("x+y = ", x())
    print("xor(x, y) = ", y())
