def fun(n):
    if n < 10:
        return 0

    umnozak = 1
    while n > 0:
        umnozak *= n % 10
        n //= 10

    return 1 + fun(umnozak)

def main():
    print(fun(999))

if __name__ == "__main__":
    main()