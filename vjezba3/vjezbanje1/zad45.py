def fun(m):
    if not m:
        return []

    return [m[0][0]] + fun([red[1:] for red in m[1:]])


def main():
    print(fun([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))


if __name__ == "__main__":
    main()