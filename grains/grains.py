def square(number):
    if 0 < number < 65:
        return 1 + sum(2 ** (item - 1) for item in range(1, number))
    raise ValueError('square must be between 1 and 64')


def total():
    return 2 ** 64 - 1
