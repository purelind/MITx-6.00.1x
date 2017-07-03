WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    handcopy = hand.copy()
    wordListCopy = wordList.copy()
    for letter in word:
        if letter not in handcopy.keys():
            return False
        else:
            handcopy[letter] -= 1
            if handcopy[letter] < 0:
                return False

    def binarySearchWord(word, wordList, lo, hi):
        if lo > hi:
            return False
        mid = lo + (hi - lo) // 2
        if word < wordList[mid]:
            return binarySearchWord(word, wordList, lo, mid - 1)
        elif word > wordList[mid]:
            return binarySearchWord(word, wordList, mid + 1, hi)
        else:
            return True
    return binarySearchWord(word, wordList, 0, len(wordList) - 1)

def binarySearchWord(word, wordList, lo, hi):
    if lo > hi:
        return False
    mid = lo + (hi - lo) // 2
    if word < wordList[mid]:
        return binarySearchWord(word, wordList, lo, mid - 1)
    elif word > wordList[mid]:
        return binarySearchWord(word, wordList, mid + 1, hi)
    else:
        return True


wordList = loadWords()
print(binarySearchWord("duck", wordList, 0, len(wordList)-1))
print(isValidWord("duck", {'t': 1, 'd': 1, 'u': 1, 'c': 1, 'g': 1, 'k': 1, 'i': 1, 'a': 1},  wordList))
