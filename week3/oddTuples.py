def oddTuples(aTup):
    """

    :param aTup:
    :return:
    """
    newTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            newTup += (aTup[i],)
    return newTup

print(oddTuples((1,2,3,4)))