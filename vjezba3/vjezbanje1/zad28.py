def fun(lst , lst2):
    if len(lst) == 0 and len(lst2) == 0:
        return {}
    return {lst[0]:lst2[0]} | fun(lst[1:], lst2[1:]) 

def main():
    print(fun(["a", "b", "c"],[1,2,3]))

if __name__== "__main__":
    main()