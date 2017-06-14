def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    animals_num = 0
    for item in aDict.values():
        animals_num += len(item)
    return animals_num

print(how_many({ 'a': ['aardvark', 'da'], 'b': ['baboon'], 'c': ['coati']}))