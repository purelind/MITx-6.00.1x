def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
    dicHelp = {}
    for item in L:
        if item in dicHelp.keys():
            dicHelp[item] += 1
        else:
            dicHelp[item] = 1

    dicHelpCopy = dicHelp.copy()
    for eachKey in dicHelp.keys():
        if dicHelp[eachKey] % 2 == 0:
            dicHelpCopy.pop(eachKey)
    if not dicHelpCopy:
        return
    else:
        return max(dicHelpCopy.keys())


print(largest_odd_times([3, 3, 2, 0]))
