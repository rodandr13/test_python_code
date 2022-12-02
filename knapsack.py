"""
Дискретная задача о рюкзаке. Собрать наибольшую ценность предметов в рюкзаке
"""


def knapsack(v, m, N, M):
    F = [[0] * (N + 1) for i in range(M + 1)]
    for i in range(N):
        for k in range(M + 1):
            if m[i] <= k:
                F[k][i] = max(F[k][i-1], v[i] + F[k-m[i]][i-1])
            else:
                F[k][i] = F[k][i-1]
    return F[-1]


m = [2, 1, 3, 4]
v = [5, 4, 7, 11]
N = len(m)
M = 10

print(knapsack(v, m , N, M))
