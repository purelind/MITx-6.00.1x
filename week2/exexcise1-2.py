iteration = 0
while iteration < 5:
    count = 0   # init count to 0 for every loop
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
# iteration     count
#     0           12
#     1           12
#     2           12
#     3           12
#     4           12