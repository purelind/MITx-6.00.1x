def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    smallerItem = min(a, b)
    while b % smallerItem != 0 or a % smallerItem != 0:
        smallerItem -= 1
    return smallerItem

print(gcdIter(17, 12))