def fun(lst):
    if lst == []:
        return []

    if isinstance(lst[0], list):
        return fun(lst[0]) + fun(lst[1:]) #uzmi prvi element i na kraj dodaj ostatak liste 

    return [lst[0]] + fun(lst[1:])

def main():
    print(fun([1,[2,3,[4,[5,[6,7,8]]]]]))

if __name__ == "__main__":
    main()