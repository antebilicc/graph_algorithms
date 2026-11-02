def fun(lst):
    if lst == []:
        return 1

    if isinstance(lst[0], list):
        return max(1 + fun(lst[0]), fun(lst[1:]))

    return fun(lst[1:])

def main():
    print(fun([1,[2,3,[4,[5,[6,7,8]]]]]))

if __name__ == "__main__":
    main()