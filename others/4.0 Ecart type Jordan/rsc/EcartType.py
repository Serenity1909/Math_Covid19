def EcartType (mtx1, mtx2):
    res = 0
    for i in range(0, 4, 1):
        res += (mtx1[i, 0] - mtx2[i, 0]) ** 2
    return res/5