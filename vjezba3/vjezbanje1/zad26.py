def fun(lst):
    if len(lst) == 0:
        return [[]]

    ostali = fun(lst[1:])
    
    return ostali + [[lst[0]] + x for x in ostali]

def main():
    print(fun([1,2,3]))

if __name__ == "__main__":
    main()