def fun(matrix):
    if not matrix:
        return 0

    lista = matrix[0]
    cnt = sum(1 for x in lista if x == 1)

    return cnt + fun(matrix[1:])


def main():
    print(fun([
        [1,2,12],
        [23,1,5],
        [7,9,1]
    ]))

if __name__ == "__main__":
    main()