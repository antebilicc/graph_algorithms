def fun(lst):
    if lst == []:
        return 0
    return 1 + fun(lst[1:])

def main():
    print(fun([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()