def func_fibonacci(*, length: int = 10) -> None:
    fibonacci_numbers = [0, 1]
    for i in range(2, length):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers


if __name__ == "__main__":
    x = func_fibonacci(length=10)
    # x = func_fibonacci(15)
    # ERROR: TypeError: func_fibonacci() takes 0 positional arguments but 1 was given
    print(x)
