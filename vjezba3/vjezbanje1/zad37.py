def fun(matrix):
    if not matrix:
        return 0

    najveci = max(matrix[0]) 

    return max(najveci, fun(matrix[1:]))

def main():
    print(fun([
        [1,2,3],
        [2,2,2],
        [45,7,8]
    ]))

if __name__ == "__main__":
    main()