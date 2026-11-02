def fun(n):
    if n < 10:
        return True
    if abs(n % 10 - (n // 10) % 10) != 1:
        return False

    return fun(n//10)

def main():
    print(fun(563765))

if __name__ == "__main__":
    main()  