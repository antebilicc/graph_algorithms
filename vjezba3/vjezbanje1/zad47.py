def fun(m, n): #putevi mogući od gore lijevo do dolje desno ali samo ići korak dolje ili korak desno
    if m == 1 or n == 1:
        return 1

    return fun(m - 1, n) + fun(m, n - 1)


def main():
    print(fun(3, 3))  


if __name__ == "__main__":
    main()