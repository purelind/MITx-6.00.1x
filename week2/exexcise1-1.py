iteration = 0
count = 0
while iteration < 5:
    # the variable "letter" in the loop stands for every
    # character, including spaces and commas!
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

# len("hello, world") --> 12
# iteration     count
#     0           12
#     1           24
#     2           36
#     3           48
#     4           60
