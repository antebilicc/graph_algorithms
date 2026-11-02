def fun(a, b):
    if a == []:
        return b

    if b == []:
        return a
    
    return [a[0], b[0]] + fun(a[1:], b[1:])


def main():
    print(fun([1,2,3,4,5,6], ["a", "b", "c"]))

if __name__ == "__main__":
    main()