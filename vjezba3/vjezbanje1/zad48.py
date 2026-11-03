def fun(matrica, i=0, j=0):
    m = len(matrica)
    n = len(matrica[0])

    if i >= m or j >= n:
        return 0

    if matrica[i][j] == 1:
        return 0

    if i == m - 1 and j == n - 1:
        return 1

    return fun(matrica, i, j + 1) + fun(matrica, i + 1, j)


def main():
    print(fun([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]))  

if __name__ == "__main__":
    main()