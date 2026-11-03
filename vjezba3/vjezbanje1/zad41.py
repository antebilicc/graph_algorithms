def fun(matrica):
    if not matrica:
        return 0
    rez = 0
    for x in matrica[0]:
        if x % 2 == 0:
            rez += 1
    return rez + fun(matrica[1:])

def main():
    print(fun([
        [1,2,12],
        [23,2,5],
        [7,9,1]
    ]))

if __name__ == "__main__":
    main()