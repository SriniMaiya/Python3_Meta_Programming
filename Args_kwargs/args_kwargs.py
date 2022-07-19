def func(*args, **kwargs) -> None:
    """*args are used for positional arguments.
    i.e. for the arguments passed without a keyword
    """
    print(f"\n\n---> Args are stored as: {type(args).__qualname__}")
    print(f"---> Kwargs are stored as: {type(kwargs).__qualname__}\n")

    print("Parsing args and kwargs.....\n")
    print("*" * 10)
    [print(arg) for arg in args]
    print("*" * 10)

    for key in kwargs.keys():
        print("--> key", key)
        print(kwargs[key])


if __name__ == "__main__":
    names = {"name1": "Jeremy", "name2": "Zlatan", "name3": "Henry"}
    ages = {"age1": 38, "age2": 32, "age3": 29}
    # "Python Args and Kwargs", "Name: Name and Age" ---> Args
    # name=names, age=ages                           ---> Kwargs
    func("Python Args and Kwargs", "Name: Name and Age", name=names, age=ages)
