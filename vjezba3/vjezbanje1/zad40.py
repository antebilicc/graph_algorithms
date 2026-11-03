def fun(matrica):
    if not matrica:
        return []

    return [sum(matrica[0])] + fun(matrica[1:])

def main():
    print(fun([
        [1,2,12],
        [23,1,5],
        [7,9,1]
    ]))

if __name__ == "__main__":
    main()