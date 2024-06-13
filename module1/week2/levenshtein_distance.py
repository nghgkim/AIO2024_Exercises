def ins_cost():
    return 1


def del_cost():
    return 1


def sub_cost(source, target):
    if source == target:
        return 0
    return 1


def levenshtein_distance(source, target):
    m = len(source) + 1
    n = len(target) + 1
    D = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        D[i][0] = i
    for j in range(n):
        D[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            D[i][j] = min(D[i-1][j] + del_cost(),
                          D[i][j-1] + ins_cost(),
                          D[i-1][j-1] + sub_cost(source[i-1], target[j-1]))

    return D[m-1][n-1]


print(levenshtein_distance('yu', 'you'))
