def sum_digits(s):
    """
    assumes s a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s it raises a ValueError exception.
    """
    sum_of_digits = 0
    count = 0
    for item in s:
        if item in list('0123456789'):
            sum_of_digits += int(item)
            count += 1
    if not count:
        raise ValueError
    return sum_of_digits

print(sum_digits("a;"))