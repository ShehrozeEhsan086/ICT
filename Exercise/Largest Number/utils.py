def find_largest(x):
    largest = x[0]
    for number in x:
        if number > largest:
            largest = number
    return largest