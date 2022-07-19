class first(object):
    def __init__(self) -> None:
        # Print parent class when inherited from 'third'
        print("first.__init__ ")


class second(object):
    def __init__(self) -> None:
        print("Second")

    def show(self) -> None:
        print(f"second.show()")


class third(first, second):
    def __init__(self) -> None:

        print(f"\n\nClass Name:\t{self.__class__.__name__} ")
        print(f"\t Super classes:\t\t{self.__class__.__bases__} ")
        print(f"\t MRO first lookup:\t{self.__class__.__base__} ", end="\t")
        print(
            f"*** If not in {self.__class__.__base__}, look in {self.__class__.__bases__[1]}\n\n "
        )
        print("third.__init__", end=" --> ")
        super().__init__()

    def show(self) -> None:
        print("third.show()", end=" --> ")
        return super().show()


if __name__ == "__main__":

    t = third()
    t.show()

    print("\n\nMRO of class 'third':\n", third.mro())
