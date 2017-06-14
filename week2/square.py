# def square(x):
#     '''
#
#     :param x:
#     :return:
#     '''
#     epsilon = 0.01
#     guess = x / 2.0
#
#     while abs(guess * guess - x) >= epsilon:
#         guess = guess - (((guess ** 2) - x) / (2 * guess))
#     return guess
#
# y = int(input("Enter a number: "))
# print("Square root of x is: " + str(square(y)))

def square(x):
    '''
    x: int or float.
    '''
    return x*x

y = int(input("Enter a number: "))
print("Square root of x is: " + str(square(y)))