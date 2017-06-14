low = 0
high = 100
ans = int((low + high) / 2)
decide = True

print("Please think of a number between 0 and 100!")

while decide:
    print("Is your secret number " + str(ans))
    word = input("Enter 'h' to indicate the guess is too high."
                 "Enter 'l' to indicate the guess is too low."
                 "Enter 'c' to indicate I guessed correctly. ")
    if word == "c":
        print("Game over. your secret number was: " + str(ans))
        decide = False
    elif word == "l":
        low = ans
        ans = int((low + high) / 2)
    elif word == "h":
        high = ans
        ans = int((low + high) / 2)
    else:
        print("Sorry, I did not understand your input.")
