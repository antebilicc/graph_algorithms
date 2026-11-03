def fun(matrica, broj):
    if not matrica:
        return []

    lst = []
    for x in matrica[0]:
        lst += [x * broj]

    return [lst] + fun(matrica[1:], broj)

def main():
    print(fun([
        [1,2,12],
        [23,1,5],
        [7,9,1]
    ], 4))

if __name__ == "__main__":
    main()