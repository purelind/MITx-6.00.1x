def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def returnFunction(x):
        listCopy = L
        indexNum = len(L) - 1
        polyValue = 0
        for item in listCopy:
            polyValue += item * x**indexNum
            indexNum -= 1
        return polyValue
    return returnFunction

print(general_poly([1, 2, 3, 4])(10))
