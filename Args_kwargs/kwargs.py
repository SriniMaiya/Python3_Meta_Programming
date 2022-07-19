def func(**kwargs):
    """**kwargs unpacks the keyword(named) arguments"""
    print(f"\n\n---> Args are stored as: {type(kwargs).__qualname__}\n")
    print("Parsing kwargs.....\n")
    for key in kwargs.keys():
        print("-->", key)
        print(kwargs[key])


if __name__ == "__main__":
    names = {"name1": "Jeremy", "name2": "Zlatan", "name3": "Henry"}
    ages = {"age1": 38, "age2": 32, "age3": 29}
    func(names=names, ages=ages)
