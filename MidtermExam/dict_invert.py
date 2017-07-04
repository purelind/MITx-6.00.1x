def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    dictCopy = d.copy()
    invertDict = {}
    for eachKey in dictCopy.keys():
        eachValue = dictCopy[eachKey]
        if eachValue in invertDict.keys():
            invertDict[eachValue].append(eachKey)
        else:
            invertDict[eachValue] = [eachKey]
    for item in invertDict.values():
        item.sort()
    return invertDict

print(dict_invert({4:True, 2:True, 0:True}))
