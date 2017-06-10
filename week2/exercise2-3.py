x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break
    # when guess == 4.9, abs(4.9**2 - 25) >= 0.01 is true; guess += 0.1
    # guess == 5.0; abs(5.0**2 - 25) >= 0.01 is false;
if abs(guess**2 - x) >= epsilon:
    print("failed")
else:
    print("succeedded: " + str(guess))

# if x = 23
# when guess == 4.6, abs(4.6**2 - 23) >= epsilon is true
# guess == 4.7, abs(4.7**2 - 23) >= epsilon is true
# guess == 4.8, abs(4.8**2 - 23) >= epsilon is true
# .........
# until guess == 25
# guess == 25.1, guess <= x is false; break
# print('failed')
