def func(*args: list) -> None:
    """*args are used for positional arguments.
    i.e. for the arguments passed without a keyword
    """
    print(f"\n\n---> Args are stored as: {type(args).__qualname__}\n")
    print("Parsing args.....\n")
    for no, names in enumerate(args):
        print(f"Number: {no+1}")
        print([name for name in names])


if __name__ == "__main__":
    names = ["Jack", "Jill", "James", "Malone", "Marylin", "Malkovich"]
    names2 = ["Jeremy", "Zlatan", "Henry"]
    names3 = ["Leonidis", "Leah", "Lauerene", "Laurence"]
    func(names, names2, names3)
