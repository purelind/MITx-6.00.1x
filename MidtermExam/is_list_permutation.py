def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    def listToDict(List):
        newDict = {}
        listCopy = List.copy()
        for item in listCopy:
            if item in newDict.keys():
                newDict[item] += 1
            else:
                newDict[item] = 1
        return newDict
    dict1 = listToDict(L1)
    dict2 = listToDict(L2)
    for eachkey in dict1.keys():
        if eachkey not in dict2.keys():
            return False
        elif dict1[eachkey] != dict2[eachkey]:
            return False
    for eachkey in dict2.keys():
        if eachkey not in dict1.keys():
            return False
        elif dict1[eachkey] != dict1[eachkey]:
            return False
    elementOccurMost = ""
    maxOccurNumber = 0
    if not dict1.keys():
        return (None, None, None)
    for eachkey in dict1.keys():
        if dict1[eachkey] > maxOccurNumber:
            maxOccurNumber = dict1[eachkey]
            elementOccurMost = eachkey
    return (elementOccurMost, maxOccurNumber, type(elementOccurMost))

print(is_list_permutation([1], ['1', 1]))