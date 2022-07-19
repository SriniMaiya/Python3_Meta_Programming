from functools import wraps

# Copies metadata of the wrapped function and stores


def debug(func):
    # func is a function to be wrapped
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Print debug message and return the function with the parameters back
        print("-->", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


@debug
def add(x: int, y: int):
    return x + y


@debug
def mult(x: int, y: int):
    return x * y


@debug
def div(x: int, y: int) -> float:
    return x / y


if __name__ == "__main__":
    x = add(5, 6)
    print(x)
    x = mult(5, 6)
    print(x)
    x = div(5, 6)
    print(x)
    print(add.__qualname__)  # Prints function name only with wraps module imported
