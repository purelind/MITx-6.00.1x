x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 - x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

# guess = 4.9, abs(4.9**2 - 25) > epsilon
# guess = 5.0, abs(5.0**2 - 25) < epsilon; break
