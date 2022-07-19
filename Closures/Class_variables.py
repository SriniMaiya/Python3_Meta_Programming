class spam:
    a = 1

    def __init__(self, b) -> None:
        self.b = b

    def increment(self):
        self.b += 1
        print(
            "\tAfter Instance method, s.increment()\n\tIncrement 'b' by 1  => b: ",
            self.b,
        )


if __name__ == "__main__":
    print("Class variable 'a' : ", spam.a)
    s = spam(5)
    print("\ns = spam(5)\n\tInstance variable 'b' : ", s.b)
    s.increment()
