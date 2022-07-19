from inspect import Parameter, Signature

_fields = ["name", "shares", "price"]
parms = [Parameter(fname, Parameter.POSITIONAL_OR_KEYWORD) for fname in _fields]

print("---> Parameters: \n", parms)

sig = Signature(parameters=parms)
print("---> Signatures: \n", sig)


def foo(*args, **kwargs):
    bound = sig.bind(*args, **kwargs)
    for name, val in bound.arguments.items():
        print(name, val)
    print("_" * 10)


if __name__ == "__main__":
    print("\n____main____: Error handling with signature creation")
    x = foo("GOOG", price=40.1, shares=25)

    try:
        foo("GOOG", 40.1)
    except TypeError as e:
        print("---> Only two parameters passed: ")
        print(e)
        print("_" * 10)

    try:
        foo("GOOG", 40.1, 250, 122)
    except TypeError as e:
        print("---> Only two parameters passed: ")
        print(e)
        print("_" * 10)
