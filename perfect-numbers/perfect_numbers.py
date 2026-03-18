def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    result = 0

    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')

    for factor in range(1, number):
        if number % factor  == 0:
            result += factor

    if result == number:
        return 'perfect'
    if result > number:
        return 'abundant'
    return 'deficient'
