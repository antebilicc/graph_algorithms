def fun(lst):
    if lst == []:
        return 0
    return lst[0] + fun(lst[1:])

def main():
    print(fun([3, 1, 4, 1, 5]))

if __name__ == "__main__":
    main()