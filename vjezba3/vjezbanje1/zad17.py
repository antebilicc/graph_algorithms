def fun(lst):
    if lst == []:
        return []

    return [lst[0] ** 2] + fun(lst[1:])


def main():
    print(fun([1,2,3,4]))

if __name__ == "__main__":
    main()