def fun(lst ):
    if len(lst) == 0:
        return {}
    return {lst[0]:len(lst[0])} | fun(lst[1:])

def main():
    print(fun(["abc", "ab", "c"]))

if __name__== "__main__":
    main()