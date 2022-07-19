from unicodedata import name


def func(x: int = 0, debug: bool = False, names: list = None):
    if names is None or len(names) == 0:
        print("No names yet.")
    elif debug is True and x >= 0:
        print(names[x])
    elif debug is False:
        print([x for x in names])


if __name__ == "__main__":
    names = ["Jack", "Jill", "James", "Malone", "Marylin", "Malkovich"]
    names1 = []
    func(names=names1)
    func(x=0, names=names)
    func(x=5, debug=True, names=names)
