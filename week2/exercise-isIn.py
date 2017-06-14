def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    midIndex = round(len(aStr)/2)
    if len(aStr) == 0 or len(aStr) == 1 and char != aStr[0]:
        return False
    # elif len(aStr) == 1 and char != aStr[0]:
    #     return False
    elif char == aStr[midIndex]:
        return True
    elif char < aStr[midIndex]:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])

print(isIn('e', 'bcfhhiklnrsvxxy'))