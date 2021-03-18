def counterClockwise(matrix):
    y = list()
    z = list()

    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix)):
            z.append(matrix[j][i])
        y.append(z)
        z = list()
    
    return list(i for i in y)

print(counterClockwise([[1,2,3],[4,5,6],[7,8,9]]))