import logging
from functools import wraps


def debug(func):

    log = logging.getLogger(__name__)
    log.setLevel("INFO")
    msg = func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(msg=msg)

        if any(type(x) != int for x in args) or any(type(x) != int for x in kwargs):
            logging.error("Not int", exc_info=True)
            exit(-1)
        return func(*args, **kwargs)

    print(log.info(msg))
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

    add(7, "a")
