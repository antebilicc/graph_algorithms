def fun(matrica, broj):
    if not matrica:
        return False

    for x in matrica[0]:
        if x == broj:
            return True

    return fun(matrica[1:], broj)
    

def main():
    print(fun([
        [1,2,12],
        [23,1,5],
        [7,9,1]
    ], 3))

if __name__ == "__main__":
    main()