def fun(n):
    if n == 0:
        return []
    if n % 2 == 0:
        return fun(n-1) + [n] 
    return fun(n-1)


def main():
    print(fun(6))

if __name__ == "__main__":
    main()