def fun(str):
    if len(str) == 0:
        return 0
    if str[0] in "aeiouAEIOU":
        return 1 + fun(str[1:])
    return fun(str[1:])

def main():
    print(fun("rekurzija"))

if __name__ == "__main__":
    main()