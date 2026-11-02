def fun(s):
    if len(s) == 0:
        return True

    if s[0] != s[-1]:
        return False

    return fun(s[1:-1])

def main():
    print(fun("anavolimilovana"))

if __name__ == "__main__":
    main()