def fun(lst):
    if len(lst) == 1:
        return lst[0]

    maks = lst[0]
   
    if maks < fun(lst[1:]):
        maks = fun(lst[1:])
        
    return maks

def main():
    print(fun([1, 6, 3, 7, 5]))

if __name__ == "__main__":
    main()