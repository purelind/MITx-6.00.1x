import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lettes_list = list(string.ascii_lowercase)

    for each_letter in lettersGuessed:
        lettes_list.remove(each_letter)
    return ''.join(lettes_list)

print(getAvailableLetters(['e', 'a']))
