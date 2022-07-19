from functools import partial, wraps


def debug(func=None, *, prefix=" "):
    if func is None:
        # Wasn't passed
        return partial(debug, prefix=prefix)
    msg = prefix + func.__qualname__
    # func is the function to be wrapped
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)

    return wrapper


@debug(prefix="+++")
def add(x: int, y: int):
    return x + y


@debug(prefix="***")
def mult(x: int, y: int):
    return x * y


@debug(prefix="///")
def div(x: int, y: int) -> float:
    return x / y


if __name__ == "__main__":
    x = add(8, 9)
    print(x)
    x = mult(8, 9)
    print(x)
    x = div(8, 9)
    print(x)
