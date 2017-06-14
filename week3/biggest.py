def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict) == 0:
        return None
    else:
        max_length = 0
        max_key = ''
        for item in aDict.keys():
            if len(aDict[item]) > max_length:
                max_length = len(aDict[item])
                max_key = item
        return max_key

print(biggest({ 'a': ['aardvark'], 'b': ['baboon', 'fad'], 'c': ['coati']}))