def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess_word_list = ""
    for each_letter in secretWord:
        if each_letter in lettersGuessed:
            guess_word_list += each_letter + " "
        else:
            guess_word_list += "_ "
    return guess_word_list[:-1]

print(getGuessedWord('apple', ['e', 'p', 'k', 's']))
