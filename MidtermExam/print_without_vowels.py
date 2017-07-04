def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    newString = ""
    for item in s:
        if item not in "aeiouAEIOU":
            newString += item
    print(newString)

# print(print_without_vowels("a"))
print_without_vowels("a")
