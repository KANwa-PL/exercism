def steps(number):
    steps_ = 0

    if number < 1:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            steps_ += 1
        else:
            number = number * 3 + 1
            steps_ += 1

    return steps_
