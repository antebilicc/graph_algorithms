def fun(lst):
    if lst == []:
        return 0

    if isinstance(lst[0], list):
        return fun(lst[0]) + fun(lst[1:])

    return lst[0] + fun(lst[1:])


def main():
    print(fun([1, [2, [3, 4]], 5]))


if __name__ == "__main__":
    main()