x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 - x) >= epsilon:
        guess += step
    # when guess == 5, no operation, guess == 5 forever, enter an infinite while loop
if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

