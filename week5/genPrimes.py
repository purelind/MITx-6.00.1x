def genPrimes():
    primesList = []
    testNum = 2
    while True:
        isPrime = True
        for item in primesList:
            if testNum % item == 0:
                isPrime = False
                break
        if isPrime:
            primesList.append(testNum)
            yield testNum
            testNum += 1
        else:
            testNum += 1

x = genPrimes()
print(next(x))
print(next(x))
print(next(x))
print(next(x))