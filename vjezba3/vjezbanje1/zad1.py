def fun(n):
    if n == 1:
        return [1]
    return [n] + fun(n-1) + [n]


def main():
    print(fun(5))


if __name__ == "__main__":
    main()