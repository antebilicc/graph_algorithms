def fun(n):
    if n == 0:
        return 0
    if (n % 10) %2 == 1:
        return 1 + fun(n//10)
    return fun(n // 10)

def main():
    print(fun(123455))

if __name__ == "__main__":
    main()