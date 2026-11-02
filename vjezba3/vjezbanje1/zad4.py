def fun(n):
    if n == 0:
        return True
    if n % 10 != 1:
        return False
    return fun(n // 10)

def main():
    print(fun(121))

if __name__ == "__main__":
    main()