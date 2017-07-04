def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    i = 0
    currentSum = 0
    while currentSum < k:
        i += 1
        currentSum += i
        if k == currentSum:
            return True
    return False

print(is_triangular(10))
