from time import time


def timer(start: time, end: time) -> str:
    if start and end:
        return f"Time difference is: {end - start} seconds"
    elif start or end:
        if start:
            return f"Starting time point is:{start} "
        if end:
            return f"End time point is: {end}"


if __name__ == "__main__":
    start = time()
    time.sleep(6)
    end = time()
    print(timer(start=start, end=None))
    print(timer(start=None, end=end))
    print(timer(start=start, end=end))
