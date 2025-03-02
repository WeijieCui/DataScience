import math


def cholesky_decomposition(mat: list[list]):
    n = len(mat)
    l = [[0] * n for _ in range(n)]
    for i in range(0, n):
        square = mat[i][i]
        for j in range(i):
            square -= l[i][j] ** 2
        l[i][i] = math.sqrt(square)
        for j in range(i + 1, n):
            product = mat[i][j]
            for k in range(j - 1):
                product -= l[i][k] * l[j][k]
            l[j][i] = 0 if l[i][i] == 0 else product / l[i][i]
    for row in l:
        print(row)
    return l


if __name__ == '__main__':
    matrix = [
        [3, -1, 0, -1, 0],
        [-1, 3, -1, 3, -1],
        [0, -1, 3, 1, 0],
        [-1, 3, 1, 5, -1],
        [0, -1, 0, -1, 1]
    ]
    cholesky_decomposition(matrix)
# [1.7320508075688772, 0, 0, 0, 0]
# [-0.5773502691896258, 1.632993161855452, 0, 0, 0]
# [0.0, -0.6123724356957945, 1.620185174601965, 0, 0]
# [-0.5773502691896258, 1.632993161855452, 1.2344267996967353, 0.6900655593423545, 0]
# [0.0, -0.6123724356957945, -0.23145502494313783, 0.4140393356054122, 0.6324555320336761]
