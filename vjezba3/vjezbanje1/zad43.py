def fun(matrix,i):
    if not matrix:
        return []

    lst = []
    lst += [matrix[0][i]]

    return lst + fun(matrix[1:],i)

def main():
    print(fun([
        [4,6,2],
        [3,6,1],
        [2,8,6]
    ], 2))

if __name__ == "__main__":
    main()